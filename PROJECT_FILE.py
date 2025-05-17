# Import necessary libraries

import pandas as pd          # Data manipulation
import numpy as np           # Numerical operations
import seaborn as sns        # Statistical data visualization
import matplotlib.pyplot as plt  # General plotting

# Setting seaborn style for better looking plots
sns.set(style="whitegrid")
# Load the CSV into a DataFrame
df = pd.read_csv('ai_impact_dataset.csv')

# Show the first few rows
df.head()
print("umr")