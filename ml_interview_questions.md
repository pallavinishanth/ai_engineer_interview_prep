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
-	What is ROC-AUC?

## ⚙️ 4. Feature Engineering
-	What is feature engineering?
-	Why is scaling important?
-	What is normalization vs standardization?
-	How do you handle categorical variables?

## 🔄 5. Data Handling
-	How do you handle missing data?
-	What is data leakage?
-	How do you split data (train/test/validation)?
-	What is cross-validation?

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

