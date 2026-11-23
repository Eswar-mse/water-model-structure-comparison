"""Replot the README analyses with a dark theme from their numeric outputs.

Run from this repository with `python3 scripts/plot_readme_dark.py`.
The original simulation/analysis scripts are unavailable; this script redraws
the same measured quantities without changing values or condition labels.
The PCA panel is explicitly an occupancy map, not the historical FEL estimate.
"""

from pathlib import Path
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/water-model-mpl")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, LogNorm, TwoSlopeNorm
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
INPUTS = ROOT / "data" / "readme_inputs"
OUT = ROOT / "figures" / "dark"
OUT.mkdir(parents=True, exist_ok=True)
MODELS = ("OPC", "SPCE", "TIP3P", "TIP4P")
STARTS = ("CRYSTAL", "PREDICTED")
BG, PANEL, FG, MUTED, GRID = "#090b10", "#151921", "#f3f5f8", "#aeb8c8", "#343b48"
CRYSTAL, PREDICTED = "#ff5b68", "#77c9f0"
MODEL_COLORS = {"OPC": "#ff5b68", "SPCE": "#ffb86b", "TIP3P": "#77c9f0", "TIP4P": "#b69aff"}
DENSITY = LinearSegmentedColormap.from_list("ember", ["#202531", "#672444", "#d94958", "#ffbb8a", "#fff0ce"])
DIVERGING = LinearSegmentedColormap.from_list("corr", ["#75c7f2", "#3b6d8e", "#192332", "#8f3545", "#ff6974"])


def label_model(model):
    return "SPC/E" if model == "SPCE" else model


def style(ax):
    ax.set_facecolor(PANEL)
    ax.tick_params(colors=MUTED, labelsize=9, length=0)
    for spine in ax.spines.values():
        spine.set_color(GRID)
    ax.grid(color=GRID, alpha=0.35, linewidth=0.6)
    ax.set_axisbelow(True)
    ax.xaxis.label.set_color(MUTED)
    ax.yaxis.label.set_color(MUTED)
    ax.title.set_color(FG)


def canvas(rows, cols, size, title, subtitle=None, **kwargs):
    fig, axes = plt.subplots(rows, cols, figsize=size, facecolor=BG, **kwargs)
    fig.suptitle(title, color=FG, weight="bold", fontsize=19, x=0.045, ha="left", y=0.99)
    if subtitle:
        fig.text(0.045, 0.951, subtitle, color=MUTED, fontsize=10.5, ha="left")
    for ax in np.ravel(axes):
        style(ax)
    return fig, axes


def save(fig, name, rect=(0, 0, 1, 0.93)):
    fig.tight_layout(rect=rect, pad=1.4)
    fig.savefig(OUT / name, dpi=170, facecolor=BG, bbox_inches="tight")
    plt.close(fig)
    print(name)


def time_grid(data, columns, titles, filename, title, ylabels, figsize=(17, 10.5)):
    fig, axes = canvas(len(columns), 4, figsize, title, "Red: crystal start  ·  blue: predicted start  ·  each column is a water model")
    for c, model in enumerate(MODELS):
        for r, col in enumerate(columns):
            ax = axes[r, c]
            for start, color in (("CRYSTAL", CRYSTAL), ("PREDICTED", PREDICTED)):
                part = data[(data.water_model == model) & (data.start_struct == start)]
                ax.plot(part.time_ns, part[col], color=color, lw=0.65, alpha=0.75, label=start.title())
            ax.set_xlim(0, 300)
            ax.set_title(f"{label_model(model)} · {titles[r]}", fontsize=11, weight="bold")
            if c == 0:
                ax.set_ylabel(ylabels[r], fontsize=10)
            if r == len(columns) - 1:
                ax.set_xlabel("Time (ns)", fontsize=10)
            if r == 0 and c == 3:
                ax.legend(facecolor=PANEL, edgecolor=GRID, labelcolor=FG, fontsize=8, loc="upper right")
    save(fig, filename)


def rmsd():
    data = pd.read_csv(INPUTS / "rmsd_all.csv")
    data = data[data.reference == "open"]
    time_grid(data, ["rmsd_global_A", "rmsd_LID_A", "rmsd_NMP_A", "rmsd_CORE_A"],
              ["Backbone", "LID", "NMP", "Core"], "rmsd_grid.png",
              "Domain-specific deviation from the open reference", ["RMSD (Å)"] * 4)


def distances():
    data = pd.read_csv(ROOT / "data" / "domain_distances.csv")
    time_grid(data, ["LID_CORE_A", "NMP_CORE_A"], ["LID–core", "NMP–core"],
              "domain_distances_grid.png", "Domain-opening coordinates over 300 ns",
              ["Distance (Å)"] * 2, figsize=(17, 6.8))


