#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install geopy
import geopy
#dir(geopy)
from geopy.geocoders import Nominatim
nom = Nominatim()
x = nom.geocode("3995 23rd St, San Francisco, CA 94114")
print(x.latitude)
print(x.longitude)


# What we just saw along is a simple Example 
# But in real we need to geocode a bit decent amount of data
# So we would be dealing a little bit With Pandas.. and Csv Files


# In[2]:


import pandas
df = pandas.read_csv("D:\\Studies\\SSIP Hackathon\\geocoding\\ADDRESS Test\\ExcatAdd.csv")
df

# We are just opening our CSV file 


# In[3]:


df["Address"] = df["Address"] + ", "+ df["City"] +", " + df["State"] + ", " + df["Country"]
df

# In order to get a complete address as prescribed in the above example
# We would be concatenating few columns to get the complete Address




# In[4]:


df["Coordinates"] = df["Address"].apply(nom.geocode)
df
# We are just applying the same procedures of geocode onto those addresses


# In[5]:


df["Latitude"]= df["Coordinates"].apply(lambda x: x.latitude if x!= None else None)
df

# Finding Latitude Work on Co-ordinates


# In[6]:


df["Longitude"]= df["Coordinates"].apply(lambda x: x.longitude if x!= None else None)
df


# In[7]:


from pandas import DataFrame
export_csv = df.to_csv(r"D:\\Studies\\SSIP Hackathon\\geocoding\\ADDRESS Test\\ExcatAdd.csv",index = False)


# In[9]:


import pandas
df = pandas.read_csv("D:\\Studies\\SSIP Hackathon\\geocoding\\ADDRESS Test\\ExcatAdd.csv")
import gmplot


latitudes = df.loc[:, 'Latitude']
#print(latitudes)
longitudes = df.loc[:, 'Longitude']
states = df['State']
unique_states = states.unique()
names = df['Address']
min_latitude = latitudes.min()
max_latitude = latitudes.max()
min_longitude = longitudes.min()
max_longitude = longitudes.max()

 

gmap = gmplot.GoogleMapPlotter(37, -122, 8)
gmap.coloricon="http://www.googlemapsmarkers.com/v1/%s/"
for i in range(7):
    lat = latitudes[i];
    long = longitudes[i];
    gmap.marker(lat, long,'red')
gmap.draw('D:\\Studies\\SSIP Hackathon\\geocoding\\ADDRESS Test\\map3.html')


# In[ ]:




