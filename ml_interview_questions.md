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

Simplify the model by reducing variables or features.

Gather more training data.

Use regularization techniques to penalize model complexity.

Stop training early before the model memorizes noise.

Underfitting: Too Simple

Underfitting occurs when a model is too simple to capture the underlying trend in the data.

The Cause: The model lacks the capacity or flexibility to learn the data's patterns.

The Symptom: Poor performance on the training data and poor performance on new test data.

The Analogy: A student who only studies one page of a textbook and fails both the practice exam and the real test.

The Fixes:

Increase model complexity (e.g., switch from linear to polynomial regression).

Feature engineering (add more relevant inputs or variables).

Decrease regularization constraints.

Train the model for a longer duration.

-	What is bias vs variance?
-	What is regularization?

## 📊 2. Supervised Learning
-	Difference between classification and regression?
-	What is linear regression? assumptions?
-	What is logistic regression?
-	What is decision tree?
-	What is Random Forest and why is it better than a single tree?

## 🔍 3. Model Evaluation
-	What is accuracy, precision, recall, F1-score?
-	When do you use precision vs recall?
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

