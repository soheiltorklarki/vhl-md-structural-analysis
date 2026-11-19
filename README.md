# Structural Bioinformatics & MD Analysis of the VHL Complex

Repository for Master's thesis research on the **von Hippel-Lindau (VHL)** complex (reference structure **PDB: 7Z76**), focusing on **GROMACS** molecular dynamics (MD) simulations, structural stability, and cancer-associated mutations.

## Research Overview
- **Target System:** pVHL–ElonginB–ElonginC complex (336 protein residues, explicit solvent with ~29,713 water molecules and 181 ions).
- **Simulation Protocol (GROMACS):**
  - **Force Field & Electrostatics:** PME for long-range electrostatics, Verlet cutoff scheme, LINCS constraints on H-bonds (`dt = 2 fs`).
  - **Equilibration & Production:** Energy minimization (`Fmax < 1000 kJ/mol/nm`), NVT (`300 K`, V-rescale), NPT (`1 bar`, C-rescale), and unrestrained production MD.
- **Downstream Analyses:** Trajectory PBC correction, backbone RMSD, per-residue RMSF, and structural mapping of hotspot cancer mutations (e.g., `N78D`, `H115N`) and VHL–HIF / Elongin B/C interfaces.

## Planned Repository Structure
- `mdp/`: GROMACS parameter files (`em.mdp`, `nvt.mdp`, `npt.mdp`, `md.mdp`).
- `scripts/`: Automation and analysis scripts (PBC handling, RMSD/RMSF parsing and plotting, mutation mapping).
- `analysis_notes/`: Summaries of equilibration metrics, stability checks, and structural observations.

## Current Status
- Completed energy minimization, NVT equilibration (~299.76 K), and NPT equilibration (~1010.19 kg/m³) on lab server **Ares**.
- Running initial 1 ns production MD benchmark/test on **Ares** prior to trajectory post-processing and extended/comparative runs.

## Links
- **ORCID:** https://orcid.org/0009-0004-6514-0597
- **LinkedIn:** https://www.linkedin.com/in/torklarki
- **Google Scholar:** https://scholar.google.com/citations?hl=en&user=3AAdx5kAAAAJ
