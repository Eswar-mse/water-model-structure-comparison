# Complete figure atlas

The original results folder contains **86 figures**. This page places every figure in the scientific argument. The [README](../README.md) presents the shorter story; this atlas preserves the full exploratory record. The original figure numbering is retained, including reused numbers and letter suffixes.

The README displays [dark renditions](../figures/dark/) of its featured analyses to match the project banner. The historical figures linked below remain unaltered. The dark plots and their [source outputs](../data/readme_inputs/) can be regenerated with [`plot_readme_dark.py`](../scripts/plot_readme_dark.py).

**Reading labels:** **Core** = directly supports the main descriptive story; **Context** = adds a complementary readout; **Exploratory** = method or uncertainty needs review; **Hold** = a visible analysis issue prevents a physical or statistical claim. These labels describe the present evidence, not the effort behind the analysis.

## 1 · What moves, and when? — Core

**RMSD, RMSF, domain distances and opening angle** establish the structural response. They should be read together: RMSD shows departure from the open reference, RMSF localizes mobility, and distances/angles describe the domain geometry without reducing it to a single global number.

| Analysis | Figures | What to look for |
| --- | --- | --- |
| Backbone and domain RMSD | [Backbone](../figures/fig01a_rmsd_backbone.png) · [LID](../figures/fig01b_rmsd_lid.png) · [NMP](../figures/fig01c_rmsd_nmp.png) · [Core](../figures/fig01d_rmsd_core.png) · [Eight-condition grid](../figures/fig01e_rmsd_all_grid.png) | Early relaxation is domain-specific, especially NMP for predicted OPC and SPC/E. The core generally moves less than the mobile domains. |
| Residue fluctuation (RMSF) | [Crystal by water](../figures/fig02a_rmsf_crystal_by_water.png) · [Predicted by water](../figures/fig02b_rmsf_predicted_by_water.png) · [All conditions](../figures/fig02c_rmsf_all_grid.png) · [OPC pair](../figures/fig02d_rmsf_OPC_crystal_vs_predicted.png) · [SPC/E pair](../figures/fig02e_rmsf_SPCE_crystal_vs_predicted.png) · [TIP3P pair](../figures/fig02f_rmsf_TIP3P_crystal_vs_predicted.png) · [TIP4P pair](../figures/fig02g_rmsf_TIP4P_crystal_vs_predicted.png) | Peaks are concentrated in mobile regions. Predicted starts have larger mean LID/NMP RMSF than crystal starts for OPC and SPC/E in the summary table. |
| Domain distances | [LID–core time series](../figures/fig03a_lid_core_timeseries.png) · [NMP–core time series](../figures/fig03b_nmp_core_timeseries.png) · [Joint scatter](../figures/fig03c_lid_nmp_scatter.png) · [Eight-condition grid](../figures/fig03d_domain_distances_grid.png) | The ordering of crystal and predicted NMP–core distances changes by water model. These coordinates anchor the central comparison. |
| Opening-angle geometry | [Time series](../figures/fig25a_domain_angle_timeseries.png) · [Distributions](../figures/fig25b_domain_angle_distributions.png) · [Box plot](../figures/fig25c_domain_angle_boxplot.png) | The angle offers an independent geometric view of the condition-dependent shifts. The angle's atom selections still need documentation. |

The [replotted occupancy map](../figures/domain_landscapes.png) combines the two distances on common axes. Its [source CSV](../data/domain_distances.csv) and [plot script](../scripts/plot_domain_landscapes.py) are included. Full-trajectory means, RMSF and distribution shapes are descriptive because independent replicate information is missing.

## 2 · How compact and exposed are the structures? — Context

**Radius of gyration (Rg) and solvent-accessible surface area (SASA)** check whether domain changes coincide with whole-protein compaction or surface exposure. They add context but do not directly measure hydration structure.

| Analysis | Figures | Reading |
| --- | --- | --- |
| Radius of gyration | [Time series](../figures/fig05a_rg_timeseries.png) · [Box plot](../figures/fig05b_rg_boxplot.png) | Rg varies modestly and changes direction across conditions: OPC predicted is lower than OPC crystal, whereas TIP4P predicted is higher than TIP4P crystal. |
| SASA | [Total](../figures/fig08a_sasa_total.png) · [Core](../figures/fig08b_sasa_core.png) · [LID](../figures/fig08c_sasa_lid.png) · [NMP](../figures/fig08d_sasa_nmp.png) · [Grid](../figures/fig08e_sasa_grid.png) | Total and domain SASA show condition-specific exposure. Domain breakdown is more informative than the total alone. |

Summary values are in [`rg_summary.csv`](../tables/rg_summary.csv) and [`sasa_summary.csv`](../tables/sasa_summary.csv). No universal compactness ordering emerges from these eight trajectories.

## 3 · Which conformations are sampled? — Core and exploratory

