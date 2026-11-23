![Water model and starting-structure comparison banner](water_model.gif)

![](https://capsule-render.vercel.app/api?type=rect&height=4&color=0:000000,50:8b0000,100:000000)

<div align="center">
<h3>Water models × Starting Structures: A Protein-Motion Comparison</h3>

**A visual analysis of eight 300 ns molecular-dynamics trajectories of adenylate kinase (4AKE).** Four explicit-water models (OPC, SPC/E, TIP3P and TIP4P) were each run from a crystal-derived and a predicted starting structure. The [complete figure atlas](docs/FIGURE_ATLAS.md) covers all **86 historical figures** plus a new reproducible comparison plot.

</div>

> **Status:** Figure-led results story and complete visual archive. The figures describe these trajectories; they do not yet establish a general ranking of water models. Simulation input files, original analysis scripts and independent replicate information are not present in this folder.

The plots displayed below are dark renditions drawn from the archived numerical outputs. The original light-theme panels remain linked in the [figure atlas](docs/FIGURE_ATLAS.md).

**Explore:** [Domain motion](#the-solvent-and-starting-structure-jointly-shape-domain-opening) · [Conformational landscapes](#the-sampled-conformational-landscapes-differ) · [Hydration context](#hydration-and-correlated-motion) · [Full figure atlas](docs/FIGURE_ATLAS.md) · [Evidence and limits](docs/EVIDENCE_AND_LIMITS.md)


![](https://capsule-render.vercel.app/api?type=rect&height=4&color=0:000000,50:8b0000,100:000000)

<div align="center">
<h3> The Question</h3>

![4AKE in water: eight trajectories and mean NMP domain opening](assets/story-cover.svg)

Does changing the water model alter the domain motions sampled by 4AKE, and does that depend on whether the simulation starts from the crystal or predicted structure?

![](https://capsule-render.vercel.app/api?type=rect&height=4&color=0:000000,50:8b0000,100:000000)

### The Starting Structure Leaves a Time-Dependent Signature

[![Backbone and domain RMSD across eight conditions, dark theme](figures/dark/rmsd_grid.png)](figures/dark/rmsd_grid.png)

The predicted-start trajectories begin with larger deviations from the open reference in several conditions. The clearest early relaxation is in the NMP domain for OPC and SPC/E. The backbone and domain RMSD traces show why a single whole-trajectory average can hide this behavior.

**Figure 1.** Backbone, LID, NMP and core RMSD relative to the open reference. Columns are water models; red is crystal start and blue is predicted start. Summary: [`tables/rmsd_summary.csv`](tables/rmsd_summary.csv).

</div>

![](https://capsule-render.vercel.app/api?type=rect&height=4&color=0:000000,50:8b0000,100:000000)

<div align="center">
<h3>The Solvent and Starting Structure Jointly Shape Domain Opening</h3>
</div>

[![Domain distance traces, dark theme](figures/dark/domain_distances_grid.png)](figures/dark/domain_distances_grid.png)

[![Domain angle distributions, dark theme](figures/dark/angle_distributions.png)](figures/dark/angle_distributions.png)

LID–core and NMP–core distances do not shift in one uniform direction. For example, OPC crystal has a mean NMP–core distance of **44.09 Å** versus **41.73 Å** for OPC predicted; TIP3P reverses that ordering (**40.27 Å** crystal versus **44.36 Å** predicted). The angle distributions tell a similar condition-dependent story.

**Figures 2–3.** Domain distance time series and NMP–core–LID angle distributions. Values and labels: [`domain_distance_summary.csv`](tables/domain_distance_summary.csv), [`domain_angle_summary.csv`](tables/domain_angle_summary.csv). The separation of curves is descriptive evidence from individual trajectories, not a replicate-level uncertainty estimate.


![](https://capsule-render.vercel.app/api?type=rect&height=4&color=0:000000,50:8b0000,100:000000)

<div align="center">
<h3> The Sampled Conformational Landscapes Differ</h3>

[![Eight condition-matched domain-distance occupancy maps, dark theme](figures/dark/domain_landscapes.png)](figures/dark/domain_landscapes.png)
</div>

The LID/NMP distance maps put all eight trajectories on the same axes and density scale. The predicted-start runs with OPC, SPC/E and TIP4P visit an additional compact NMP region in these trajectories, while their crystal-start counterparts concentrate elsewhere. These maps count sampled frames; they are **not equilibrium free-energy landscapes**.

**Figure 4.** LID–core versus NMP–core distance occupancy, with identical axis limits, bins and color scale. Recreate this dark rendition with [`scripts/plot_readme_dark.py`](scripts/plot_readme_dark.py), the included [`data/domain_distances.csv`](data/domain_distances.csv), and [`requirements.txt`](requirements.txt). The maps remain sensitive to finite sampling and early relaxation.

An [exploratory Jensen–Shannon divergence heatmap](figures/fig11_jsd_heatmap.png) compares the same coordinates. Its uncertainty analysis needs review before treating model differences as robust. See the [evidence and limits guide](docs/EVIDENCE_AND_LIMITS.md).

![](https://capsule-render.vercel.app/api?type=rect&height=4&color=0:000000,50:8b0000,100:000000)

<div align="center">
<h3>Hydration and Correlated Motion</h3>
</div>

[![Inter-domain bridge water counts, dark theme](figures/dark/water_bridge_summary.png)](figures/dark/water_bridge_summary.png)

[![LID-NMP cross-domain correlation, dark theme](figures/dark/lid_nmp_coupling.png)](figures/dark/lid_nmp_coupling.png)

Water-bridge counts and domain-motion correlations vary by condition. They provide context for hypotheses about hydration and motion. Their association does not establish that individual waters drive particular conformational changes.

**Figures 5–6.** Mean bridge-water counts and off-diagonal LID/NMP dynamic cross-correlation. Summaries: [`water_bridge_summary.csv`](tables/water_bridge_summary.csv), [`dccm_network_summary.csv`](tables/dccm_network_summary.csv). Definitions and cutoffs must be recovered before manuscript use.

![](https://capsule-render.vercel.app/api?type=rect&height=4&color=0:000000,50:8b0000,100:000000)

<div align="center">
<h3>Explore the Other Analyses</h3>
</div>

The central story uses six figures for a readable path through the results. The full project also measured local flexibility, protein size and exposure, collective coordinates, and residue-level motion. These views provide useful context; the [complete atlas](docs/FIGURE_ATLAS.md) links and explains every historical figure.

| Local flexibility | Global exposure |
| --- | --- |
| [![RMSF across all conditions, dark theme](figures/dark/rmsf_grid.png)](figures/dark/rmsf_grid.png) <br> **RMSF:** where the chain is flexible. | [![SASA across all conditions, dark theme](figures/dark/sasa_grid.png)](figures/dark/sasa_grid.png) <br> **SASA and Rg:** how exposure and compactness change. |

| Collective coordinates | Correlated motion |
| --- | --- |
| [![PCA occupancy grid, dark theme](figures/dark/pca_occupancy.png)](figures/dark/pca_occupancy.png) <br> **PCA:** occupancy in the shared projection, without a free-energy claim. | [![DCCM grid, dark theme](figures/dark/dccm_grid.png)](figures/dark/dccm_grid.png) <br> **DCCM:** which residue motions are correlated. |

The atlas also covers hydration RDF and contact traces, residue hydration, JSD and convergence, tICA/MSM/TPT, hydrogen-bond lifetimes, water diffusion, and the original composite scorecard. It marks the last three analysis families where their current outputs fail basic interpretation checks.

![](https://capsule-render.vercel.app/api?type=rect&height=4&color=0:000000,50:8b0000,100:000000)

<div align="center">
<h3> What This Dataset Supports</h3>
</div>
The strongest defensible conclusion is that **the sampled 4AKE domain motions vary across combinations of water model and starting structure**. Differences are visible across distance traces, angle distributions and condition-matched occupancy maps. The available trajectories alone cannot separate a reproducible water-model effect from run-to-run variation or initial-condition memory.

![](https://capsule-render.vercel.app/api?type=rect&height=4&color=0:000000,50:8b0000,100:000000)

<div align="center">
<h3>Repository Map</h3>


[![Figure atlas](https://img.shields.io/badge/FIGURE_ATLAS-8b0000?style=for-the-badge)](docs/FIGURE_ATLAS.md) [![Evidence and limits](https://img.shields.io/badge/EVIDENCE_%26_LIMITS-5c0000?style=for-the-badge)](docs/EVIDENCE_AND_LIMITS.md) [![Preprint draft](https://img.shields.io/badge/PREPRINT_DRAFT-3a0000?style=for-the-badge)](docs/PREPRINT_DRAFT.md) [![Methods to recover](https://img.shields.io/badge/METHODS_TO_RECOVER-1a1a1a?style=for-the-badge)](docs/METHODS_TO_RECOVER.md)
</div>

- [`docs/FIGURE_ATLAS.md`](docs/FIGURE_ATLAS.md): guided index to all 86 original figures, grouped by scientific question and interpretation status.
- [`docs/EVIDENCE_AND_LIMITS.md`](docs/EVIDENCE_AND_LIMITS.md): claim-by-claim evidence and known analysis issues.
- [`docs/PREPRINT_DRAFT.md`](docs/PREPRINT_DRAFT.md): provisional title, abstract and manuscript outline.
- [`docs/METHODS_TO_RECOVER.md`](docs/METHODS_TO_RECOVER.md): exact information needed for a reproducible preprint.
- [`figures/`](figures/): all historical panels, plus the new matched-axis occupancy map.
- [`tables/`](tables/): all original compact summary tables; see the atlas before interpreting flagged outputs.
- [`data/domain_distances.csv`](data/domain_distances.csv) and [`scripts/plot_domain_landscapes.py`](scripts/plot_domain_landscapes.py): data and code for the featured occupancy map.
- [`scripts/plot_readme_dark.py`](scripts/plot_readme_dark.py) and [`data/readme_inputs/`](data/readme_inputs/): source results and plotting code for the dark README figures. The original light figures remain in the atlas.

![](https://capsule-render.vercel.app/api?type=rect&height=4&color=0:000000,50:8b0000,100:000000)

<div align="center">
<h3> Publication Status</h3>


The visual story stands on its own. If we later pursue a preprint, it should wait for the simulation protocol, predicted-structure provenance, trajectory/replicate accounting, and checks of statistical uncertainty and water-diffusion analysis. See the optional [preprint draft](docs/PREPRINT_DRAFT.md) and [methods checklist](docs/METHODS_TO_RECOVER.md).
</div>

![](https://capsule-render.vercel.app/api?type=rect&height=4&color=0:000000,50:8b0000,100:000000)

<div align="center">
  
<h3>Study Credits</h3>
<a href="https://github.com/Eswar-mse">Moparti Sri Venkata Satya Sai Eswar</a> · <a href="https://github.com/biomaverik">Debojyoti Chatterjee</a> · <a href="https://github.com/Vivin-francis">Vivin Francis</a>
</div>

