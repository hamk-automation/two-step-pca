import two_step_pca as TS_PCA 
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
        sims.update({file[:-4] :pd.read_csv(path, sep=",").values})
    #remove info about disturbance
    sims.pop('disturbance', None)
    return sims

#load all the files from 'Faults' folder
data_list = load_simulation_data('Faults')
#get training data from the list
train_data = data_list['no_disturbance']
#training - you only need A_train values from this function, but we still fetching them all to test dimensionality
U_train, A_train, tildaX_train = TS_PCA.fit_transform(train_data, 1, 200)
print("U_train.shape: {}  A_train.shape: {}  tildaX_train.shape: {}".format(U_train.shape, A_train.shape, tildaX_train.shape))
#creating scaler 
scaler = StandardScaler()
scaler.fit(U_train)
#testing
test_data_dict = {}

#big loop for big guys
#compute innovation component based on dynamic part for "ideal" data
#then use pca on innovation component and calcualte metrics 
#and in the end put all those into a dict for later plotting
for key in data_list:
    tilda_test_X = TS_PCA.shift_data(data_list[key], 1) 
    U_test = data_list[key][1:] - np.dot(tilda_test_X, A_train) #[1:] because shift_data had lag parameter of 1, so we need to remove first element for allignment
    U_test = scaler.transform(U_test)
    T, P, E, var_explained = TS_PCA.pca(U_test)
    T_l, E_l, T_rest = TS_PCA.dividePCs(T, E, var_explained, 0.8)
    T2 = TS_PCA.computeT2(T_l, E_l)
    SPE = TS_PCA.computeSPE(T_rest)
    test_data_dict.update({key: [T2, SPE]})


#get disturbance
disturbance = pd.read_csv('Faults/disturbance.csv', sep=",").values
#warning: during the fault 6 reactor shuts down shortly after disturbance rising, but the disturbance graph is for the full 
#simulation - that is the reason for strange graph axes
#second warning: obviously there is no disturbance for "no_disturbance" example, it just lazy me, who didnt want to make anything with it
for key in test_data_dict:
    plt.title(key)
    plt.subplot(3, 1, 1)
    plt.ylabel('T2: ' + key)
    plt.plot(test_data_dict[key][0])
    plt.subplot(3, 1 , 2)
    plt.ylabel('SPE: ' + key)
    plt.plot(test_data_dict[key][1])
    plt.subplot(3, 1, 3)
    plt.ylabel('Disturbance')
    plt.plot(disturbance)
    plt.show()
