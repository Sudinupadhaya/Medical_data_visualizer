# Medical Data Visualizer

This project analyzes medical examination data and creates visual summaries using Python. It is based on the freeCodeCamp Data Analysis with Python project structure, with a small sample dataset included so the project can run locally.

## Goal

The goal is to explore how basic health indicators relate to cardiovascular disease. The project uses data cleaning, feature engineering, categorical comparison, and correlation analysis.

## Dataset

The dataset file is `medical_examination.csv`.

Main columns:

- `id`
- `age`
- `gender`
- `height`
- `weight`
- `ap_hi`
- `ap_lo`
- `cholesterol`
- `gluc`
- `smoke`
- `alco`
- `active`
- `cardio`

## Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## What the Project Does

- Reads the medical examination dataset
- Adds an `overweight` column using BMI logic
- Normalizes cholesterol and glucose values
- Creates a categorical plot for selected health indicators
- Creates a correlation heatmap after removing invalid records
- Saves output charts as image files

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

After running, the project creates:

```text
catplot.png
heatmap.png
```

## Note

The included CSV is a small sample dataset for demo and portfolio use. For the full freeCodeCamp project, replace it with the official `medical_examination.csv` dataset.

## Author

Sudin Upadhaya
