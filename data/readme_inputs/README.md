# Inputs for the dark README figures

These files are byte-for-byte copies of numerical outputs in the original results archive. [`plot_readme_dark.py`](../../scripts/plot_readme_dark.py) uses them, [`domain_distances.csv`](../domain_distances.csv), and two summary tables to redraw the README figures against a dark background.

| Here | Original results file | Figure family |
| --- | --- | --- |
| `rmsd_all.csv` | `01_rmsd/rmsd_all.csv` | Backbone and domain RMSD |
| `rmsf_all.csv` | `02_rmsf/rmsf_all.csv` | Residue RMSF |
| `sasa_timeseries_all.csv` | `08_sasa/sasa_timeseries_all.csv` | Total and domain SASA |
| `domain_angle_all.csv` | `21_domain_angle_kinetics/domain_angle_all.csv` | Opening-angle distributions |
| `pca_scores_all.csv` | `06_pca/pca_scores_all.csv` | Shared PCA occupancy |
| `lid_nmp_coupling_block_summary.csv` | `20_dccm_networks/lid_nmp_coupling_block_summary.csv` | LID/NMP correlation bars |
| `dccm/dccm_*.npy` | `07_dccm/dccm_*.npy` | Eight DCCM matrices |

The bridge-count plot uses [`tables/water_bridge_summary.csv`](../../tables/water_bridge_summary.csv). The distance plots use [`data/domain_distances.csv`](../domain_distances.csv).

These are analysis outputs, not raw trajectories. They reproduce the plotted values, but the original trajectory preparation and analysis code remain unavailable. The new PCA panel plots **occupancy** of PC1/PC2 bins; it does not claim to reproduce the historical free-energy color scale.
