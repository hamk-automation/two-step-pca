import two_step_pca as TS_PCA 
import pandas as pd 
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('clean_data.csv', index_col=0, sep=";")
#limiting the amount of data, so you can check at least something visually
#it is a litle bit complicated to do then you have 20 columns initially and even more after time shifting (a lot more)
data = df[df.columns.values[1:6]]
np_data = data[:500].values
U, A, tildaX = TS_PCA.fit_transform(np_data, 6, 50)
print("U.shape: {}  A.shape: {}  tildaX.shape: {}".format(U.shape, A.shape, tildaX.shape))

scaler = StandardScaler()
U = scaler.fit_transform(U)
print("U: \n",U[:5])

T, P, E, var_explained = TS_PCA.pca(U)
print("T.shape: {} P.shape: P{} E.shape: {} ".format(T.shape, P.shape, E.shape))
print("Variance explained: ", var_explained)
T_l, E_l, T_rest = TS_PCA.dividePCs(T, E, var_explained, 0.8)
print("T_l.shape: {} E_l.shape: {} T_rest.shape: {}".format(T_l.shape, E_l.shape, T_rest.shape))
T2 = TS_PCA.computeT2(T_l, E_l)
print("Hotelling's T2 metric: \n", T2[:5])
SPE = TS_PCA.computeSPE(T_rest)
print("SPE: \n", SPE[:5])

