# ML Interview Questions

## 🧠 1. ML Fundamentals
-	What is machine learning?

Machine learning is a subset of artificial intelligence where computers are trained to learn patterns from data and make decisions without being explicitly programmed. Instead of writing step-by-step instructions, developers feed data into algorithms, enabling the system to learn from experience and improve on its own over time.

-	Types of ML: supervised, unsupervised, reinforcement?

Supervised learning, the model is trained on a labeled dataset, which acts like an "answer key". The model learns the relationship between input features and known output variables.

Unsupervised learning works with unlabeled data, meaning the system must find hidden patterns or structures on its own without predefined answers.

Reinforcement learning is a feedback-based process where an "agent" learns to interact with an environment through trial and error. It receives rewards for correct actions and penalties for wrong ones to maximize overall long-term success.


-	What is overfitting and underfitting?

Overfitting: Too Complex

Overfitting occurs when a model learns the training data too well, memorizing the noise and random fluctuations instead of the underlying pattern.

The Cause: The model is too complex relative to the amount and simplicity of the data.

The Symptom: High accuracy on training data, but poor accuracy on new, unseen test data.

The Analogy: A student who memorizes the exact answers to a practice exam but fails the real test because the questions changed slightly.

The Fixes:

  * Simplify the model by reducing variables or features.

  * Gather more training data.

  * Use regularization techniques to penalize model complexity.

  * Stop training early before the model memorizes noise.

Underfitting: Too Simple

Underfitting occurs when a model is too simple to capture the underlying trend in the data.

The Cause: The model lacks the capacity or flexibility to learn the data's patterns.

The Symptom: Poor performance on the training data and poor performance on new test data.

The Analogy: A student who only studies one page of a textbook and fails both the practice exam and the real test.

The Fixes:

  * Increase model complexity (e.g., switch from linear to polynomial regression).

  * Feature engineering (add more relevant inputs or variables).

  * Decrease regularization constraints.

  * Train the model for a longer duration.

-	What is bias vs variance?

The Bias-Variance Tradeoff In data science, this concept is framed as managing Bias and Variance:

Underfitting = High Bias: The model makes strong, incorrect assumptions about the data, ignoring its actual complexity.

Overfitting = High Variance: The model is highly sensitive to small fluctuations in the training set, changing wildly with different data.

-	What is regularization?

Regularization is a technique used to prevent overfitting by adding a penalty to the model's complexity.It discourages the machine learning model from learning overly complex patterns, keeping it simple enough to perform accurately on new, unseen data.

During training, a regression model minimizes its Loss (the error between actual and predicted values). Regularization alters this process by adding a penalty score to the loss:

Total Cost = Loss(Prediction Error) + Penalty (Model Complexity)

If the model tries to create a highly flexible, wiggly line to touch every single training data point, the Penalty increases dramatically. This forces the model to settle for a smoother, simpler line that generalizes better. 

There are three common ways to calculate and apply this complexity penalty in regression: L1 Regularization (Lasso Regression), L2 Regularization (Ridge Regression), Elastic Net Regularization

## 📊 2. Supervised Learning
-	Difference between classification and regression?

  Classification predicts discrete categories or labels (e.g., "spam" vs. "not spam"). Regression predicts continuous, numerical quantities (e.g., the price of a house or temperature). Both are forms of supervised machine learning, but they fundamentally differ in the type of output they produce.
  
-	What is linear regression? assumptions?

Linear regression works reliably only when certain key assumptions about the data are met. These assumptions ensure that the model’s estimates are accurate, unbiased, and suitable for prediction. Some of the assumptions of linear regression are: Linearity, Homoscedasticity of Residuals, Multivariate Normality - Normal Distribution, Independence of Errors, Lack of Multicollinearity, Absence of Endogeneity
  
-	What is logistic regression?

  Logistic regression is a supervised machine learning and statistical algorithm used to predict the probability that a given data point belongs to a specific category. Instead of predicting continuous numbers (like linear regression), it uses a logistic (sigmoid) function to map outputs to a probability between 0 and 1.

