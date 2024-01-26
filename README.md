# aicure_The-Noobs


## Task
The goal is to construct an advanced model capable of accurately predicting an individual's heart rate.The dataset encompasses diverse attributes derived from signals measured through ECG recordings for various individuals, each exhibiting different heart rates at the respective time of measurement. These features collectively contribute to determining the heart rate at the specific moment for each individual.

## Files Descriptions
- '.ipynb' : Jupyter notebook containing your experiments
- '.joblib' : Trained model to be used.
- 'run.py': Script which runs the model and predicts and stores the output in a .csv file based on the input (.csv) given.
- 'Report' : Contains the research work done to decide upon which Machine Learning Model to be used.


## Local Quickstart

Follow these steps to get the model running locally.

### 1. Install dependencies
 Open a terminal and run
```bash
pip install joblib
```
```bash
pip install pandas
```
```bash
pip install sklearn.preprocessing
```
### 2. Run the script 'run.py'

To generate the `results.csv` that contains the predicted Heart Rate values, run:
```bash
python run.py test_data.csv
```