def smooth_density(values, edges):
    counts, _ = np.histogram(values, bins=edges, density=True)
    xs = np.arange(-10, 11)
    kernel = np.exp(-0.5 * (xs / 2.0) ** 2)
    kernel /= kernel.sum()
    return np.convolve(counts, kernel, mode="same")


def angles():
    data = pd.read_csv(INPUTS / "domain_angle_all.csv")
    edges = np.linspace(45, 105, 181)
    centers = (edges[:-1] + edges[1:]) / 2
    fig, axes = canvas(2, 2, (13, 8), "Opening-angle distributions",
                       "NMP–core–LID angle · identical axes for all four water models", sharex=True, sharey=True)
    for ax, model in zip(axes.flat, MODELS):
        for start, color in (("CRYSTAL", CRYSTAL), ("PREDICTED", PREDICTED)):
            values = data.loc[(data.water_model == model) & (data.start_struct == start), "nmp_core_lid_angle_deg"]
            density = smooth_density(values, edges)
            ax.plot(centers, density, color=color, lw=2.0, label=start.title())
            ax.fill_between(centers, density, color=color, alpha=0.13)
        ax.set_title(label_model(model), weight="bold", fontsize=13)
        ax.set_xlim(45, 105)
        ax.set_ylim(bottom=0)
    axes[0, 0].legend(facecolor=PANEL, edgecolor=GRID, labelcolor=FG, fontsize=9)
    for ax in axes[-1]: ax.set_xlabel("NMP–core–LID angle (°)")
    for ax in axes[:, 0]: ax.set_ylabel("Density")
    save(fig, "angle_distributions.png")


def histogram_grid(data, xcol, ycol, xedges, yedges, title, subtitle, filename, xlabel, ylabel):
    hist = {}
    for start in STARTS:
        for model in MODELS:
            part = data[(data.water_model == model) & (data.start_struct == start)]
            counts, _, _ = np.histogram2d(part[xcol], part[ycol], bins=(xedges, yedges))
            hist[(start, model)] = counts
    vmax = max(x.max() for x in hist.values())
    fig, axes = canvas(2, 4, (16, 8.3), title, subtitle, sharex=True, sharey=True)
    for r, start in enumerate(STARTS):
        for c, model in enumerate(MODELS):
            ax = axes[r, c]
            ax.grid(False)
            mesh = ax.pcolormesh(xedges, yedges, np.ma.masked_less(hist[(start, model)].T, 1),
                                 cmap=DENSITY, norm=LogNorm(vmin=1, vmax=vmax), shading="flat")
            ax.set_title(label_model(model), weight="bold", fontsize=12)
            if c == 0: ax.set_ylabel(f"{start.title()} start\n{ylabel}", fontsize=10)
            if r == 1: ax.set_xlabel(xlabel, fontsize=10)
    fig.subplots_adjust(right=0.9)
    cbar = fig.colorbar(mesh, ax=axes, fraction=0.025, pad=0.016, shrink=0.75)
    cbar.set_label("Frames per bin · log scale", color=MUTED)
    cbar.ax.tick_params(colors=MUTED)
    fig.savefig(OUT / filename, dpi=170, facecolor=BG, bbox_inches="tight")
    plt.close(fig)
    print(filename)


def domain_landscapes():
    data = pd.read_csv(ROOT / "data" / "domain_distances.csv")
    histogram_grid(data, "LID_CORE_A", "NMP_CORE_A", np.linspace(24, 47, 117), np.linspace(22, 57, 141),
                   "Eight trajectories, eight sampled conformational spaces",
                   "Same axes and density scale across conditions · occupancy, not free energy",
                   "domain_landscapes.png", "LID–core distance (Å)", "NMP–core distance (Å)")


def grouped_bars(ax, data, value, title, ylabel=None):
    x = np.arange(4)
    for start, shift, color in (("CRYSTAL", -0.18, CRYSTAL), ("PREDICTED", 0.18, PREDICTED)):
        vals = [data.loc[(data.water_model == m) & (data.start_struct == start), value].iloc[0] for m in MODELS]
        ax.bar(x + shift, vals, width=0.34, color=color, label=start.title(), edgecolor="none")
    ax.set_xticks(x, [label_model(m) for m in MODELS])
    ax.set_title(title, fontsize=12, weight="bold")
    if ylabel: ax.set_ylabel(ylabel, fontsize=10)
    ax.set_ylim(bottom=0)