The [matched-axis occupancy map](../figures/domain_landscapes.png) is the main view because it shows the observed domain-coordinate distributions directly. The historical **PMF and PCA landscape figures** provide additional views, but free-energy interpretation needs documented binning, equilibration and convergence.

| Analysis | Figures | Reading |
| --- | --- | --- |
| Historical 2D PMF | [Crystal](../figures/fig04a_pmf_crystal.png) · [Predicted](../figures/fig04b_pmf_predicted.png) · [Grid](../figures/fig04c_pmf_all_grid.png) | **Exploratory.** The original maps have large empty ranges and an unexplained reference marker. Their free-energy calculation needs review. |
| Shared PCA projection | [Crystal/predicted overlay](../figures/fig06a_pca_overlay.png) · [Time colored](../figures/fig06b_pca_timecolored.png) · [PC time series](../figures/fig06c_pc_timeseries.png) | **Context.** PCA offers a second view of how the conformational clouds overlap and evolve over time. PC1 and PC2 account for about 41% and 22% of reported variance, respectively. |
| PCA-derived FEL | [OPC crystal](../figures/fig06d_fel_opc_crystal.png) · [OPC predicted](../figures/fig06d_fel_opc_predicted.png) · [SPC/E crystal](../figures/fig06d_fel_spce_crystal.png) · [SPC/E predicted](../figures/fig06d_fel_spce_predicted.png) · [TIP3P crystal](../figures/fig06d_fel_tip3p_crystal.png) · [TIP3P predicted](../figures/fig06d_fel_tip3p_predicted.png) · [TIP4P crystal](../figures/fig06d_fel_tip4p_crystal.png) · [TIP4P predicted](../figures/fig06d_fel_tip4p_predicted.png) · [Grid](../figures/fig06e_fel_grid.png) | **Exploratory.** Shapes differ, but the thermodynamic meaning of the color scale requires convergence and method checks. |
| tICA and VAMP2 | [tICA projection](../figures/fig15a_tica_projection.png) · [tICA time series](../figures/fig15b_tica_time_series.png) · [VAMP2 scores](../figures/fig15c_vamp2_scores.png) | **Exploratory.** tICA is a kinetic projection. The VAMP2 score panel appears blank, so it currently supplies no interpretable comparison. |

The historical maps remain in the repository as analysis outputs; the README makes its landscape claim from the directly reproducible occupancy plot.

## 4 · Do residues move together? — Context and exploratory

**Dynamic cross-correlation matrices (DCCM)** and their network summaries show correlated motion patterns. Such correlations can guide hypotheses about inter-domain coupling, but they do not establish signal transmission or a hydration mechanism.

| Analysis | Figures | Reading |
| --- | --- | --- |
| Eight DCCMs | [OPC crystal](../figures/fig07_dccm_opc_crystal.png) · [OPC predicted](../figures/fig07_dccm_opc_predicted.png) · [SPC/E crystal](../figures/fig07_dccm_spce_crystal.png) · [SPC/E predicted](../figures/fig07_dccm_spce_predicted.png) · [TIP3P crystal](../figures/fig07_dccm_tip3p_crystal.png) · [TIP3P predicted](../figures/fig07_dccm_tip3p_predicted.png) · [TIP4P crystal](../figures/fig07_dccm_tip4p_crystal.png) · [TIP4P predicted](../figures/fig07_dccm_tip4p_predicted.png) · [Grid](../figures/fig07i_dccm_grid.png) | **Context.** Inspect changes in the off-diagonal blocks; the shared color scale helps compare conditions. |
| DCCM-derived summaries | [Residue network strength](../figures/fig24a_dccm_network_strength.png) · [Coupling by structure](../figures/fig24b_dccm_coupling_by_struct.png) · [LID/NMP coupling](../figures/fig24c_lid_nmp_coupling_bar.png) · [OPC–TIP3P difference](../figures/fig24d_dccm_difference_opc_tip3p.png) | **Context.** The LID/NMP block average differs among conditions; definitions and time-window sensitivity need review. |
| Putative allosteric paths | [Path length](../figures/fig16_allosteric_path_length.png) · [Path residues](../figures/fig17_allosteric_path_residues_grid.png) | **Exploratory.** Graph paths depend on correlation thresholds and edge definitions; do not equate them with experimentally established communication routes. |

## 5 · What does the hydration analysis add? — Context and exploratory

**Water contacts and bridges** connect the solvent question back to domain geometry. They are association measures: a bridge count can change because domains move closer, because water organization changes, or both.

