import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('output.csv')

# Set page title
st.title('Car Price Analysis')

# Display the data
st.header('Dataset Overview')
st.dataframe(data)

# Show summary statistics
st.header('Summary Statistics')
st.write(data.describe())

# Filter data by age, fuel type, and transmission type
st.sidebar.header('Filter Options')
age_filter = st.sidebar.slider('Select Age Range', int(data['age'].min()), int(data['age'].max()), (10, 40))
fuel_filter = st.sidebar.multiselect('Select Fuel Type', data['fueltype'].unique(), default=data['fueltype'].unique())
transmission_filter = st.sidebar.selectbox('Select Transmission Type', ['All', 'Automatic', 'Manual'])

# Apply filters
filtered_data = data[(data['age'] >= age_filter[0]) & (data['age'] <= age_filter[1])]
if 'All' not in transmission_filter:
    is_automatic = 1 if transmission_filter == 'Automatic' else 0
    filtered_data = filtered_data[filtered_data['automatic'] == is_automatic]
filtered_data = filtered_data[filtered_data['fueltype'].isin(fuel_filter)]

# Display filtered data
st.header('Filtered Data')
st.write(filtered_data)

# Visualization - Scatter plot
st.header('Visualizations')
st.subheader('Price vs. Kilometers Driven')
fig, ax = plt.subplots()
sns.scatterplot(x='km', y='price', data=filtered_data, ax=ax)
plt.xlabel('Kilometers Driven')
plt.ylabel('Price')
plt.title('Price vs. Kilometers Driven')
st.pyplot(fig)

# Visualization - Histogram of Age
st.subheader('Distribution of Car Age')
fig, ax = plt.subplots()
sns.histplot(filtered_data['age'], bins=20, kde=True, ax=ax)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Car Age')
st.pyplot(fig)

# Display correlation heatmap
st.subheader('Correlation Heatmap')
fig, ax = plt.subplots()
sns.heatmap(filtered_data.corr(), annot=True, cmap='coolwarm', ax=ax)
plt.title('Correlation Heatmap')
st.pyplot(fig)


