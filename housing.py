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
    
    
  

#<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Boston Housing Prediction - Regression</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>




<style type="text/css">
    pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: var(--jp-cell-editor-active-background) }
.highlight { background: var(--jp-cell-editor-background); color: var(--jp-mirror-editor-variable-color) }
.highlight .c { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment */
.highlight .err { color: var(--jp-mirror-editor-error-color) } /* Error */
.highlight .k { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword */
.highlight .o { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator */
.highlight .p { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation */
.highlight .ch { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Multiline */
.highlight .cp { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Preproc */
.highlight .cpf { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Single */
.highlight .cs { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Special */
.highlight .kc { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Pseudo */
.highlight .kr { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Type */
.highlight .m { color: var(--jp-mirror-editor-number-color) } /* Literal.Number */
.highlight .s { color: var(--jp-mirror-editor-string-color) } /* Literal.String */
.highlight .ow { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator.Word */
.highlight .w { color: var(--jp-mirror-editor-variable-color) } /* Text.Whitespace */
.highlight .mb { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Bin */
.highlight .mf { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Float */
.highlight .mh { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Hex */
.highlight .mi { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer */
.highlight .mo { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Oct */
.highlight .sa { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Affix */
.highlight .sb { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Backtick */
.highlight .sc { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Char */
.highlight .dl { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Delimiter */
.highlight .sd { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Doc */
.highlight .s2 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Double */
.highlight .se { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Escape */
.highlight .sh { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Heredoc */
.highlight .si { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Interpol */
.highlight .sx { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Other */
.highlight .sr { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Regex */
.highlight .s1 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Single */
.highlight .ss { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Symbol */
.highlight .il { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer.Long */
  </style>



<style type="text/css">
