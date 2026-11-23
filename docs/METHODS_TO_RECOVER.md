# Methods and provenance needed for a preprint

The results folder does not contain simulation input files, trajectories, topology files, analysis scripts, or a methods record. Please recover the following from the original project or collaborator notes.

1. **Structure identity:** 4AKE chain, biological assembly, ligand/nucleotide state, missing residues and mutations; exact predicted structure file, accession, prediction method and date; alignment and residue mapping between starts.
2. **System preparation:** protonation, termini, cofactors/ions, protein force field, water-model variants and implementation, box size, salt concentration, system atom counts.
3. **Simulation protocol:** engine and version, minimization, equilibration, production length, temperature and pressure controls, timestep, constraints, cutoffs, long-range electrostatics, periodic-boundary treatment, output stride and random seeds.
4. **Sampling:** number of independently initialized replicates for each of the eight conditions, production periods excluded as equilibration, and whether any run was restarted or extended.
5. **Analysis definitions:** exact CORE/LID/NMP residue ranges; alignment for RMSD/RMSF/PCA/DCCM; domain distance and angle atom selections; hydration, water-bridge and hydrogen-bond cutoffs; PMF/JSD binning and smoothing.
6. **Uncertainty and validation:** replicate-level variation or justified time-block analysis, convergence tests, and any experimental structure or measurement used for comparison.
7. **Reproducibility and rights:** scripts/workflow, software versions, raw-data location, figure-generation commands, contributor list, funding, intended preprint server and license.

The available audit file (`00_audit/input_audit.csv`) records paths on the original machine and lists both topology and trajectory files as existing there at analysis time. It cannot verify that those files are available now.
