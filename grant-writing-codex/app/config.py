from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

DEFAULT_DB_URL = f"sqlite:///{DATA_DIR / 'grant_codex.db'}"

