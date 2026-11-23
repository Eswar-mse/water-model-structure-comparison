# Provisional preprint draft

**Working title:** Water model and starting structure jointly shape adenylate kinase domain dynamics in molecular-dynamics simulations

**Status:** Narrative scaffold. Not submission-ready until the methods and validation items in [`METHODS_TO_RECOVER.md`](METHODS_TO_RECOVER.md) are resolved.

## Abstract (draft)

Molecular-dynamics simulations are sensitive to both solvent representation and the structure used to start a trajectory. We examined eight 300 ns trajectories of adenylate kinase, crossing four explicit-water models (OPC, SPC/E, TIP3P and TIP4P) with crystal-derived (PDB 4AKE) and predicted starting structures. Domain-resolved RMSD, LID–core and NMP–core distances, opening angles and two-dimensional conformational maps show that the sampled motions differ across conditions. The direction of the crystal-versus-predicted shift depends on water model: mean NMP–core distance is higher for crystal than predicted starts with OPC (44.09 versus 41.73 Å), whereas the ordering is reversed with TIP3P (40.27 versus 44.36 Å). Water-bridge counts and domain-motion correlations also vary, suggesting testable links between hydration and conformational sampling. Together, the observations show condition-dependent variation in sampled domain motion. Independent-replicate uncertainty, simulation provenance and the predicted structure identity remain to be established before generalizing or assigning mechanism.

## Proposed figure sequence

1. **Design and initial relaxation:** schematic of the 4 × 2 design (to create after provenance is known); current `fig01e_rmsd_all_grid.png`.
2. **Domain motion:** `fig03d_domain_distances_grid.png` and `fig25b_domain_angle_distributions.png`.
3. **Conformational distributions:** `domain_landscapes.png`, a reproducible occupancy map on matched axes. Use `fig11_jsd_heatmap.png` only after its binning and uncertainty are checked.
4. **Hydration and coupling:** `fig26d_bridge_summary_bar.png` and `fig24c_lid_nmp_coupling_bar.png`, framed as associations.
5. **Supplement:** RMSF, radius of gyration, SASA, PCA and additional hydration plots after methods review.

## Results narrative to develop

**Starting structure affects early dynamics.** Describe the domain-specific relaxation visible in RMSD and distance time series. Quantify the first and last 100 ns separately and report whether shifts persist after an equilibration cutoff.

**Water-model effects depend on starting structure.** Report distance and angle distributions for each of the eight conditions; avoid a single overall water-model ranking. Use replicate-level estimates if independent runs exist.

**Conformational ensembles differ.** Compare domain-coordinate occupancy maps using consistent support, bins and convergence checks. Recompute JSD uncertainty with a method that respects temporal correlation. Do not call frame-count maps equilibrium free-energy landscapes.

**Hydration correlates with the observed motions.** Define bridge waters explicitly and test whether bridge changes precede, follow or merely accompany domain motion. Keep causal language out unless supported by further analysis.

## Discussion points

The results suggest that a water model can change how a protein explores conformations from a particular start, but the effect is not uniform across starting structures. Interpret this in the context of finite simulation time, possible memory of the initial conformation, force-field coupling and the limits of a single protein. Discuss any discrepancy with experiment only after the experimental comparator is specified.

## Required before submission

Complete Methods; verify predicted structure; establish replicates and uncertainty; audit diffusion and lifetime outputs; rerun or document figure generation; confirm all authors and data/code availability. The present figures can support a preprint once these issues are resolved, but the current folder alone cannot support a reproducible Methods section.
