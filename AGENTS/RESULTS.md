# Provisional Working Model (RESULTS)

## 1. Metadata

- **Git Commit**: `22bf43d50a35b481747c659ac544ef4d37adec8e`
- **Worktree Status**: dirty. Manuscript-relevant modified files at refresh time: `main.tex`, `main.bib`, and `sm.tex`. Agent workflow/state files are also present as untracked files or modified working files: `.agents/`, `AGENTS.md`, and `AGENTS/`. Untracked build artifacts: `main.pdf` and `main.synctex.gz`.
- **Refresh Scope**: updated shared context to state that large-`k` mode attenuation is due to known imaging aberrations / MTF attenuation, not merely generic finite imaging resolution. No LaTeX build or figure regeneration was run.

**Working-Memory Rule**: This file is an extracted working model of the manuscript and related discussion. It may be stale, incomplete, or wrong. It coordinates agents but does not override the manuscript.

## 2. Literature & Domain Context

### State of the Field

The manuscript is positioned in the problem of how isolated many-body systems relax after being prepared far from equilibrium. The broad theoretical context is that equilibrium statistical mechanics and the eigenstate thermalization hypothesis can explain eventual thermal behavior in many complex quantum systems, but the route to equilibrium often contains long-lived intermediate states.

The paper uses "prethermalization" in the standard sense: a rapid initial relaxation or dephasing process establishes a quasisteady configuration, while true global thermal equilibrium is delayed by slower inelastic or mode-coupling processes. The introduction contrasts this with both near-integrable ultracold-gas experiments and the classical Fermi-Pasta-Ulam-Tsingou problem, where weak nonlinear coupling between modes can delay equipartition.

The distinctive setting here is a quenched immiscible binary Bose-Einstein condensate whose separated phases create a one-dimensional interface embedded in a two-dimensional bulk. The interface supports ripplons, while the condensate bulk acts as a weakly coupled thermal reservoir. The central scientific opportunity is that the interface is neither simply an isolated near-integrable gas nor an ordinary interface in contact with an uncontrolled bath: the authors can measure interface fluctuations mode by mode and independently infer the bulk temperature.

### Prior Art Mapping

- `DAlessio2016`: review background for ETH, quantum chaos, and thermalization; supports the broad statistical-mechanics frame and the conclusion's ETH language.
- `Mori2018`, `Langen2016`: review/theory background for prethermalization in isolated quantum systems and near-integrable dynamics.
- `Kinoshita2006`, `Gring2012`, `Langen2015`, `Tang2018`, `Neyenhuis2017`: primary experimental ultracold-atom or trapped-ion examples establishing prethermal or anomalously slow thermalization through integrable or near-integrable structure. `Langen2015` is the primary GGE observation and is preferred over using `Langen2016` as the main support for that claim. `Neyenhuis2017` should not be framed as a clean non-GGE counterexample; it can be bundled with GGE or GGE-like cases because the spin-chain dynamics map to a near-integrable model.
- `RubioAbadal2020`: primary cold-atom Floquet prethermalization example in a driven Bose-Hubbard system. It is useful as a distinct mechanism in which high-frequency driving suppresses heating, contrasting with the present undriven post-quench ripplon system.
- `Berges2004`, `Kofman1994`: origins of prethermalization language in high-energy/cosmological settings.
- `Barnett2011`, `Gong2013`, `Yin2023`, `Williamson2016`, `Kroker2021`: support for broader mechanisms where slow and fast relaxation channels coexist.
- `Fermi1955`, `Onorato2015`: FPUT analogy and kinematic/scattering constraints as a route to slow thermalization.
- `Lamporesi2023`, `Huh2024`: binary/spinor condensate and quench/coarsening context.
- `Takeuc2013`, `Kobyakov2011`, `VanScha2008`, `GengTao2025`: theory and prior work on binary-condensate interfaces, ripplons, capillary dynamics, and interfacial tension.
- `Flekko1995`, `Aarts2004`: capillary-wave/interface fluctuation theory used to connect `C(k)` to temperature through the quadratic interface Hamiltonian.
- `Beliaev1957`, `Dereziski2024`, `Zhang2021`: Beliaev/inverse-Beliaev damping and quasiparticle decay framework used to motivate the on-shell scattering argument.
- `Giorgini1997`, `Fang2016`, `Ville2018`, `Pitaevskii2016`: thermometry and Bose-gas theory supporting the minority-thermal-atom temperature extraction and Bogoliubov treatment.
- `Segal2010`, `Dubessy2014`, `Galka2022`: principal component analysis as a way to extract collective modes from fluctuating ultracold-gas data.
- `Hung2011`, `Altunta2021`, `ImagingFootnote`: imaging-aberration and modulation-transfer-function attenuation context for large-`k` modes.

