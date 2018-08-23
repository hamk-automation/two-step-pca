import two_step_pca as tsp
import pandas as pd 
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from pathlib import Path
from os import listdir
import numpy as np

def load_simulation_data(folder):
    """
    Loads csv files from "folder" as numpy arrays
    Arguments:
        folder - name of the folder where the data is located
    Returns:
        sims - dictionary {file_name : numpy array with loaded csv}
    """
    files_list = listdir(folder)
    sims = {}
    #load all csv files as df into the sims list
    for file in files_list:
        path = folder + '/' + file
        sims.update({file[:-4] :pd.read_csv(path, sep=",")})
    #remove info about disturbance
    sims.pop('disturbance', None)
    return sims

#load all the files from 'Faults' folder
data_list = load_simulation_data('Faults')
#get training data from the list
train_data = data_list['no_disturbance']

ts_pca = tsp.TS_PCA()
ts_pca.fit(train_data, 1, 200)

#testing
test_data_dict = {}

#compute metrics for all test cases 
for key in data_list:
    metrics_df = ts_pca.detect(data_list[key], 0.8)
    test_data_dict.update({key: metrics_df})

#get disturbance
disturbance = pd.read_csv('Faults/disturbance.csv', sep=",").values
#warning: during the fault 6 reactor shuts down shortly after disturbance rising, but the disturbance graph is for the full 
#simulation - that is the reason for strange graph axes
#second warning: obviously there is no disturbance for "no_disturbance" example, it just lazy me, who didnt want to make anything with it

for key in test_data_dict:
    plt.title(key)
    plt.subplot(3, 1, 1)
    plt.ylabel('T2: ' + key)
    plt.plot(test_data_dict[key]['T2'])
    plt.subplot(3, 1 , 2)
    plt.ylabel('SPE: ' + key)
    plt.plot(test_data_dict[key]['SPE'])
    plt.subplot(3, 1, 3)
    plt.ylabel('Disturbance')
    plt.plot(disturbance)
    plt.show()
