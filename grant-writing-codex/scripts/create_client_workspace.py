from argparse import ArgumentParser
from datetime import date
from pathlib import Path
import re
import shutil


CLIENT_SUBDIRS = [
    "01_PreAward/Opportunity_Research",
    "01_PreAward/Proposal_Drafts",
    "01_PreAward/Budgets",
    "01_PreAward/Attachments",
    "02_Award",
    "03_PostAward/Reports",
    "03_PostAward/Financials",
    "Templates_Resources",
    "Research_Database",
]


SAFE_RE = re.compile(r"[^A-Za-z0-9._-]+")


def create_client_workspace(root: Path, client_name: str) -> Path:
    client_dir = root / "Clients" / slugify(client_name)
    for folder in CLIENT_SUBDIRS:
        (client_dir / folder).mkdir(parents=True, exist_ok=True)
    return client_dir


def enforce_file_name(original_name: str, description: str, version: str = "v1") -> str:
    original = Path(original_name)
    safe_description = slugify(description).replace("-", "_")
    return f"{date.today().isoformat()}_{safe_description}_{version}{original.suffix.lower()}"


def rename_into(target_dir: Path, source_path: Path, description: str, version: str = "v1") -> Path:
    target_dir.mkdir(parents=True, exist_ok=True)
    target_name = enforce_file_name(source_path.name, description=description, version=version)
    destination = target_dir / target_name
    shutil.copy2(source_path, destination)
    return destination


def slugify(value: str) -> str:
    clean = SAFE_RE.sub("-", value.strip())
    return clean.strip("-").lower()


def main() -> None:
    parser = ArgumentParser(description="Create the Master Grant Writer client directory structure.")
    parser.add_argument("client_name")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()

    client_dir = create_client_workspace(Path(args.root), args.client_name)
    print(client_dir)


if __name__ == "__main__":
    main()

