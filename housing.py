# Importing necessary libraries
import numpy as np
import pickle
import pandas as pd
import catboost
from catboost import CatBoostRegressor
import streamlit as st 

from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_california_house_price(house_age, total_rooms, total_bedrooms, population, households, median_income):
  
    """
    **housingMedianAge:** Median age of a house within a block; a lower number is a newer building
    **totalRooms:** Total number of rooms within a block
    **totalBedrooms:** Total number of bedrooms within a block
    **population:** Total number of people residing within a block
    **households:** Total number of households, a group of people residing within a home unit, for a block

    """

    prediction = classifier.predict([[house_age, total_rooms, total_bedrooms, population, households, median_income]])


    print(prediction)
    return prediction



def main():
    st.title("California House Price Prediction App")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit House Prices Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    house_age = st.text_input("House Age","Type Here")
    total_rooms = st.text_input("Total Rooms","Type Here")
    total_bedrooms = st.text_input("Total Bedrooms","Type Here")
    population = st.text_input("Population","Type Here")
    households = st.text_input("Households","Type Here")
    median_income = st.text_input("Median Income","Type Here")
    
    result=""
    if st.button("Predict"):
        result = predict_california_house_price(house_age, total_rooms, total_bedrooms, population, households, median_income)
        formatted_result = "${:.4f}".format(result.item())
        st.success('The Prediction Price Based on your Requirement is {}'.format(formatted_result))


    if st.button("About"):
        st.text(" House Price Prediction")
        st.text(" The Team")
        st.text("""
            1. Mohamed Ali Ibrahim, Group Leader who bulding the system
            2. Juwayriya Mohamed Hassan text book with 
            3. Hassan Abdi Mohamed assisant juwriya
            4. Bian Abdullahi Said assisanat with mohamed
         
        

            Variable descrpition:

            longitude: A measure of how far west a house is; a higher value is farther west.

            latitude: A measure of how far north a house is; a higher value is farther north.

            housingMedianAge: Median age of a house within a block; a lower number is a newer building.

            totalRooms: Total number of rooms within a block.

            totalBedrooms: Total number of bedrooms within a block.

            population: Total number of people residing within a block.

            households: Total number of households, a group of people residing within a home unit, for a block.

            medianIncome: Median income for households within a block of houses (measured in tens of thousands of US Dollars).

            medianHouseValue: Median house value for households within a block (measured in US Dollars).

            oceanProximity: Location of the house w.r.t ocean/sea.
            
                """)
        if choices=='Predicted House':
    #st.subheader("Predicted House")
    st.info("expand to see data clearly")
    if os.path.exists("db.csv"):
        data = pd.read_csv('db.csv')
        st.write(data)
    else:
        st.error("please try some prediction, then the data will be available here")
if choices=='About':
    st.subheader("About Us")
    info='''
        A house value is simply more than location and square footage. Like the features that make up a person, an educated party would want to know all aspects that give a house its value.

        We are going to take advantage of all of the feature variables available to use and use it to analyze and predict house prices.

        We are going to break everything into logical steps that allow us to ensure the cleanest, most realistic data for our model to make accurate predictions from.

        - Load Data and Packages
        - Analyzing the Test Variable (Sale Price)
        - Multivariable Analysis
        - Impute Missing Data and Clean Data
        - Feature Transformation/Engineering
        - Modeling and Predictions
    '''
    st.markdown(info,unsafe_allow_html=True)

if choices=='Visual':
    st.subheader("Data Visualization")      

    train_data = load_train_data(train_path)
    test_data = load_test_data(test_path)


    if st.checkbox("view dataset colum description"):
        st.subheader('displaying the column wise stats for the dataset')
        st.write(train_data.columns)
        st.write(train_data.describe())

    st.subheader('Correlation b/w dataset columns')
    corrmatrix = train_data.corr()
    f,ax = plt.subplots(figsize=(20,9))
    sns.heatmap(corrmatrix,vmax = .8, annot=True)
    st.pyplot()

    st.subheader("most correlated features")
    top_corr = train_data.corr()
    top_corr_feat = corrmatrix.index[abs(corrmatrix['SalePrice'])>.5]
    plt.figure(figsize=(10,10))
    sns.heatmap(train_data[top_corr_feat].corr(), annot=True, cmap="RdYlGn")
    st.pyplot()

    st.subheader("Comparing Overall Quality vs Sale Price")
    sns.barplot(train_data.OverallQual, train_data.SalePrice)
    st.pyplot()

    st.subheader("Pairplot visualization to describe correlation easily")
    sns.set()
    cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
    sns.pairplot(train_data[cols], size=2.5)
    st.pyplot()

    st.subheader("Analyis of Sale Price column in dataset")
    sns.distplot(train_data['SalePrice'] , fit=norm)# Get the fitted parameters used by the function
    (mu, sigma) = norm.fit(train_data['SalePrice'])
    st.write( '\n mu = {:.2f} and sigma = {:.2f}\n'.format(mu, sigma))

    plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu, sigma)], loc='best')
    plt.ylabel('Frequency')
    plt.title('SalePrice distribution')
    st.pyplot()

    fig = plt.figure(figsize=(10,10))
    res = stats.probplot(train_data['SalePrice'], plot=plt,)
    st.pyplot()
      

              
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
  
