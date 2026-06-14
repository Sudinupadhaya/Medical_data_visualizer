import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("medical_examination.csv")

# BMI > 25 is treated as overweight.
df["overweight"] = ((df["weight"] / ((df["height"] / 100) ** 2)) > 25).astype(int)

# Normalize cholesterol and glucose values: 0 = normal, 1 = above normal.
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)


def draw_cat_plot():
    """Create a categorical plot for selected health indicators."""
    columns = ["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]

    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=columns,
        var_name="variable",
        value_name="value",
    )

    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    chart = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
    )

    fig = chart.fig
    fig.savefig("catplot.png")
    return fig


def draw_heat_map():
    """Create a correlation heatmap after removing invalid records."""
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    corr = df_heat.corr(numeric_only=True)
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        linewidths=0.5,
        square=True,
        cbar_kws={"shrink": 0.7},
        ax=ax,
    )

    fig.savefig("heatmap.png")
    return fig
