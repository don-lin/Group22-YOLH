import pandas as pd
import sklearn
df = pd.read_csv('b.csv')


# Clean the data

categoryCol=['substrict','type','direction']
for i in categoryCol:
    df[i]=df[i].astype("category")

df['time'] = pd.to_datetime(df['time'], format='%Y.%m.%d')

for i in range(len(df)):
    if df.loc[i,'time'] < pd.Timestamp(2011, 1, 1):
        df.loc[i,'time']=pd.Timestamp(2011, 1, 1)

def cleanMinus(data):
    data=str(data)
    if data.find('-')==-1:
        return data
    data=data.split('-')
    return data[0]

def cleanColMinus(df,colName):
    for i in range(len(df)):
        df.loc[i,colName]=cleanMinus(df.loc[i,colName])

minusCols=['price','price per m2']
for i in minusCols:
    cleanColMinus(df,i)
    df[i]=df[i].astype('float64')

df.index = df['time']
#df.price.plot(figsize=(15,8), title= 'house price trend', fontsize=14)

from sklearn import preprocessing
typeEncoder=preprocessing.LabelEncoder().fit(df['type'])
directionEncoder=preprocessing.LabelEncoder().fit(df['direction'])

df['type']=typeEncoder.transform(df['type'])
df['direction']=directionEncoder.transform(df['direction'])


X_train=df[['X','Y','time','type','direction','square']]
X_train=df[['X','Y','type','direction','square']]

allRow=int(len(X_train)*0.8)
y_train=df['price']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=0)


from sklearn.tree import DecisionTreeClassifier
decclf = DecisionTreeClassifier()
decclf = decclf.fit(X_train,y_train)
dec_pred = decclf.predict(X_test)
# Now, we calculate the RMSE value.

def calculateRMSE(pred,real):
    return ((pred - real) ** 2).mean() ** .5

def calculateMSE(pred,real):
    return calculateRMSE(pred,real)**2

def calculateR2(pred,real):
    return sklearn.metrics.r2_score(real, pred, sample_weight=None, multioutput='uniform_average')

from sklearn.linear_model import LinearRegression
linearclf=LinearRegression()
linearclf = linearclf.fit(X_train,y_train)

linear_pred = linearclf.predict(X_test)
linearRMSE=((linear_pred - y_test) ** 2).mean() ** .5
print('linear success')

from sklearn.neighbors import KNeighborsClassifier
knnclf = KNeighborsClassifier()
knnclf = knnclf.fit(X_train,y_train)
knn_pred = knnclf.predict(X_test)
knnRMSE=((knn_pred - y_test) ** 2).mean() ** .5
print('knn success')


from sklearn import svm
svmclf = svm.SVC(kernel='linear',max_iter=20)
svmclf = svmclf.fit(X_train,y_train)
svm_pred = svmclf.predict(X_test)
svmRMSE=((svm_pred - y_test) ** 2).mean() ** .5
print('svm success')

from sklearn.ensemble import RandomForestRegressor
rfclf = RandomForestRegressor(n_estimators=10, max_depth=3, random_state=41)
rfclf = rfclf.fit(X_train,y_train)
rf_pred = rfclf.predict(X_test)
rfRMSE=((rf_pred - y_test) ** 2).mean() ** .5
print('rf success')


from sklearn.neural_network import MLPRegressor
mlpclf = MLPRegressor(random_state=41, max_iter=40,alpha = 1e-4,hidden_layer_sizes = (50,50),verbose = True)
mlpclf = mlpclf.fit(X_train,y_train)
mlp_pred = mlpclf.predict(X_test)
mlpRMSE=((mlp_pred - y_test) ** 2).mean() ** .5
print('nn success')

from sklearn.linear_model import Lasso
lassoclf=Lasso()
lassoclf = lassoclf.fit(X_train,y_train)
lasso_pred = lassoclf.predict(X_test)
lassoRMSE=((lasso_pred - y_test) ** 2).mean() ** .5
print('lasso success')

print('Decision Tree RMSE:',calculateRMSE(dec_pred,y_test))
print('Linear Regression RMSE:',calculateRMSE(linear_pred,y_test))
print('KNN RMSE:',calculateRMSE(knn_pred,y_test))
print('svm RMSE:',calculateRMSE(svm_pred,y_test))
print('lasso RMSE:',calculateRMSE(lasso_pred,y_test))
print('random forest RMSE:',calculateRMSE(rf_pred,y_test))
print('Neural Network RMSE:',calculateRMSE(mlp_pred,y_test))

print()

print('Decision Tree MSE:',calculateMSE(dec_pred,y_test))
print('Linear Regression MSE:',calculateMSE(linear_pred,y_test))
print('KNN MSE:',calculateMSE(knn_pred,y_test))
print('svm MSE:',calculateMSE(svm_pred,y_test))
print('lasso MSE:',calculateMSE(lasso_pred,y_test))
print('random forest MSE:',calculateMSE(rf_pred,y_test))
print('Neural Network MSE:',calculateMSE(mlp_pred,y_test))

print()

print('Decision Tree R2:',calculateR2(dec_pred,y_test))
print('Linear Regression R2:',calculateR2(linear_pred,y_test))
print('KNN R2:',calculateR2(knn_pred,y_test))
print('svm R2:',calculateR2(svm_pred,y_test))
print('lasso R2:',calculateR2(lasso_pred,y_test))
print('random forest R2:',calculateR2(rf_pred,y_test))
print('Neural Network R2:',calculateR2(mlp_pred,y_test))

import graphviz
from sklearn import tree
# DOT data
dot_data = tree.export_graphviz(decclf, out_file='a.png',
                                filled=True)

# Draw graph
graph = graphviz.Source(dot_data, format="png") 
graph.render("decision_tree_graphivz")