# Awesome BJJ Data

Curated datasets and tools for Brazilian Jiu-Jitsu research, analysis, and visualization.

## Categories
- Competition Datasets
- Moves/Techniques Datasets
- Athletes and Gyms
- Physiology and Training
- Visualizations

## Quick Start
1. Clone the repo.
2. Install Python 3.11+ and `uv` or `poetry`.
3. `pip install -r requirements.txt` or `uv pip install -r requirements.txt`.
4. Validate the registry: `python scripts/validate_registry.py`.

## Competition Datasets
- IBJJF medal and bracket results
- ADCC brackets and results
- Grappling Industries event results
- Smoothcomp exports for local events

## Moves/Techniques Datasets
- Technique taxonomy with unique IDs
- Labeled examples with position, sub-position, transition, and tags
- Frame-level or event-level annotations for sequences

## Athletes and Gyms
- Athlete master list with aliases
- Gym directory with locations and affiliations
- Athlete-gym-time affiliation edges

## Physiology and Training
- Training load logs
- HRV and recovery snapshots
- Drilling and sparring breakdowns

## Visualizations
- Notebooks and scripts to reproduce charts
- Ready-made dashboards for competition trends

## External Resources
For additional BJJ data sources, APIs, and datasets, see [EXTERNAL_RESOURCES.md](EXTERNAL_RESOURCES.md). This includes links to:
- Official competition results (ADCC, IBJJF, Grappling Industries)
- Data aggregators (BJJ Heroes, FloGrappling, Less Impressed More Involved)
- Kaggle datasets (ADCC historical data, grappling techniques)
- APIs and technical resources for data collection

## How to Contribute
See [CONTRIBUTING.md](CONTRIBUTING.md). Add a new dataset by creating a file in `datasets/...` and a matching entry in `registry/datasets.json`.
