from __future__ import annotations
from pathlib import Path
from typing import List, Literal
import json
from pydantic import BaseModel, HttpUrl, Field, ValidationError


class DatasetItem(BaseModel):
    id: str = Field(pattern="^[a-z0-9-]+$")
    name: str
    category: Literal["competitions", "techniques", "athletes", "gyms", "physiology"]
    path: str
    format: Literal["csv", "json", "jsonl", "parquet"]
    source_url: HttpUrl | str
    license: str
    description: str | None = None
    updated_at: str | None = None
    columns: List[str] | None = None


def main() -> None:
    registry_path = Path("registry/datasets.json")
    data = json.loads(registry_path.read_text())
    items = [DatasetItem(**it) for it in data]
    missing = [it for it in items if not Path(it.path).exists()]
    if missing:
        names = ", ".join([m.id for m in missing])
        raise SystemExit(f"Files missing for: {names}")
    print(f"OK: {len(items)} dataset entries")


if __name__ == "__main__":
    main()
