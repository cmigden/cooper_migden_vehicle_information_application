#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly_express as px
import altair as alt
import streamlit as st
import numpy as np

#import needed packages

#print(pd.__version__)
#print(px.__version__)
#this tells me the verions I am using so that I can add them to the requirements.txt page

# In[2]:

data = pd.read_csv('/Users/coopermigden/data_sets/vehicles_us (1).csv', encoding='utf-8')
#data = pd.read_csv('/Users/coopermigden/data_sets/vehicles_us (1).csv')
#Brings the data into the program


# In[3]:


#data.describe
#gives general information about the data and it shows how it looks


# In[4]:


#data.isna().sum()
#shows the amount of unknown values in each column


# In[5]:


columns_to_replace = ['model_year','cylinders','odometer','paint_color','is_4wd']
for column in columns_to_replace:
    data[column] = data[column].fillna('unknown')
#replaces all unknown values with the word unknown


# In[6]:


# In[7]:


data.isna().sum()
#check to see if the previous function worked


# In[8]:


data.duplicated().sum()
#to check if the data has any duplicates. There are no doubles


# In[9]:


data['model'].sort_values().unique()
#went through list of model names to check if any are spelled incorrectly. none are spelled incorrectly.


# In[10]:


#determins the titles of the columns. Columns are in the appropriate snake_case
#data.columns


# In[11]:


#to create a new csv file for the cleaned data
data.to_csv('cleaned_vehicles_us.csv', index = True)


# In[13]:


st.title('Car Sales Data')


# In[14]:


st.write(data.head())
#displays data table


# In[15]:


st.header('Interactive Scatterplot')


# In[16]:


def interactive_plot(data):
    x_axis_val = st.selectbox('Select X-Axis Value', options=data.columns)
    y_axis_val = st.selectbox('Select Y-Axis Value', options=data.columns)
    
    plot = px.scatter(data,x=x_axis_val,y=y_axis_val)
    st.plotly_chart(plot)
#This is a function that creates a scatterplot in which the user is able to choose the x and y axis based upon the columns in the data dataframe.


# In[17]:


interactive_plot(data)


# In[18]:


st.header('Interactive Histogram')


# In[19]:


st.header('Histogram Via Type of Car and Price')
color_opt=st.checkbox('Please select this checkbox if you want this graph to have color.')
color ='type' if color_opt else None
#determines if the graph has color

hist =px.histogram(data_frame=data,x='type',y='price',color=color)

st.plotly_chart(hist)
#This is a function that creates a histogram that looks at the type of car in this data set.


# Final conclusions
# -There is a direct correlation between the type of car andtotal sales. This is seen by the trucks havingg significantly higher sales then any other vehicle.
#The newer the model, the higher the price.
# the lower the odometer, the higher the price.
# -The better the condition the higher the price
#The less daus it was posted, the higher the price
#updated python system
