# Medical Data Visualizer

This is a Python practice project for working with medical examination data. I used Pandas for data cleaning and Seaborn/Matplotlib for the charts.

The project is based on the freeCodeCamp Medical Data Visualizer exercise. I included a small CSV file in this repository so the code can be run and checked easily.

## What I worked on

- Reading a CSV file with Pandas
- Adding an `overweight` column from height and weight
- Converting cholesterol and glucose values into simple normal/high values
- Reshaping the data for a categorical chart
- Cleaning unusual blood pressure, height, and weight records before making the heatmap
- Saving the final charts as image files

## Files

```text
README.md
medical_data_visualizer.py
main.py
requirements.txt
medical_examination.csv
```

## Columns in the dataset

```text
id, age, gender, height, weight, ap_hi, ap_lo,
cholesterol, gluc, smoke, alco, active, cardio
```

## How to run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

It will create two files:

```text
catplot.png
heatmap.png
```

## Notes

The CSV in this repository is a small sample dataset for running the project. For the full freeCodeCamp version, the same code structure can be used with the official `medical_examination.csv` file.

## Author

Sudin Upadhaya
