import pandas as pd

ireland_df=pd.read_csv("dataset/PPR-ALL.csv")

def queryDate(date):
    result=ireland_df[ireland_df['Date of Sale (dd/mm/yyyy)']==date]
    return result.values.tolist()


#ireland_df['Date of Sale (dd/mm/yyyy)']=='04/01/2010'