## 3. Paper Summary

The paper reports an experiment on prethermal ripplons in a quenched immiscible binary sodium Bose-Einstein condensate. A microwave quench prepares a spin mixture in which coherent/near-deterministic initial spin structure and amplified fluctuations seed droplet patterns; these droplets coalesce, coarsen, and then phase separate into two domains with a one-dimensional interface. The interface height profile is measured in situ over many experimental realizations.

The authors identify ripplon-like standing-wave modes of the interface, measure their Fourier-space fluctuations `C(k)`, compare those fluctuations to thermal capillary-wave predictions, and infer a mode-dependent effective temperature. The main result is that high-momentum ripplons thermalize with the independently measured bulk condensate temperature, while low-momentum ripplons remain overpopulated and hot for seconds. The proposed microscopic origin is kinematic isolation: low-`k` ripplons cannot efficiently decay into the phonon bath through on-shell energy- and momentum-conserving three-field processes.

The paper also introduces a thermometry method for extremely low-temperature binary condensates: the density of minority thermal atoms in the opposite-spin condensate region can be measured directly, avoiding subtraction of a large same-spin condensate background.

## 4. Core Scientific Claims

1. A quenched immiscible binary sodium condensate forms a stable one-dimensional interface after fast spin-domain coarsening seeded by both coherent initial structure and amplified fluctuations, and the interface supports ripplon modes measurable through height fluctuations.
2. PCA of repeated interface profiles recovers spatial components consistent with sinusoidal standing ripplon modes under the box boundary condition; DCT analysis maps these components to increasing spatial frequency.
3. The equilibrium capillary-wave prediction `C(k) = k_B T / [sigma (k^2 + xi^{-2})]` describes high-`k` interface fluctuations when evaluated at the independently measured bulk temperature, but low-`k` modes show excess occupation.
4. Individual ripplon-mode amplitude distributions are consistent with normal distributions up to the measured moment order, allowing an effective temperature to be assigned to each mode even when the full `k` distribution is nonthermal.
5. Low-`k` ripplon temperatures remain elevated relative to the bulk, follow an approximate low-`k` power law `T_k ~ k^{-1.38(8)}`, and decay on a measured `5(1) s` timescale, much slower than the stated `~0.1 s` bulk equilibration timescale.
6. The proposed explanation is mode-selective kinematic isolation: at low `k`, the ripplon dispersion and phonon dispersion do not permit on-shell phonon-producing three-field scattering within the empirical linewidth; high-`k` ripplons have available channels and thermalize with the bulk.
7. Minority thermal atoms in the opposite-spin condensate region provide an in situ bulk thermometer. The Hartree-Fock effective-potential model, with quantized transverse `z` levels, fits measured minority density profiles and yields `T_bulk`.
8. Agreement between `T_bulk` and the temperature inferred from high-`k` ripplon tails supports the interpretation that the high-momentum ripplons are equilibrated with the condensate bulk.

## 5. Open Questions & Weaknesses

