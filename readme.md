# 🧍 JoJo Stand Strength Analysis & Prediction

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-FE7923?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

> A machine learning project analyzing **JoJo’s Bizarre Adventure** stand stats using **unsupervised clustering** and **supervised classification** to predict strength categories.

---

## 📊 Project Overview

JoJo stands are ranked by stats like Power, Speed, Range, etc., typically letter-graded from A to E. We performed:

- **Data Encoding**: Converting letter grades into numerical values.
- **Clustering**: Using **unsupervised learning (KMeans)** to derive strength categories.
- **Supervised Prediction**: Training a model to predict these strength clusters from stats.

---

## 📁 Dataset

- `jojo-stands.csv`: Original letter-graded stats.
- `encoded-jojo-stands.csv`: Numerically encoded stats.
- `labeled-encoded-jojo-stands.csv`: Encoded stats with cluster-assigned rank labels.

---

## 🧪 Models

### 🔹 Unsupervised Learning (`unsupervisedClusteringModel.ipynb`)

- **KMeans Clustering** was used to assign unsupervised strength categories (`Rank`).
- Result: 3 strength clusters emerged, possibly representing **Low, Mid, High tiers**.

### 🔸 Supervised Learning (`supervisedPredictionModel.ipynb`)

- Various models (like `RandomForest`, `SVC`, etc.) were trained to predict the cluster label from the stats.
- Used accuracy, confusion matrix, and classification reports for evaluation.

---

## 📈 Visualizations

### 🔍 Stat Distribution

![Stat Distribution](./jojo_figures/stat_distribution.png)

### 🔁 Correlation Between Stats

![Stat Correlation](./jojo_figures/stat_correlation.png)

### 🧩 Cluster (Rank) Distribution

![Rank Distribution](./jojo_figures/rank_distribution.png)

---

## 💡 Insights

- **PER (Perception)** shows high values across most stands — likely a key stat.
- Clustering found **3 tiers** of stand strength not explicitly defined in canon.
- Strongest stands tend to have higher **PWR**, **SPD**, and **DEV**.

---

## 🚀 How to Run

```bash
git clone https://github.com/your-username/jojo-stand-strength-analysis.git
cd jojo-stand-strength-analysis

# Create environment
pip install -r requirements.txt

# Launch notebooks
jupyter notebook
```