-	What is decision tree?

  A decision tree is a flowchart-like model used to map out decisions, their potential outcomes, and associated costs. It works by breaking down a complex problem into a series of simple, conditional yes-or-no questions, allowing individuals or algorithms to evaluate the best course of action.
  
-	What is Random Forest and why is it better than a single tree?

  A Random Forest is an ensemble machine learning algorithm that creates a "forest" of multiple individual decision trees and merges them together for a more accurate and stable prediction. A single decision tree is like a strict flowchart—it is highly intuitive, but it often struggles when applied to new, unseen data. A Random Forest improves upon this limitation through a few key mechanisms - Drastically Reduced Overfitting, The "Wisdom of Crowds", Bootstrap Sampling, Feature Randomness.

## 📊 2. Unsupervised Learning
- What are the main types of unsupervised learning?

 Clustering: Grouping similar data points together. Common algorithms include K-Means (groups into \(K\) distinct clusters), DBSCAN (groups based on data point density), and Hierarchical Clustering (creates a tree of clusters).
 
 Dimensionality Reduction: Compressing features while retaining the underlying structure of the dataset. Common techniques include PCA (Principal Component Analysis) for linear data, and t-SNE or UMAP for visualizing high-dimensional data.
 
 Association Rule Learning: Uncovering logical relationships and rules between variables, such as discovering items frequently bought together in retail.

## 🔍 3. Model Evaluation
- Evaluation metric for supervised vs unsupervised?

  Supervised learning evaluation is highly objective because you can directly compare the model's predictions against the actual known outcomes (y). The metrics are divided by task type:

  Classification Metrics (Predicting Categories) - Accuracy, Precision, Recall, F1-score, ROC-AUC

  Regression Metrics (Predicting Numbers) - MAE, MSE, RMSE, R2
  
-	What is accuracy, precision, recall, F1-score?

    + Accuracy: The percentage of total correct predictions. It works well only if your dataset is balanced.
    + Precision: Out of all predicted positives, how many were actually positive? Use this when false positives are costly (e.g., email spam filtering).
    + Recall (Sensitivity): Out of all actual positives, how many did the model find? Use this when false negatives are dangerous (e.g., medical diagnoses).
    + F1-Score: The harmonic mean of precision and recall. It provides a single balance score for imbalanced data.
    + ROC-AUC: Measures the model's ability to distinguish between classes across all possible thresholds.
-	When do you use precision vs recall?

  Use Precision when the cost of a False Positive is high. Use Recall when the cost of a False Negative is high.
-	What is confusion matrix?

  A Confusion Matrix is a tabular summary that visualizes the performance of a classification model by comparing its predictions against the actual ground-truth labels. 
-	What is ROC-AUC?

  ROC-AUC is a performance metric used to evaluate a binary classification model by measuring its ability to distinguish between two classes across all possible decision thresholds. Instead of evaluating the model at just one specific cutoff (like the default [50%]), ROC-AUC evaluates how well the model separates and ranks the data overall.

## ⚙️ 4. Feature Engineering
-	What is feature engineering?

  Feature engineering is the process of transforming raw data into meaningful, structured inputs (features) that machine learning models use to make predictions. It involves selecting relevant data, modifying existing variables, and creating new ones to improve a model's accuracy and performance. Feature engineering relies on several key methods to optimize your dataset - Imputation, scaling, normalization, encoding, feature creation, feature selection.
  
-	Why is scaling important?

  Scaling is important because machine learning algorithms struggle when different data inputs have vastly different numeric ranges. Large values overpower small values during model training, Algorithms find the optimal solution much faster, Algorithms treating data geometrically require uniform scales.