- The microscopic thermalization mechanism is currently qualitative. The dispersion/on-shell argument explains why low-`k` decay is suppressed, but the draft does not yet compute scattering rates or quantitatively predict the observed `5(1) s` decay.
- The comparison between the low-`k` decay time and the `~0.1 s` bulk equilibration time is central to the prethermal claim; the source and measurement basis for the bulk timescale should be explicit enough that a referee cannot read it as asserted.
- The conclusion's statement that the normal mode distributions hint that ETH "partially" applies is provocative and may be too strong unless framed carefully. The data show Gaussian single-mode amplitudes and mode-dependent effective temperatures; the connection to ETH is interpretive.
- The linewidth estimate used to exclude on-shell scattering is empirical and appears in a footnote. Because it is a central part of the kinematic-isolation argument, the manuscript should make clear how robust the conclusion is to this linewidth estimate.
- The thermometry argument depends on the assumptions that thermal-thermal interactions are negligible and that `V_eff` varies slowly in `e_y`; the paper notes the edge failure mode but should keep the valid fitting region visually and textually clear.
- Some existing prose/editing issues remain visible in the current draft, including abstract edit macros, commented author notes, and typos such as "eliminats", "commom", "emperically", "equillibrium", and "dominate".
- For the introduction's novelty paragraph, do not use `Eigen2018` as a primary contrast for long-lived cold-atom prethermalization unless the text explicitly discusses universal unitary-gas dynamics. That work is better framed as a short-time universal-dynamics/quench-to-unitarity result in which three-body recombination causes particle loss and heating, rather than as a close analogue of this paper's long-lived, mode-selective ripplon prethermalization.

## 6. Target Venue

- **Journal/Audience**: Physical Review Letters style, based on the `revtex4-1` `prl` two-column document class and the compact four-main-figure narrative.
- **Audience**: AMO/quantum-gas and nonequilibrium many-body physicists; likely readers know BECs and thermalization at a high level but may not know binary-condensate interface thermometry.
- **Constraints**: Letter-style main text with compressed narrative. The core story must be understandable from the four main figures, with technical derivations and thermometry details carried by the appendix/supplement.

## 7. Structural Outline / Figure Mapping

- **Abstract**: Claims the observation of a long-lived prethermal ripplon configuration after a quench, with high-`k` modes equilibrated to the bulk and low-`k` modes remaining hot because of kinematic isolation.
- **Introduction**: Establishes the thermalization/prethermalization problem, the FPUT analogy, and why this binary-condensate interface is a new setting with both an interface subsystem and a thermal bath.
- **Figure 1 / Experimental Setup and Pathway**: Shows the quench, the coherent/near-deterministic early spin structure and amplified fluctuations that seed droplet formation, subsequent coarsening, the separated interface, and the schematic mode-population relaxation pathway.
- **Experiment Description**: Defines the sodium spin states, quasi-2D box, microwave quench, magnetic-gradient stabilization, hold time, imaging, and interface-height extraction.
- **Figure 2 / Mode Identification and `C(k)`**: Supports the identification of measured interface fluctuations as ripplons and shows the key nonequilibrium signature: low-`k` excess population with high-`k` thermal tails.
- **Capillary-Wave Model**: Provides the phenomenological equilibrium relation between `C(k)` and temperature using interface tension and capillary length.
- **Figure 3 / Mode Temperatures and Mechanism**: Shows Gaussian mode-amplitude distributions, mode-dependent temperatures, long-lived low-`k` excess, and the dispersion/scattering-channel picture for kinematic isolation.
- **Figure 4 / Thermometry**: Establishes the independent bulk thermometer using minority thermal atoms and validates the high-`k` ripplon temperature against `T_bulk`.
- **Conclusion**: Restates the prethermal interface result, proposes kinematic isolation as the origin, and identifies quantitative energy-exchange theory and higher-temperature decay mechanisms as future work.
- **Appendix / SM**: Supplies the Bogoliubov ripplon theory, quantum-vs-classical `C(k)` comparison, quantum harmonic-oscillator distribution for `h_k`, and quasi-2D thermometry calculation.
