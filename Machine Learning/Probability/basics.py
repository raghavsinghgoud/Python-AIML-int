import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm                # Normal Distribution Calculator
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.ensemble import RandomForestClassifier

# #You feed it a mean and standard deviation , and it can answer any probability question about q.

# #Normal Distribution - The bell curve 
# #Normal Distribution with mean 165cm and standard deviation 7cm.
# mean_h, std_h = 165,7

# # Probability of being taller than 175cm
# prob = 1 - norm.cdf(175, mean_h, std_h) # Cumulative distribution function, tells how many prob.
# print(f'P(height > 175cm) = {prob:.4f} = {prob>100:.1f}%')

# # The 68-95-99.7 Rule
# print(f'68% of people: {mean_h-std_h:.0f}cm to {mean_h+std_h:.0f}cm')
# print(f'95% of people: {mean_h-2*std_h:.0f}cm to {mean_h+2*std_h:.0f}cm')
# print(f'99% of people: {mean_h-3*std_h:.0f}cm to {mean_h+3*std_h:.0f}cm')


'''Simulated dataset: 500 student records'''
# np.random.seed(42)
# x= np.random.randn(500,5)  # 5 features (study hrs, attendance, etc.)
# y = np.random.randint(0,2,500) # Labels: pass(1)/fail(0)

# # 80/20 Train-Test Split
# x_train,x_test,y_train,x_test = train_test_split(
#     x,y, test_size = 0.2, random_state= 42, stratify= y
# )
# print(f'Training samples: {len(x_train)} | Test samples: {len(x_test)}')


'''5-Fold Cross-Validation - more reliable than single split'''

# model = RandomForestClassifier(n_estimators= 50, random_state= 42)
# cv_scores = cross_val_score(model,x,y,cv=5, scoring='accuracy')
# print(f'CV Scores each fold: {cv_scores.round(3)}')
# print(f'Mean: {cv_scores.mean():.4f} ± {cv_scores.std():.4f} ')
