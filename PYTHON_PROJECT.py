#!/usr/bin/env python
# coding: utf-8

# # PROJECT (by Prerna Gautam)
The california Dataset gives a description about the california housing data.This dataset was derived from the 1990 U.S. census.
and the dataset consists of following features:
1) longitude-The datatype is numerical and a continuous data    
2) latitude- The datatype is numerical and also is a continuous data
3) housing_median_age- Quantitative type-Discrete data
4) total_rooms- Quantitative type-Discrete data
5) total_bedrooms-Quantitative type-Discrete data
6) population- Quantitative type-Discrete data
7) households- Quantitative type-Discrete data
8) median_income-Quantitative type- Continuous data 
9) median_house_value-Quantitative type-Discrete data 
10) ocean_proximity-Quantitative type-Nominal data  
# In[35]:


#1. What is the average median income of the data set and check the distribution of data using appropriate plots. 
#Please explain the distribution of the plot.
import pandas as pd               #imported all the required libraries
import matplotlib.pyplot as plt   # pandas for data manipulation and matplotlib and seaborn for data visualisation
import seaborn as sns
datasets=pd.read_excel(r"C:\Users\lenovo\Downloads\housing+(1).xlsx") #loaded the dataset 
datasets.head(5)    #displayed the dataset


# In[36]:


datasets.describe()  # describe() function in Pandas is used to generate various summary statistics of a DataFrame or Series.


# In[34]:


#1. What is the average median income of the data set and check the distribution of data using appropriate plots. 
#Please explain the distribution of the plot.
avg_median=datasets["median_income"].median() #calculated the median 
print(f"The average median income is ",round(avg_median,2))
 #Histogram is used for seeing the distribution of numerical data.
datasets.hist(bins=30,figsize=(22,22))
plt.show()
sns.set()


# In[33]:


#2. Draw an appropriate plot to see the distribution of housing_median_age and explain your observations.

plt.hist(datasets["median_income"],color='m')
plt.grid("true")
plt.xlabel("count")
plt.ylabel("Median_Income")
plt.title("Distribution of Median_Income",color='brown',size=20)
plt.show()
#This shows that the data is right skewed 


# In[61]:


plt.figure(figsize=(10, 5))
plt.hist(datasets["housing_median_age"], bins=10, edgecolor='k')
plt.xlabel("Housing Median Age")
plt.ylabel("Frequency")
plt.title("Distribution of Housing Median Age")
plt.show()


# In[89]:


#3. Show with the help of visualization, how median_income and median_house_values are related?
datas=datasets.head(1000)    

import matplotlib.pyplot as plt

# Assuming you have a DataFrame named 'df' containing the data
df = datas # Replace 'your_dataframe' with the actual DataFrame containing the data

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['median_income'], df['median_house_value'], alpha=0.5,marker='p',edgecolor='blue',facecolor='red')
plt.title('Relationship between Median Income and Median House Value',
         fontname='Arial',fontsize=14, fontweight='bold', style='italic')
plt.xlabel('Median Income',fontname="Brush Script MT", fontsize=25)
plt.ylabel('Median House Value',fontname="Brush Script MT", fontsize=25)

# Show the plot
plt.show()




   

   
   
   
   


# In[95]:


#4 Create a data set by deleting the corresponding examples from the data set for which total_bedrooms are not available.
import pandas as pd
new_df=datasets.dropna(subset=["total_bedrooms"]) #dropna will help in deleting the desired dataset 
new_df


# In[91]:


import pandas as pd
new_df=datasets.dropna(subset=["total_bedrooms"])


# In[23]:


#4 Create a data set by deleting the corresponding examples from the data set for which total_bedrooms are not available.
import pandas as pd


# Create a new dataset with rows where 'total_bedrooms' are available
new_df = datasets.dropna(subset=["total_bedrooms"])

# Save the new dataset to a new Excel file if needed
new_df.to_excel("new_housing_dataset.xlsx", index=False)

# Display the first few rows of the new dataset
new_df.head(50)


# In[12]:


pd.isnull(new_df).sum()


# In[19]:


#5 Create a data set by filling the missing data with the mean value of the total_bedrooms in the original data set.

x=datasets["total_bedrooms"].mean()
# Fill missing values with the mean
datasets['total_bedrooms'].fillna(x, inplace=True)

# Save the new dataset to a new Excel file if needed
datasets.to_excel("new_housing_dataset_filled.xlsx", index=False)

# Display the first few rows of the new dataset
datasets.head(10)


# In[32]:


# 6 Write a programming construct (create a user defined function) to calculate the median value of the data set wherever
#required.
import pandas as pd
import numpy as np
def median_value(x):
       return new_df[x].median()
show=list(new_df.columns) 
shows=show[:-1]
for ele in shows:
    print(f'{ele} median is:',median_value(ele))
     


     







# In[107]:


# 7 Plot latitude versus longitude and explain your observations.

import matplotlib.pyplot as plt
import seaborn as sns
datasets=pd.read_excel(r"C:\Users\lenovo\Downloads\housing+(1).xlsx")
#datasets.head(5)

sns.scatterplot(x="longitude", y="latitude", data=datasets, marker='p', edgecolor='purple', facecolor='black')
plt.title("THE RELATIONSHIP BETWEEN LATITUDE AND LONGITUDE",color="brown",fontname='Franklin Gothic Medium', fontsize=18)
plt.show()


# In[42]:


#8 Create a data set for which the ocean_proximity is ‘Near ocean’.
datasets[datasets["ocean_proximity"]=="NEAR OCEAN"]


# In[108]:


#9 Find the mean and median of the median income for the data set created in question 8.

datasets   
mean=datasets["median_income"].mean()  # Calculated the mean of the Median_income
median=datasets["median_income"].median()   #Calculated the median of the Median_income
print("The Mean of the median_income is",round(mean,2))
print("The Median of the median_income is",round(median,2))


# In[109]:


# 10 Please create a new column named total_bedroom_size. If the total bedrooms is 10 or less, it should be quoted as small. If the total bedrooms is 11 or more but less than 1000, 
#it should be medium, otherwise it should be considered large.

# Define a function to categorize 'total_bedrooms' size
def categorize_bedroom_size(total_bedrooms):
    if total_bedrooms <= 10:
        return 'small'
    elif 11 <= total_bedrooms < 1000:
        return 'medium'
    else:
        return 'large'

# Apply the function to create the 'total_bedroom_size' column
datasets['total_bedroom_size'] = datasets['total_bedrooms'].apply(categorize_bedroom_size)

# Display the updated DataFrame
datasets  





# In[45]:


datasets=datasets.fillna({method:="bfill"})


# In[40]:


datasets.info()


# In[46]:


datasets = datasets.fillna(method='bfill')


# In[47]:


datasets


# In[ ]:




