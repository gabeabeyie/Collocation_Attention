### BEYOND NEWS HEADLINES AND TFIDF: ENHANCING TEXT-BASED FORECASTING MODELS WITH VALIDATED COLLOCATIONS AND IMPROVED ATTENTION

### Overview
This repository contains the replication files for the project, "Beyond news headlines and TFIDF: Enhancing text-based forecasting models with validated colocations and improved attention". The project includes Jupyter notebooks, datasets, and result files that demonstrate the forecasting methodology and findings.

To replicate the main results of the paper, run the python scripts in the notebooks:

    main_results.ipynb
    Appendix.ipynb
The following notebooks generates the forecast values all the different models in the paper. Note that, they take longer to run. The results are in the ```forecasts/``` folder. Hence no need to run them.

    Appendix_alternative_updating_scheme.ipynb
    Benchmark_models.ipynb
    Continuous.ipynb
    FredMD.ipynb
    Sahm_Rule.ipynb

### Repository Structure

```\
  ├── notebooks/                     # Jupyter notebooks for analysis

  │   ├── FredMD.ipynb               # Code for generating forecast using both text data and FRED-MD

  │   ├── main_results.ipynb         # Main results generation

  │   ├── Sahm_Rule.ipynb            # Code for generating forecast using Sahm-Rule updating scheme

  │   ├── Appendix.ipynb             # Appendix results

  │   ├── Appendix_alternative_updating_scheme.ipynb  # Code for generating forecast using alternative updating scheme

  │   ├── Benchmark_models.ipynb     # Benchmark forecasting models

  │   ├── Continuous.ipynb           # Code for generating forecast using continuous updating scheme

  ├── data/                          # Contains all datasets used

  ├── forecasts/                     # Contains forecasts generated from models

  ├── results/                       # Main results-This folder would be generated once main_results.ipynb is run (tables, figures)

  ├── appendix_results/              # Output results (tables, figures)

  ├── complete_words.json            # JSON file containing list of words used in the text-based forecasting

  ├── requirements.txt               # List of dependencies for replication

  ├── run.py                         # Script to automate execution (optional)

  └── README.md                      # Project documentation (this file)
```

## Getting Started

## Prerequisites
Ensure you have Python installed. Clone this repository and install dependencies:

```\
git clone https://github.com/yourusername/Collocation_Attention.git

cd Collocation_Attention

pip install -r requirements.txt
```
## Running the Project

To replicate the main results, execute:

    jupyter notebook notebooks/main_results.ipynb

This will generate a ```results/``` folder with tables and figures.

To generate appendix results, run:

    jupyter notebook notebooks/Appendix.ipynb

This will create the ```appendix_results/``` folder with appendix data.

## Automating Execution (Optional)

A ```run.py``` script will be provided to streamline execution of multiple notebooks in sequence.

## Results

  The ```results/``` folder contains all final outputs (tables, charts, key figures).

  The ```appendix results/``` folder contains all appendix outputs (tables, charts, key figures).

  The ```forecasts/``` folder contains generated forecasts for different models.

  The ```data/``` folder includes the datasets used for forecasting.

## Contributing

If you would like to contribute or suggest improvements, feel free to open a pull request or issue.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or collaboration, reach out via [Email](gappau@ymail.com) or connect on [LinkedIn](https://www.linkedin.com/in/gabrielabeyie/).

