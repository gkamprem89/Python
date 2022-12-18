# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
city = ['Spain','India']
salary = [10000,20000]
Age = [17, 20]
dataset = pd.read_excel('country.xlsx')
dataset.to_csv("country1.xlsx")