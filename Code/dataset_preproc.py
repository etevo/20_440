import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load data
data = pd.read_csv('../project_folder/Dataset/fpkm_table_normalized.csv')
data = data.iloc[1:,1:]
#Z-score data
mean = data.mean(axis=1)
std_dev = data.std(axis =1)

data = data.subtract(mean,axis =0)
data = data.divide(std_dev, axis=0)

data = data.transpose() #Improve heatmap visualization

#Remove empty values
data = data.dropna(axis = 1)
data = data.dropna(axis = 0)

#Plot a heatmap of expression data for the first 1000 genes
fig = plt.figure(figsize = (20,10))

plt.matshow(data.iloc[:, :500], cmap = 'PiYG', vmin = -1, vmax = 1)
plt.colorbar(shrink = 0.5)

plt.xlabel('Gene ID')
plt.ylabel('Patient ID')
plt.title('Normalized FPKM Counts')

#plt.show()

plt.savefig('Figure/Figure1_FPKM_Heatmap.png')
