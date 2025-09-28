from __future__ import annotations
from pathlib import Path
from typing import Literal, Iterable
import json, datetime as dt
import pandas as pd
import httpx
from pydantic import BaseModel, HttpUrl

RawFormat = Literal["csv", "json"]


class SourceCfg(BaseModel):
    id: str
    org: str
    mode: Literal["results", "export"]
    cadence: Literal["manual", "weekly", "monthly"]
    event_ids: list[str] | None = None


class Config(BaseModel):
    competitions: list[SourceCfg] = []
    rankings: list[SourceCfg] = []


def ts() -> str:
    return dt.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")


def fetch_text(url: str) -> str:
    with httpx.Client(timeout=30) as client:
        r = client.get(
            url, follow_redirects=True, headers={"User-Agent": "awesome-bjj-data/1.0"}
        )
        r.raise_for_status()
        return r.text


def write_text(p: Path, s: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s)


def normalize_competitions(frames: Iterable[pd.DataFrame]) -> pd.DataFrame:
    cols = [
        "event",
        "date",
        "org",
        "ruleset",
        "division",
        "belt",
        "weight",
        "gender",
        "round",
        "athlete_a",
        "athlete_b",
        "winner",
        "method",
        "time",
        "points_a",
        "points_b",
        "adv_a",
        "adv_b",
        "pen_a",
        "pen_b",
        "gi",
    ]
    df = pd.concat(frames, ignore_index=True).reindex(columns=cols)
    df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date
    df["org"] = df["org"].str.lower()
    df = df.drop_duplicates()
    return df


def run() -> None:
    cfg = Config.model_validate_json(Path("ingest/config.yaml").read_text())
    raw_frames: list[pd.DataFrame] = []

    for src in cfg.competitions:
        if src.org == "ibjjf":
            url = "https://example-ibjjf-results-endpoint"  # replace with your fetcher logic
            raw_json = fetch_text(url)
            write_text(Path(f"data/raw/ibjjf/{ts()}.json"), raw_json)
            records = json.loads(raw_json)
            raw_frames.append(pd.DataFrame.from_records(records))
        elif src.org == "adcc":
            url = "https://example-adcc-results-endpoint"
            raw_json = fetch_text(url)
            write_text(Path(f"data/raw/adcc/{ts()}.json"), raw_json)
            records = json.loads(raw_json)
            raw_frames.append(pd.DataFrame.from_records(records))
        elif src.org == "smoothcomp":
            frames: list[pd.DataFrame] = []
            for eid in src.event_ids or []:
                url = f"https://example-smoothcomp-export/{eid}.json"
                raw_json = fetch_text(url)
                write_text(Path(f"data/raw/smoothcomp/{eid}.json"), raw_json)
                records = json.loads(raw_json)
                frames.append(pd.DataFrame.from_records(records))
            if frames:
                raw_frames.append(pd.concat(frames, ignore_index=True))

    if raw_frames:
        df = normalize_competitions(raw_frames)
        out = Path("data/curated/competitions.parquet")
        out.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(out, index=False)


if __name__ == "__main__":
    run()
