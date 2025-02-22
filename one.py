import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

df = pd.read_csv("cleaned_dataset.csv")
print(df.head())
print(df['label'].value_counts())

import matplotlib.pyplot as plt

plt.hist(df['label'],color = 'r')
plt.title("Bar plot")
plt.xlabel("fraud calls vs normal calls")
plt.ylabel("count")