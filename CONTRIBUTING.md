# Contributing

## Principles
- Respect licenses and terms of service.
- Prefer open formats: CSV, Parquet, JSONL.
- Include a `source_url` and `license` for each dataset.

## Add a Dataset
1. Place the file under an appropriate `datasets/` subfolder.
2. Add a JSON entry to `registry/datasets.json` that conforms to `schemas/dataset.schema.json`.
3. Run `python scripts/validate_registry.py`.
4. Open a PR with a short description and sample queries.

## Naming
- Use `kebab-case` filenames.
- Include year and event in competition files.
- Use UTC dates in ISO-8601.

## Quality
- No personally sensitive data for minors.
- Provide a `README` snippet or docstring in notebooks.
