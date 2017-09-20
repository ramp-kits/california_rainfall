# California Winter Extreme Rainfall Prediction

David John Gagne (dgagne@ucar.edu)

### Setup

To prepare your local machine to process the data for this competition, first install the Miniconda Python distribution [here](https://conda.io/miniconda.html). Then install the required dependencies for the contest using the following command line command:
```bash
conda env create -f environment.yml
source activate ramp_ci_2017
```
If you have trouble creating a conda environment from the environment.yml file, try the following steps to manually install the necessary Python libraries:
```bash
conda create --name ramp_ci_2017 -c conda-forge python=3.6 numpy scipy matplotlib cartopy scikit-learn pandas xarray ipython jupyter
source activate ramp_ci_2017
```

Download the contest data using the following command
```bash
python download_data.py
```

Install [ramp-workflow](https://github.com/paris-saclay-cds/ramp-workflow) within the `ramp_ci_2017` enviornment, then execute the following line
```bash
ramp_test_submission
```
to make sure the starting kit submission works. Once you create your own submission, you can test it using the same command.
