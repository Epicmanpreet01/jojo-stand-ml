# JoJo Stand Strength Analysis and Prediction

A machine learning project that analyzes the statistics of Stands from JoJo's Bizarre Adventure to identify patterns, discover natural strength categories, and predict Stand strength levels.

The project combines unsupervised and supervised machine learning techniques. KMeans clustering is used to identify natural groupings within the Stand statistics, while multiple classification models are trained to predict the strength category of a Stand based on its attributes.

## Features

* Analysis of JoJo Stand statistics
* Data preprocessing and numerical encoding
* Missing value handling
* Exploratory Data Analysis
* KMeans clustering for discovering strength categories
* PCA visualization for cluster analysis
* Supervised machine learning models
* Comparison of multiple classification algorithms
* Interactive prediction for new Stand statistics
* Model evaluation using multiple performance metrics

## Stand Statistics

The dataset contains multiple attributes used to describe each Stand:

* PWR (Power)
* SPD (Speed)
* RNG (Range)
* PER (Perception)
* PRC (Precision)
* DEV (Development)

These statistics are originally represented using letter grades and are converted into numerical values for machine learning analysis.

## Data Processing

The project follows a data preprocessing pipeline before training the machine learning models.

### Grade Encoding

The Stand statistics are converted from letter grades into numerical values:

| Grade | Value |
| ----- | ----: |
| F     |     0 |
| E     |     2 |
| D     |     4 |
| C     |     6 |
| B     |     8 |
| A     |    10 |
| Infi  |    20 |

### Preprocessing Steps

The dataset processing includes:

1. Handling missing values.
2. Converting letter grades into numerical values.
3. Normalizing features using StandardScaler.
4. Balancing the dataset using upsampling for supervised learning.

## Machine Learning Approach

### Unsupervised Learning

The project uses KMeans clustering to identify natural strength groupings among Stands.

The clustering model divides the dataset into four groups:

* Rank 0: Weak Stands
* Rank 1: Average Stands
* Rank 2: Strong Stands
* Rank 3: God Tier Stands

PCA is used to visualize the clusters in a two-dimensional space.

### Supervised Learning

After generating strength labels through clustering, multiple classification models are trained to predict the strength category of a Stand.

The following algorithms are evaluated:

* Logistic Regression
* Random Forest Classifier
* Support Vector Classifier
* K-Nearest Neighbors
* Gradient Boosting Classifier

## Model Evaluation

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Reports

The project also compares the performance of multiple machine learning algorithms to identify how effectively each model predicts Stand strength categories.

## Tech Stack

### Programming and Machine Learning

* Python
* Scikit-learn
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Development Environment

* Jupyter Notebook

## Project Structure

```text id="5pt0jz"
jojo-stand-ml/
│
├── data/
│   ├── jojo-stands.csv
│   ├── encoded-jojo-stands.csv
│   └── labeled-encoded-jojo-stands.csv
│
├── notebooks/
│   ├── unsupervisedClusteringModel.ipynb
│   └── supervisedPredictionModel.ipynb
│
├── figures/
│   ├── EDA/
│   ├── clustering/
│   └── supervisedEvaluation/
│
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation

### Clone the Repository

```bash id="1bmbs7"
git clone https://github.com/Epicmanpreet01/jojo-stand-ml.git
cd jojo-stand-ml
```

### Create a Virtual Environment

Creating a virtual environment is recommended.

```bash id="5g9ktb"
python -m venv venv
```

Activate the environment.

On Windows:

```bash id="k9s7o4"
venv\Scripts\activate
```

On macOS or Linux:

```bash id="agrc2c"
source venv/bin/activate
```

### Install Dependencies

```bash id="s8nhqq"
pip install -r requirements.txt
```

## Running the Project

Start Jupyter Notebook:

```bash id="u8y5um"
jupyter notebook
```

### Step 1: Unsupervised Analysis

Start with:

```text id="l6syrq"
unsupervisedClusteringModel.ipynb
```

This notebook performs:

* Data preprocessing
* Feature normalization
* KMeans clustering
* PCA visualization
* Cluster analysis

It also generates the labeled dataset used for supervised learning.

### Step 2: Supervised Prediction

Run:

```text id="qojpvz"
supervisedPredictionModel.ipynb
```

This notebook:

* Loads the labeled dataset
* Processes and balances the data
* Trains multiple classification models
* Evaluates model performance
* Compares different algorithms
* Allows prediction of strength categories for new Stand statistics

## How It Works

The project follows the following workflow:

```text id="qtw48b"
Raw Stand Statistics
        │
        ▼
Data Cleaning and Preprocessing
        │
        ▼
Letter Grade Encoding
        │
        ▼
Feature Normalization
        │
        ▼
KMeans Clustering
        │
        ▼
Strength Category Labels
        │
        ▼
Supervised Model Training
        │
        ▼
Model Evaluation and Comparison
        │
        ▼
Stand Strength Prediction
```

## Results

The analysis identifies four primary Stand strength categories based on their statistical attributes.

The project includes:

* Four KMeans-derived strength clusters
* Six primary Stand statistics
* Five supervised machine learning models
* PCA-based cluster visualization
* Exploratory data analysis
* Confusion matrices for individual models
* Performance comparison across classification algorithms

## Learning Objectives

This project was developed to gain hands-on experience with:

* Data preprocessing
* Feature engineering
* Exploratory Data Analysis
* Unsupervised machine learning
* KMeans clustering
* Principal Component Analysis
* Supervised machine learning
* Classification algorithms
* Dataset balancing
* Model evaluation and comparison
* Data visualization using Python

## Future Improvements

Potential improvements for the project include:

* Testing additional clustering algorithms
* Hyperparameter optimization
* Implementing more advanced classification models
* Building an interactive web interface
* Creating a real-time Stand strength prediction tool
* Adding more detailed statistical analysis
* Exploring dimensionality reduction techniques beyond PCA

## Dataset

The dataset used in this project is based on JoJo Stand statistics and contains the attributes used for the machine learning analysis.

The dataset and its original source should be used according to their respective licensing terms.

## Disclaimer

This project is created for educational and experimental purposes. JoJo's Bizarre Adventure and its associated characters and concepts belong to their respective copyright holders.

## License

The code in this repository is licensed under the MIT License.

The dataset is subject to the licensing terms of its original source.
