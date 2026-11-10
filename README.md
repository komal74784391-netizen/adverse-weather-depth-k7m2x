# adverse-weather-depth

Benchmark code for **"Outdoor Depth Estimation under Adverse Weather: A
Benchmark"** (WACV 2024).

This repository contains the dataset loaders, the evaluation metrics and the
scripts used to reproduce the leaderboard in the paper.

## Layout

- `src/benchmark/datasets.py` - rain/fog/snow splits
- `src/benchmark/metrics.py` - depth metrics
- `scripts/run_benchmark.py` - end-to-end evaluation
- `configs/bench.yaml` - benchmark configuration
