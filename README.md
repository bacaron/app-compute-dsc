<h1 align="center">DSC evaluation (wmc - wmc) - Seperate tractograms</h1>

<p align="center">
  Measures the overlap between estimated and ground-truth white matter bundles, given as WMC classifications of two separate tractograms, with the Dice similarity coefficient, Jaccard index and sensitivity.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.729"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.729-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Measures the overlap between estimated and ground-truth white matter bundles, given as WMC classifications of two separate tractograms, with the Dice similarity coefficient, Jaccard index and sensitivity.**

Converts both tractograms to .trk using the T1, extracts the bundles listed in tractID_list from each WMC classification, voxelizes them and computes DSC, weighted DSC, Jaccard, sensitivity, TP, FP and FN per bundle. Use it to evaluate a bundle segmentation against a reference segmentation of the same subject made on a different tractogram. All inputs must belong to the same subject.

| | |
|---|---|
| **Inputs** | `neuro/track/tck` ×2 · `neuro/wmc` ×2 · `neuro/anat/t1w` |
| **Outputs** | `neuro/tractmeasures` |
| **Container** | `brainlife/dipy:0.16.0` |
| **Resources** | 4 CPUs · 1 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.729](https://doi.org/10.25663/brainlife.app.729) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `0` | `neuro/track/tck` | yes | Tractogram associated with the white matter classification (WMC) structure |
| `1` | `neuro/wmc` | yes | Ground truth bundles in form of white matter classification (WMC) structure |
| `2` | `neuro/track/tck` | yes | Tractogram associated with the white matter classification (WMC) structure |
| `3` | `neuro/wmc` | yes | Estimated bundles in form of white matter classification (WMC) structure |
| `4` | `neuro/anat/t1w` (acpc_aligned) | yes | ACPC-aligned T1 of the subject, used as reference to convert the tractograms from .tck to .trk. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `csv` | `neuro/tractmeasures` | CSV containing the following scalars: DSC, wDSC, Jaccard, sensitivity, TP, FP, FN |

<details>
<summary><b>Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `tractID_list` | string |  | ID list of the bundles of interest, separated by commas |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.729](https://doi.org/10.25663/brainlife.app.729), choose `neuro/track/tck`, `neuro/wmc`, `neuro/track/tck`, `neuro/wmc`, `neuro/anat/t1w` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/tractmeasures`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/dipy:0.16.0`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "tractogram_true": "/path/to/0/tractogram_true",
       "seg_true": "/path/to/1/seg_true",
       "tractogram_est": "/path/to/2/tractogram_est",
       "seg_est": "/path/to/3/seg_est",
       "t1": "/path/to/4/t1",
       "tractID_list": ""
   }
   ```

3. Run `./main`.

## Troubleshooting

- **Error: estimated segmentation and ground truth segmentation are the same. DSC will be 1.**: Select different estimated and ground-truth segmentations.
- **Inputs subject IDs incorrectly inserted. Check them again.**: Use inputs from one subject.

## On [Brainlife.io](http://brainlife.io/)

You can submit this App online at https://doi.org/10.25663/brainlife.app.212 via the “Execute” tab.

Inputs: \
The two inputs are (i) a collection of estimated masks and (ii) a collection of ground truth masks. If you have bundles in WMC format, you can convert them in the correct datatype by using this App: https://doi.org/10.25663/brainlife.app.142. WARNING: be sure that the two collections contain the exact same bundles, and that are in the same anatomical space.

Output: \
Along with the DSC score, other 5 common scores are returned, specifically: 
* [Dice Similarity Coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient) (DSC) 
* [Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index) (J) 
* [sensitivity](https://en.wikipedia.org/wiki/Sensitivity_and_specificity) (sens)
* [True Positives](https://en.wikipedia.org/wiki/False_positives_and_false_negatives) (TP) 
* [False Positives](https://en.wikipedia.org/wiki/False_positives_and_false_negatives) (FP)
* [False Negatives](https://en.wikipedia.org/wiki/False_positives_and_false_negatives) (FN)

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- DSC evaluation (wmc - wmc) - Seperate tractograms. brainlife.io App. [doi:10.25663/brainlife.app.729](https://doi.org/10.25663/brainlife.app.729)
- Dice LR. Measures of the amount of ecologic association between species. Ecology 26(3):297-302 (1945).
- Dice, L. R., 1945. Measures of the amount of ecologic association between species. Ecology 26 (3), 297–302. [https://www.jstor.org/stable/1932409](https://www.jstor.org/stable/1932409)
- Garyfallidis et al. Dipy, a library for the analysis of diffusion MRI data. *Frontiers in Neuroinformatics* 8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Giulia Bertò

**Contributors**

- Emanuele Olivetti

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>
