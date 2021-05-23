import pandas as pd
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
y_train=df['price']

from sklearn.tree import DecisionTreeClassifier
decclf = DecisionTreeClassifier()
decclf = decclf.fit(X_train,y_train)

y_pred = decclf.predict(X_train)
# Now, we calculate the RMSE value.

from sklearn.linear_model import LinearRegression
linearclf=LinearRegression()
linearclf = linearclf.fit(X_train,y_train)
linear_pred = linearclf.predict(X_train)
linearRMSE=((linear_pred - y_train) ** 2).mean() ** .5

from sklearn.neighbors import KNeighborsClassifier
knnclf = KNeighborsClassifier()
knnclf = knnclf.fit(X_train,y_train)
knn_pred = knnclf.predict(X_train)
knnRMSE=((knn_pred - y_train) ** 2).mean() ** .5

from sklearn.linear_model import LogisticRegression
logclf = LogisticRegression(random_state=0)
logclf = logclf.fit(X_train,y_train)
log_pred = logclf.predict(X_train)
logRMSE=((log_pred - y_train) ** 2).mean() ** .5

from sklearn import svm
svmclf = svm.SVC(kernel='linear')
svmclf = svmclf.fit(X_train,y_train)
svm_pred = svmclf.predict(X_train)
svmRMSE=((svm_pred - y_train) ** 2).mean() ** .5

from sklearn.ensemble import RandomForestClassifier
rfclf = RandomForestClassifier(n_estimators=100, max_depth=13, random_state=41)
rfclf = rfclf.fit(X_train,y_train)
rf_pred = rfclf.predict(X_train)
rfRMSE=((rf_pred - y_train) ** 2).mean() ** .5

from sklearn.neural_network import MLPClassifier
mlpclf = MLPClassifier(random_state=41, max_iter=10,alpha = 1e-4,hidden_layer_sizes = (50,50),verbose = True)
mlpclf = mlpclf.fit(X_train,y_train)
mlp_pred = mlpclf.predict(X_train)
mlpRMSE=((mlp_pred - y_train) ** 2).mean() ** .5


print('Decision Tree RMSE:',((y_pred - y_train) ** 2).mean() ** .5)
print('Linear Regression RMSE:',linearRMSE)
print('Logistic Regression RMSE:',logRMSE)
print('KNN RMSE:',knnRMSE)
print('svm RMSE:',svmRMSE)
print('random forest RMSE:',rfRMSE)
print('Neural Network RMSE:',mlpRMSE)