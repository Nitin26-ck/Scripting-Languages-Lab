"""a)Load the ‘Black Friday’ dataset into one of the data structures (NumPy or Pandas).\n",
    "b)Display header rows and description of the loaded dataset.\n",
    """
import pandas as pd
import numpy as np

df = pd.read_csv("blackfri.csv")
print(\"<-----Data Information----->\")
print("Head of Dataset")
print(df.head(5))
print("Head of Dataset")
print(df.describe())
print(df.info())

"""c) Remove unnecessary features (E.g. drop unwanted columns) from the dataset such as ‘User_ID’, ‘Product_ID ‘ ‘Stay_In_Current_City_Years’"""
df.drop(['User_ID','Product_ID','Stay_In_Current_City_Years'], axis=1, inplace=True)
print(df.head(5))
   
"""d) Manipulate data by replacing empty column values in ‘City_Category’ with a default value for the city. """
print("Filling empty values")
df['City_Category'] = df['City_Category'].fillna(\"A\")
print(df.head(5))

"""e) Convert the attribute ‘City_Category’ to have ‘A’ to be ‘Metro Cities’, ‘B’ to be ‘Small Towns’ ,  ‘C’ to be ‘Villages’."""
print("Mapping values/attributes in City_Category to types")
df['City_Category'] = df['City_Category'].map({'A':'Metro cities','B':'Small Towns','C':'Villages'})
print(df.head(5))

"""f) Rename the attribute ‘Product_Category_1’ to have ‘Baseball Caps’, \n",
    "‘Product_Category_2’ to have ‘Wine Tumblers’ and ‘Product_Category_3’ to \n",
    "have ‘Pet Raincoats’\n",
    """
print("Renaming the column names")
df.rename(columns={'Product_Category_1':'Baseball_Caps','Product_Category_2':'Wine_Tumblers','Product_Category_3':'Pet_Raincoats'},inplace=True)
print(df.head(5))

"""g) Convert the attribute ‘Marital_Status’ to have ‘1:Married’ and ‘0:Un-Married’\n","""
print("Mapping values/attributes in Marital Status to types")
df['Marital_Status'] = df['Marital_Status'].map({1:'Married',0:'Un-Married'})
print(df.head(5))

"""h) Perform the following visualizations on the loaded dataset:\n",
    "i)   Tally of the Number of Male & Female who bought ‘Product_Category_3(Pet_Raincoats)’. \n",
    """
import matplotlib.pyplot as plt
import seaborn as sns
print("<-------Data Visualisation------->")
print(pd.crosstab(df.Gender,df.Baseball_Caps))
print(pd.crosstab(df.Gender,df.Pet_Raincoats))

ax = sns.countplot(data=df,x='Gender',hue='Pet_Raincoats',palette='Set2')
ax.set(title='Male and Female who bought Pet_Raincoats',xlabel='Gender',ylabel='Count')
plt.show()


"""h) Perform the following visualizations on the loaded dataset:\n",
    "ii)  Total Number of Male & Female persons belonging to each city category\n",
    """
ax = sns.countplot(data=df,x='Gender',hue='City_Category',palette='Set1')
ax.set(title='Male and Female belonging to each city',xlabel='Gender',ylabel='Count')
plt.show()
