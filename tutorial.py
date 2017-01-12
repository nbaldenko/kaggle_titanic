# data analysis and wrangling
import pandas as pd
import numpy as np
import random as rnd

# visualization
import seaborn as sns
import matplotlib.pyplot as plt
#matplotlib inline

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

# read titanic training & test csv files as a pandas DataFrame
train_df = pd.read_csv('/Users/nicolasbaldenko/Documents/Portfolio/Data Science/Titanic/Data/train.csv')
test_df = pd.read_csv('/Users/nicolasbaldenko/Documents/Portfolio/Data Science/Titanic/Data/test.csv')

train_df.info()
print("_"*40)
test_df.info()

#print(train_df.columns.values)
#print(test_df.columns.values)
