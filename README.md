
# Malware Detection with Clustering and Association Rule Learning

## Project Overview
This project involves the detection of malware using machine learning techniques. The dataset consists of software features that are used to classify or cluster data points into malware or non-malware categories.

## Dataset

- **Source**: The dataset is obtained from the [Kaggle Hackathon](https://www.kaggle.com/datasets/), specifically from the **Super AI Engineer Season 5 - Level 1 - Hackathon Online** competition.
- **Training Data**:
  - **train.csv**: The training set consisting of 107,548 entries, where each row represents a software sample with various features.
  - **test.csv**: The test set containing 26,887 entries to evaluate the trained model.
- **Features**: The dataset contains 2381 features representing different characteristics extracted from the software, with an additional `id` column and `label` column (0 for normal software, 1 for malware).
- **File Format**: CSV

## Methods Used

### 1. **Supervised Learning: Classification**
   - **Model**: XGBoost Classifier
   - **Objective**: Classify software samples as malware or non-malware based on extracted features.
   - **Evaluation**: The model is evaluated using accuracy and cross-validation.
   - **Libraries**: pandas, xgboost, sklearn

### 2. **Unsupervised Learning: Clustering**
   - **Method**: K-Means Clustering
   - **Objective**: Group software samples into clusters and analyze patterns in the clusters that may indicate malware characteristics.
   - **Evaluation**: The silhouette score is used to evaluate clustering quality.
   - **Libraries**: pandas, sklearn, matplotlib, seaborn

### 3. **Unsupervised Learning: Association Rule**
   - **Method**: FP-Growth Algorithm
   - **Objective**: Discover strong association rules between features, potentially linking certain feature patterns with malware behavior.
   - **Evaluation**: Association rules are evaluated based on support, confidence, and lift metrics.
   - **Libraries**: pandas, mlxtend

## How to Use

1. **Clone the repository**:
   ```bash
   git clone <repository_link>
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Data Loading**:
   - Load the dataset by specifying the file paths for `train.csv` and `test.csv`.
   - Use the `pd.read_csv()` function to load the dataset into pandas DataFrames.

4. **Data Preprocessing**:
   - Clean and prepare the dataset by handling missing values, normalizing features, and splitting data into training and test sets.

5. **Model Training (Classification)**:
   - Use **XGBoost** to train the classification model on the training dataset and evaluate it using cross-validation and accuracy metrics.

6. **Clustering**:
   - Apply **K-Means Clustering** to the dataset after reducing its dimensionality using **PCA** for better visualization and clustering performance.
   - Use silhouette scores to evaluate clustering performance.

7. **Association Rule Learning**:
   - Apply **FP-Growth** to discover association rules and analyze patterns in the features of the dataset.

## Results
- **Classification Accuracy**: The model achieved an accuracy of **0.9964** on the test dataset.
- **Clustering**: The dataset was successfully grouped into **7 clusters**. The clusters were analyzed to identify potential relationships with malware behavior.
- **Association Rules**: Strong association rules were generated, identifying feature patterns linked to malware samples.

## Conclusion
This project successfully demonstrates the use of machine learning techniques to classify, cluster, and discover patterns in a dataset for malware detection. Further work can involve tuning the models, improving preprocessing techniques, and exploring other unsupervised learning methods for enhanced performance.

## Acknowledgements
This project utilizes the dataset from the [Kaggle Online Hackathon](https://www.kaggle.com/datasets/). Special thanks to the Kaggle community for providing such valuable datasets for learning and competition.
