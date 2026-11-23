# Evidence and limits

## Design visible in the results

The audit lists eight protein trajectories: OPC, SPC/E, TIP3P and TIP4P, each with CRYSTAL and PREDICTED starts. Each time series runs from 0 to 300 ns at 0.01 ns spacing (30,001 frames per condition). The source paths point to a different machine; trajectories and topology files are absent from this folder. The crystal input is identified by the project owner as PDB **4AKE**. The predicted input is not identified here.

## Recommended main figures

| Story step | Figure | What it shows | Interpretation limit |
| --- | --- | --- | --- |
| Early relaxation | `fig01e_rmsd_all_grid.png` | Domain-specific RMSD traces | Need fitting and reference definitions |
| Domain movement | `fig03d_domain_distances_grid.png` | LID/core and NMP/core time series | One trajectory may not be representative |
| Opening geometry | `fig25b_domain_angle_distributions.png` | Condition-dependent angle distributions | Angle atom selections need documentation |
| Conformational landscape | `domain_landscapes.png` | Occupied LID/NMP coordinate regions on matched axes | Counts frames; finite sampling and early relaxation matter |
| Exploratory distribution comparison | `fig11_jsd_heatmap.png` | Pairwise domain-coordinate JSD | Histogram/binning and frame dependence matter |
| Hydration context | `fig26d_bridge_summary_bar.png` | Inter-domain bridge-water counts | Bridge definition needs documentation |
| Motion coupling | `fig24c_lid_nmp_coupling_bar.png` | LID/NMP DCCM block averages | Correlation is not causal coupling |

## Numerical anchors

From `tables/domain_distance_summary.csv`: NMP–core means are 44.094 Å (OPC crystal), 41.725 Å (OPC predicted), 40.266 Å (TIP3P crystal), and 44.359 Å (TIP3P predicted). The ordering changes with model. From `tables/domain_angle_summary.csv`: means are 79.30° versus 76.62° for OPC and 74.87° versus 81.94° for TIP3P (crystal versus predicted). These are full-trajectory means and do not resolve equilibration or sampling uncertainty.

From `10_jsd_stats/bootstrap_jsd_crystal_vs_predicted.csv`, reported JSD means are 0.883 (OPC), 0.660 (SPC/E), 0.355 (TIP3P) and 0.879 (TIP4P). The bootstrap method is not documented. Treat their ranking as descriptive until recomputed using independent trajectories or a justified block-resampling scheme.

## Results to hold out of the main claim

- **Water diffusion:** `tables/water_diffusion_summary.csv` has negative diffusion coefficients for seven of eight conditions. Diffusion coefficients cannot be negative. The underlying MSD starts at hundreds of Å² at a 0.02 ns lag; coordinate wrapping/unwrapping and fit windows need auditing. Do not use `fig20_water_msd.png` or `fig21_water_diffusion_bar.png` as physical diffusion results.
- **Frame-level significance:** `tables/stats_summary.csv` reports 120,004 observations for each four-model comparison, apparently 30,001 frames × four conditions. Frames in an MD trajectory are correlated, so these p-values cannot stand in for independent simulation replicates. Do not claim statistical significance from them.
- **Mechanistic scorecard:** `fig20_mechanistic_scorecard.png` mixes descriptive metrics with the invalid diffusion estimates and subjective normalization/direction choices. Do not use its model ranking.
- **Hydrogen-bond lifetimes:** every row in `tables/hbond_lifetimes_summary.csv` reports 2.0 ns with 100% mean occupancy. This uniformity suggests a cap or definition issue and does not demonstrate model-dependent lifetimes.
- **MSM/TPT kinetics:** `12_msm_deeptime/msm_run_notes.txt` describes a four-macrostate model using a 0.1 ns lag and LID, NMP and radius of gyration features. CK errors in `17_msm_ck_tpt/ck_validation.csv` rise substantially across steps. Without a documented validation and replicate-aware design, do not make quantitative kinetic or transition-path claims from these outputs.

## Interpretation guardrails

This is one protein and a limited set of runs. The data reveal condition-specific behavior; they cannot distinguish water-model effects from initial-condition memory, stochastic trajectory variation, or setup differences without the complete methods and independent simulations. The label “predicted” should not be silently equated with a specific AlphaFold model until its file or accession is found.