-	What is normalization vs standardization?

  Normalization and standardization are the two most common techniques used to scale data for machine learning. While both transform features to a common scale, they calculate that scale differently and serve different purposes. Normalization (Min-Max Scaling): Rescales data into a fixed range, usually between 0 and 1. Standardization (Z-Score Normalization): Rescales data so it has a mean of 0 and a standard deviation of 1.

  Use Normalization when: You know the exact minimum and maximum bounds of your data (e.g., image pixels from 0 to 255).Your algorithm requires a bounded range, such as Neural Networks or KNN.Your data does not follow a bell curve (Gaussian distribution).
  
  Use Standardization when: Your data contains outliers, as normalization will compress the normal data into a tiny range to accommodate the extreme values.Your algorithm assumes the data is normally distributed, such as Linear Regression, Logistic Regression, or Support Vector Machines (SVM).
  
-	How do you handle categorical variables?

  Handling categorical variables requires converting text labels or categories into numbers because machine learning models can only perform mathematical operations. 
  
   * One-Hot Encoding: Creates a new binary (0 or 1) column for every unique category in a feature. 
   * Ordinal Encoding: Assigns a unique integer to each category based on a specific, meaningful order.
   * Label Encoding: Assigns a unique integer to each category randomly, without implying any specific order.
   * Target Encoding: Replaces each category with the average value of the target output variable for that category.

## 🔄 5. Data Handling
-	How do you handle missing data?

  Handling missing data requires either removing the incomplete records or replacing the missing values with calculated estimates. The right choice depends on the amount of missing data and the type of feature. 
  
  Core Techniques
    * Deletions: Removing missing values from the dataset entirely.
    * Imputation: Replacing missing cells with computed statistical values.
    * Flagging: Creating an indicator column to tell the model a value was missing.
  
-	What is data leakage?

  Data leakage in machine learning occurs when a model unintentionally uses information from outside the training dataset, such as future data or test results. This "cheating" artificially inflates the model's accuracy during testing, but causes it to fail dramatically when making predictions in the real world. To prevent data leakage in machine learning projects, implement the following best practices: Always divide your data into training, validation, and test sets before performing any exploratory data analysis or feature engineering, Scale, normalize, or impute missing values only on the training data, and then apply those exact same transformations to your test data, Ensure that all features used to train the model would logically exist and be available at the exact moment a prediction needs to be made in a live, production environment.
  
-	How do you split data (train/test/validation)?

  Data splitting separates your dataset into distinct subsets to train your model and accurately test its real-world performance. You must perform this split before any data preprocessing to prevent data leakage. 
  
  The Three Data Subsets: Training Set (60–80%), Validation Set (10–20%), Testing Set (10–20%). 

  Standard Splitting Methods: Random Splitting, Stratified Splitting, Time-Based (Temporal) Splitting
  
-	What is cross-validation?

  Cross-validation is a resampling technique used to evaluate how well a machine learning model generalizes to unseen data. It splits a single dataset into multiple parts, training the model on some parts and testing it on the remaining parts to ensure the model does not just memorize the training data (overfitting).

  Common Types : K-fold, Stratified k-fold, time series split.

## 🧠 6. Time Series 
-	What is time-series data?
-	What is LSTM and why is it used?
-	What is stationarity?
-	How do you handle trends and seasonality?
-	How do you evaluate time-series models?


## 🤖 7. Deep Learning Basics
-	What is a neural network?
-	What are activation functions?
-	What is backpropagation?
-	What is gradient descent?

## 📈 8. Model Optimization
-	What is hyperparameter tuning?
-	Grid search vs random search?
-	What is learning rate?
-	What is early stopping?


## 🧩 9. Real-world / Scenario Questions
-	How would you build a fraud detection system?
-	How do you handle imbalanced data?
-	Your model accuracy is high but business performance is low—why?
-	How would you deploy an ML model?
  
## 🔄 10. ML Pipeline
-	What are steps in ML pipeline?
-	How do you move from training → production?
-	What is feature store?
-	What is model monitoring?


## ☁️ 11. ML in Cloud 
-	How do you deploy ML models on AWS?
-	What is SageMaker?
-	How do you build scalable ML pipelines?

## 🔥 12. Advanced (to stand out)
-	What is ensemble learning?
-	What is boosting vs bagging?
-	What is SHAP / explainability?
-	What is concept drift?

