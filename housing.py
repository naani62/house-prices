import streamlit as st
st.title("housr prices prdection")

st.write("You have entered", st.session_state["my_input"])




import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)
    import streamlit as st






# Importing necessary libraries
import numpy as np
import pickle
import pandas as pd
import catboost
from catboost import CatBoostRegressor
import streamlit as st 

from PIL import Image
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
    st.title("California House Price Prediction using machine learning")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit House Prices Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    longitude = st.text_input("longitude","Enter longitude")
    latitude = st.text_input("latitude","Enter latitude")
    house_age = st.text_input("House Age","Enter house_age")
    total_rooms = st.text_input("Total Rooms","Enter total_rooms")
    total_bedrooms = st.text_input("Total Bedrooms","Enter total_bedrooms")
    population = st.text_input("Population","Enter population")
    households = st.text_input("Households","Enter households")
    median_income = st.text_input("Median Income","Enter median_income")
    median_house_value = st.text_input(" median_house_value","Enter median_house_value")
    ocean_proximity = st.text_input(" ocean_proximity","Enter ocean_proximity")
   
    
    result=""
    if st.button("Predict"):
        result = predict_california_house_price(house_age, total_rooms, total_bedrooms, population, households, median_income)
        formatted_result = "${:.4f}".format(result.item())
        st.success('The Prediction Price Based on your Requirement is {}'.format(formatted_result))
    st.title("House Pricing  prdection using machine learning Analysis")


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

              
        st.text("Built with mohamed ali using Streamlit")
     
    
       

if __name__=='__main__':
    main()
   

def main():
    st.title("Our Team's Work")

    # Load the images
    image1 = Image.open("download.jpg")
    
    image2 = Image.open("download.jpg")
   
    image3 = Image.open("download.jpg")
  

    # Display the images with captions
    st.image(image1, caption="Work 1", use_column_width=True)
    st.image(image2, caption="Work 2", use_column_width=True)
    st.image(image3, caption="Work 3", use_column_width=True)

    # Add some text about the team
    st.header("Meet Our Team")
    st.write("We are a group of friends who love to work together on various projects. Our team consists of:")
    st.write("- John: Project Manager")
    st.write("- Jane: Designer")
    st.write("- Bob: Developer")
    st.write("- Sarah: Content Creator")
    st.write("- Tom: QA Tester")

    # Add a group photo
    group_photo = Image.open("download.jpg")
    st.image(group_photo, caption="Our Team Photo", use_column_width=True)

if __name__ == "__main__":
    main()





