import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('students_data.xlsx')
print(df)
# print(df.at[0,'Age'])
# print(df.index)
# print(df.columns)
# print(df.dtypes)
# print(df.iat[7,4])
# print(df.iloc[7,4])
# print(df.loc[0])
# data=pd.DataFrame({'english':[98,59,65,48,21,75,60,80,94,55,40,57]})
# print(data)
# newfile=pd.concat((df,data),axis=1)
# print(newfile)
# print('#'*90)

# print(newfile.size)
# print('#'*90)

# print(newfile.T)
# print('#'*90)
# print(newfile.empty)
# print('#'*90)
# print(newfile.isna())
# print('#'*90)
# print(newfile.head(2))
# print('#'*90)
# print(newfile.tail(2))
# print('#'*90)
# df=newfile.isnull()
# print(df)
# print('#'*90)
# df=newfile.isnull().sum()
# print(df)

# print('#'*90)
# print(newfile.iat[0,5])
# print('#'*90)
# df=newfile.dropna(how='any')
# print(df) 
# print('#'*90)

# df=newfile.fillna({'Name':'Adham','Statistics':90})
# print(df)
# print('#'*90)

# df=newfile.sort_values(by='Age').reset_index(drop=True)
# print(df) 
# print('#'*90)
# print(newfile[(newfile['Department']=='Computer Science') &(newfile['Python'] >80)])
# print('#'*90)
# subjects = ['Python', 'Database', 'Statistics', 'Programming', 'english']
# df['Status']=np.where((df[subjects]>=50).all(axis=1),'passed','faild')
# print(df)
# print('#'*90)

# df['congratulations']=np.where((df['Status']=='passed'),'congrats','sorry')
# print(df)
# print('#'*90)

# print(df.groupby('Department')['Age'].mean())


# print(df.groupby('Department')['Age'].describe())
# df_melted=df.melt(
#                  id_vars='Name',

#                   value_vars=['Python','Database','Statistics','Programming','english'],
#                    var_name='subject',

#                    value_name='marks' ,
#                    ignore_index=True

#                     )
# print(df_melted)

# df_poved=df_melted.pivot(index='Name',
#                          columns='subject',

#                   values='marks'
#                   )
# print(df_poved)
# sales=[10,30,6,80,4,6]
# df=pd.DataFrame({'str_date':['2026/2/4','2026/7/5','2026/10/9','2026/3/10','2026/4/6','2026/6/5'],'sales':sales})
# print(df)
# df['date']=pd.to_datetime(df['str_date'])
# print(df)
# df['year']=df['date'].dt.year

# df['month']=df['date'].dt.month
# df['day']=df['date'].dt.day
# print(df)
# df.set_index('date',inplace=True)
# monthly_sales=df.resample('ME').sum()
# print(monthly_sales)
# print(df['sales'].sum())
# print('*'*90)
# feb_mar_sales=df[(df['month']>=2)& (df['month']<=3)]['sales'].sum()
# print(feb_mar_sales)
# name=df.sort_values(by='Name',ascending=True)

# print(name)
st.write("Hello Adham")
st.title('Student Performance & Academic Analytics Dashboard')
st.header('📊 Dataset Overview')
# st.subheader('The Sub')
st.markdown('An interactive overview analyzing student grade distribution, course performance, and academic metrics.')
st.dataframe(df)

plt.bar(df['Name'],df['Final Exam'])
plt.title('Final Exam Gradse')

plt.xlabel('Name')
plt.ylabel('Final Exam')
plt.xticks(rotation=35)
plt.yticks(rotation=90)

st.pyplot(plt)
plt.figure()
plt.scatter(df['Name'],df['Final Exam'],colors='r')
plt.title('Final Exam Gradse')
plt.xlabel('Name')
plt.ylabel('Final Exam')
plt.xticks(rotation=35)
plt.yticks(rotation=90)
st.pyplot(plt)
plt.figure()
p=df['Department'].value_counts()
plt.pie(p,labels=p.index,autopct='%1.1f%%')
plt.title('Department Percentage')
st.pyplot(plt)