def bridges():
    data = pd.read_csv(ROOT / "tables" / "water_bridge_summary.csv")
    fig, axes = canvas(1, 3, (15, 5.2), "Water bridges between moving domains",
                       "Mean counts across each trajectory · descriptive values")
    for ax, col, title in zip(axes, ["LID_CORE_bridges_mean", "NMP_CORE_bridges_mean", "LID_NMP_bridges_mean"],
                              ["LID–core", "NMP–core", "LID–NMP"]):
        grouped_bars(ax, data, col, title, "Mean bridge count")
    axes[0].legend(facecolor=PANEL, edgecolor=GRID, labelcolor=FG, fontsize=9)
    save(fig, "water_bridge_summary.png")


def coupling():
    data = pd.read_csv(INPUTS / "lid_nmp_coupling_block_summary.csv")
    fig, axes = canvas(1, 1, (9, 5.6), "LID–NMP correlated motion",
                       "Mean absolute off-diagonal DCCM correlation · descriptive values")
    ax = axes
    grouped_bars(ax, data, "lid_nmp_mean_abs_corr", "Cross-domain coupling", "Mean |correlation|")
    ax.legend(facecolor=PANEL, edgecolor=GRID, labelcolor=FG, fontsize=9)
    save(fig, "lid_nmp_coupling.png")


def rmsf():
    data = pd.read_csv(INPUTS / "rmsf_all.csv")
    fig, axes = canvas(2, 4, (16, 7.5), "Residue-level flexibility",
                       "Cα RMSF across the eight conditions · same y-axis scale", sharex=True, sharey=True)
    for r, start in enumerate(STARTS):
        for c, model in enumerate(MODELS):
            ax = axes[r, c]
            part = data[(data.water_model == model) & (data.start_struct == start)].sort_values("resid")
            ax.plot(part.resid, part.rmsf_A, color=CRYSTAL if start == "CRYSTAL" else PREDICTED, lw=1.35)
            ax.set_title(label_model(model), fontsize=12, weight="bold")
            if c == 0: ax.set_ylabel(f"{start.title()} start\nCα RMSF (Å)", fontsize=10)
            if r == 1: ax.set_xlabel("Residue", fontsize=10)
    save(fig, "rmsf_grid.png")


def sasa():
    data = pd.read_csv(INPUTS / "sasa_timeseries_all.csv")
    time_grid(data, ["sasa_total_A2", "sasa_CORE_A2", "sasa_LID_A2", "sasa_NMP_A2"],
              ["Total", "Core", "LID", "NMP"], "sasa_grid.png",
              "Solvent-accessible surface area over time", ["SASA (Å²)"] * 4)


def pca():
    data = pd.read_csv(INPUTS / "pca_scores_all.csv", usecols=["water_model", "start_struct", "PC1", "PC2"])
    histogram_grid(data, "PC1", "PC2", np.linspace(-105, 75, 145), np.linspace(-75, 75, 121),
                   "Shared PCA projection: sampled occupancy",
                   "PC1 versus PC2 · same axes and density scale · not a free-energy estimate",
                   "pca_occupancy.png", "PC1", "PC2")


def dccm():
    fig, axes = canvas(2, 4, (16, 8.1), "Correlated Cα motion across eight trajectories",
                       "Dynamic cross-correlation matrix · same −1 to +1 scale", sharex=True, sharey=True)
    for r, start in enumerate(STARTS):
        for c, model in enumerate(MODELS):
            ax = axes[r, c]
            matrix = np.load(INPUTS / "dccm" / f"dccm_{model}_{start}.npy")
            ax.grid(False)
            image = ax.imshow(matrix, origin="lower", cmap=DIVERGING,
                              norm=TwoSlopeNorm(vmin=-1, vcenter=0, vmax=1), interpolation="nearest")
            ax.set_title(label_model(model), fontsize=12, weight="bold")
            if c == 0: ax.set_ylabel(f"{start.title()} start\nResidue index", fontsize=10)
            if r == 1: ax.set_xlabel("Residue index", fontsize=10)
    fig.subplots_adjust(right=0.9)
    cbar = fig.colorbar(image, ax=axes, fraction=0.025, pad=0.016, shrink=0.75)
    cbar.set_label("Correlation", color=MUTED)
    cbar.ax.tick_params(colors=MUTED)
    fig.savefig(OUT / "dccm_grid.png", dpi=170, facecolor=BG, bbox_inches="tight")
    plt.close(fig)
    print("dccm_grid.png")


def main():
    rmsd()
    distances()
    angles()
    domain_landscapes()
    bridges()
    coupling()
    rmsf()
    sasa()
    pca()
    dccm()


if __name__ == "__main__":
    main()
