import pandas as pd

ireland_df=pd.read_csv("dataset/PPR-ALL.csv",encoding='gbk')

def getDF():
    return ireland_df

def queryDate(date,df):
    result=df[df['Date of Sale (dd/mm/yyyy)']==date]
    return result

def queryCounty(county,df):
    result=df[df['County']==county]
    return result

def convertDfList(df):
    return df.values.tolist()

#ireland_df['Date of Sale (dd/mm/yyyy)']=='04/01/2010'

if __name__=='__main__':
    print("hello world")