| Analysis | Figures | Reading |
| --- | --- | --- |
| Protein–water shell | [Hydration RDF](../figures/fig09_hydration_rdf.png) · [First-shell contacts](../figures/fig10_hydration_contacts.png) | **Exploratory.** Contact traces show changes over time. The plotted “RDF” rises monotonically and resembles a cumulative count, so its definition needs checking before calling it a conventional radial distribution function. |
| Residue hydration | [Crystal residue profile](../figures/fig23a_residue_hydration_crystal.png) · [Eight-condition grid](../figures/fig23b_residue_hydration_grid.png) · [Domain means](../figures/fig23c_residue_hydration_domain_bar.png) · [Predicted residue profile](../figures/fig23d_residue_hydration_predicted.png) | **Context.** Position-specific low-contact residues are clearer than domain averages, which are similar across models. |
| Inter-domain bridge waters | [LID–core trace](../figures/fig26a_bridge_lid_core.png) · [NMP–core trace](../figures/fig26b_bridge_nmp_core.png) · [LID–NMP trace](../figures/fig26c_bridge_lid_nmp.png) · [Summary](../figures/fig26d_bridge_summary_bar.png) | **Context.** Bridge counts differ by condition; LID–NMP bridges are sparse in most crystal-start trajectories. The 3.5 Å cutoff appears in the CSV, but the full bridge definition is missing. |

Summary tables: [`residue_hydration_domain_summary.csv`](../tables/residue_hydration_domain_summary.csv), [`water_bridge_summary.csv`](../tables/water_bridge_summary.csv).

## 6 · Are the differences robust? — Exploratory

**Jensen–Shannon divergence, block summaries and effect sizes** quantify differences between the existing trajectories. Their displayed error bars and significance cannot stand in for independent-replicate uncertainty without an analysis that respects temporal correlation.

| Analysis | Figures | Reading |
| --- | --- | --- |
| Pairwise ensemble divergence | [JSD heatmap](../figures/fig11_jsd_heatmap.png) · [Bootstrap comparison](../figures/fig12_jsd_bootstrap_bar.png) | The reported crystal/predicted divergence is lowest for TIP3P in this dataset. Bootstrap resampling method and binning are not documented. |
| Time-block summaries | [100 ns block convergence](../figures/fig13_block_convergence.png) | Some trajectories shift between blocks, especially early predicted-start runs. Three blocks within one trajectory are not independent replicates. |
| Standardized effects | [Cohen's d heatmap](../figures/fig22_effect_sizes_heatmap.png) | A descriptive summary of mean differences. The accompanying frame-level p-values treat correlated frames as observations, so do not claim statistical significance from them. |

See [`EVIDENCE_AND_LIMITS.md`](EVIDENCE_AND_LIMITS.md) for the underlying numerical caveats.

## 7 · Kinetic and transition analyses — Exploratory / hold

The **MSM, tICA, committor and transition-path figures** are part of the historical analysis. They require model validation and a documented feature/lag/state design before kinetic conclusions are made. The Chapman–Kolmogorov (CK) error table rises across steps; the plotted CK panel should be read alongside those errors.

| Analysis | Figures | Status |
| --- | --- | --- |
| Deeptime MSM | [Feature space](../figures/fig14a_msm_feature_space.png) · [Implied timescales](../figures/fig14b_msm_implied_timescales.png) · [Macrostate populations](../figures/fig14c_msm_macro_populations.png) · [Transition matrices](../figures/fig14d_msm_macro_transitions.png) | **Exploratory.** The notes describe 200 microstates, 4 macrostates and a 0.1 ns chosen lag; validation and start-structure pooling need review. |
| CK, committor and TPT | [CK panel](../figures/fig16_ck_validation.png) · [Committor](../figures/fig17_committor.png) · [TPT net flux](../figures/fig18_tpt_net_flux.png) · [Open/closed balance](../figures/fig19_open_close_balance.png) | **Hold for quantitative kinetics.** State definitions and CK validation are incomplete. |

## 8 · Water kinetics and composite ranking — Hold

These figures are preserved for transparency. Their visible or numerical issues are strong enough that they should not be used to compare physical water models in the README.

| Analysis | Figures | Why held |
| --- | --- | --- |
| Hydrogen-bond persistence | [Autocorrelation](../figures/fig18_hbond_autocorr.png) · [Lifetime bars](../figures/fig19_hbond_lifetime_bar.png) | All lifetime rows are exactly 2.0 ns with 100% occupancy. The autocorrelation curves are nearly flat. The measurement or truncation needs checking. |
| Water diffusion | [MSD curves](../figures/fig20_water_msd.png) · [Diffusion bars](../figures/fig21_water_diffusion_bar.png) | Seven of eight fitted diffusion coefficients are negative, which is physically invalid. Coordinate unwrapping and fit windows need reanalysis. |
| Composite score | [Mechanistic scorecard](../figures/fig20_mechanistic_scorecard.png) | Mixes the invalid diffusion estimates with subjective score directions and scaling. Its overall model ranking is unsupported. |

## What the full collection means

The many complementary structural analyses support a **condition-specific descriptive result**: the eight trajectories sample different 4AKE motions and conformations, with notable dependence on both water model and starting structure. Hydration and correlation analyses provide hypotheses about why. The present archive does not establish reproducible model rankings, causal water-mediated allostery or validated kinetics. Keeping every figure visible makes the scope and the limits of the project reviewable.
