"""Plot the eight 4AKE domain-distance distributions on identical axes.

Run from the repository root:
    python3 scripts/plot_domain_landscapes.py

Requires numpy, pandas and matplotlib. The input is the unmodified
03_distances/distances_all.csv from the original results archive.
"""

from pathlib import Path
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/4ake-matplotlib")

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "domain_distances.csv"
OUTPUT = ROOT / "figures" / "domain_landscapes.png"
MODELS = ("OPC", "SPCE", "TIP3P", "TIP4P")
STARTS = ("CRYSTAL", "PREDICTED")
X_EDGES = np.linspace(24, 47, 117)
Y_EDGES = np.linspace(22, 57, 141)


def main() -> None:
    data = pd.read_csv(INPUT)
    required = {"water_model", "start_struct", "LID_CORE_A", "NMP_CORE_A"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    outside = (
        (data.LID_CORE_A < X_EDGES[0])
        | (data.LID_CORE_A > X_EDGES[-1])
        | (data.NMP_CORE_A < Y_EDGES[0])
        | (data.NMP_CORE_A > Y_EDGES[-1])
    )
    if outside.any():
        raise ValueError(f"Plot limits exclude {int(outside.sum())} frames")

    histograms = {}
    for start in STARTS:
        for model in MODELS:
            group = data[(data.water_model == model) & (data.start_struct == start)]
            if group.empty:
                raise ValueError(f"No frames for {model} / {start}")
            counts, _, _ = np.histogram2d(
                group.LID_CORE_A, group.NMP_CORE_A, bins=(X_EDGES, Y_EDGES)
            )
            histograms[(start, model)] = counts

    vmax = max(int(counts.max()) for counts in histograms.values())
    fig, axes = plt.subplots(2, 4, figsize=(15.2, 8.2), sharex=True, sharey=True)
    fig.patch.set_facecolor("#f6f8fc")
    cmap = plt.colormaps["magma"].copy()
    cmap.set_bad("#e8edf5")

    for row, start in enumerate(STARTS):
        for col, model in enumerate(MODELS):
            ax = axes[row, col]
            ax.set_facecolor("#e8edf5")
            counts = histograms[(start, model)]
            image = ax.pcolormesh(
                X_EDGES,
                Y_EDGES,
                np.ma.masked_less(counts.T, 1),
                cmap=cmap,
                norm=LogNorm(vmin=1, vmax=vmax),
                shading="flat",
                rasterized=True,
            )
            ax.set_xlim(X_EDGES[0], X_EDGES[-1])
            ax.set_ylim(Y_EDGES[0], Y_EDGES[-1])
            ax.set_title(model.replace("SPCE", "SPC/E"), fontsize=15, weight="bold", color="#17253b", pad=12)
            ax.tick_params(labelsize=10, colors="#4f6078", length=0)
            for spine in ax.spines.values():
                spine.set_color("#c4cfdf")
            if col == 0:
                ax.set_ylabel(f"{start.title()} start\nNMP–core distance (Å)", fontsize=11, color="#243b5a", labelpad=12)
            if row == 1:
                ax.set_xlabel("LID–core distance (Å)", fontsize=11, color="#243b5a")

    fig.suptitle(
        "Eight trajectories, eight sampled conformational spaces",
        x=0.06, y=0.985, ha="left", fontsize=19, weight="bold", color="#14243a"
    )
    fig.text(
        0.06, 0.945,
        "Each panel uses the same distance ranges and density scale; color counts frames per 2D bin (log scale).",
        ha="left", fontsize=10.5, color="#50637d"
    )
    fig.subplots_adjust(left=0.08, right=0.9, top=0.88, bottom=0.11, wspace=0.12, hspace=0.24)
    cbar = fig.colorbar(image, ax=axes, location="right", fraction=0.025, pad=0.02, shrink=0.8)
    cbar.set_label("Frames per bin · log scale", fontsize=11, color="#243b5a")
    cbar.ax.tick_params(labelsize=10, colors="#4f6078")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=180, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    main()
