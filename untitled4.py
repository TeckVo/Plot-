# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 13:59:02 2021

@author: Cu Chi
"""


import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import matplotlib.pyplot as plt
import csv
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     st.write("filename:", uploaded_file.name)
     st.write(bytes_data)
     
def load_data(nrows):
     data = pd.read_csv('C:/Users/Cu Chi/Dropbox/My PC (CuChi)/Desktop/Web-based GUI/Data_set/Discharging ESS.csv', nrows=nrows)
     return data
weekly_data = load_data(96)
df_1 = pd.DataFrame(weekly_data[:96],columns = ['ESS1','ESS2'],
                    index=pd.RangeIndex(100, name='x'))    
df_1 = df_1.reset_index().melt('x', var_name='ESS', value_name='y')
line_chart = alt.Chart(df_1).mark_line().encode(
    alt.X('x', title='Time slot [min]'),
    alt.Y('y', title='Discharging power [MW]'),
    color='ESS:N').properties(title='ESS scheduling')

st.altair_chart(line_chart)



#def base_load(nrows):
    #data = pd.read_csv('C:/Users/Cu Chi/Dropbox/My PC (CuChi)/Desktop/Web-based GUI/Data_set/Base load.csv', nrows=nrows)
    #return data
#load_demand = base_load (366)       
df = pd.DataFrame(weekly_data[:365],columns = ['Time [day]','Base_load [p.u]'])
c = alt.Chart(df).mark_line().encode(
     x='Time [day]', y='Base_load [p.u]', tooltip=['Time [day]', 'Base_load [p.u]'])
st.altair_chart(c, use_container_width=True)



def load_data(nrows):
     data = pd.read_csv('C:/Users/Cu Chi/Dropbox/My PC (CuChi)/Desktop/Web-based GUI/Data_set/Base load.csv', nrows=nrows)
     return data
weekly_data = load_data(365)
exampledata = np.array(weekly_data[1:],dtype=np.float64)               
xdata=exampledata[:,0]
ydata=exampledata[:,1]
fig, ax = plt.subplots()
plt.plot(xdata,ydata)
ax.set_xlabel("Time [day]")
ax.set_ylabel("Base load [p.u]")            
st.pyplot(fig)           

import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)





#with open ('C:/Users/Cu Chi/Dropbox/My PC (CuChi)/Desktop/Web-based GUI/Data_set/Base load.csv','r') as i:
    #rawdata = list(csv.reader(i,delimiter=","))
#exampledata=np.array(rawdata[1:],dtype=np.float64)  
#xdata=exampledata[:,0]
#ydata=exampledata[:,1]
#fig, ax = plt.subplots()
#plt.plot(xdata,ydata)
#ax.set_xlabel("Time [day]")
#ax.set_ylabel("Base load [p.u]")            
#st.pyplot(fig)           

            
















source = pd.DataFrame(np.cumsum(np.random.randn(100, 3), 0).round(2),
                    columns=['alcohol', 'beer', 'coke'], index=pd.RangeIndex(100, name='x'))
source = source.reset_index().melt('x', var_name='category', value_name='y')

line_chart = alt.Chart(source).mark_line(interpolate='basis').encode(
    alt.X('x', title='Year'),
    alt.Y('y', title='Amount in liters'),
    color='category:N'
).properties(
    title='Sales of consumer goods'
)

st.altair_chart(line_chart)