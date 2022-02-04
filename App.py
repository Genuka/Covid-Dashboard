import pandas as pd
import streamlit as st
from libraries import *

st.markdown("<h1 style='text-align: center; color: white;'>COVID 19 DASHBOARD</h1>", unsafe_allow_html=True)
countries = ["Australia","China","India","Sri Lanka","USA","Singapore","Egypt","Russia","France",]
data_types = ["cases","deaths","recovered"]
flag_codes ={"Australia":"au","China":"cn","India":"in","Sri Lanka":"lk","USA":"us","Singapore":"sg","Egypt":"eg","Russia":"ru","France":"fr",} 


country = st.sidebar.selectbox('Select A Country',countries)


days = st.sidebar.slider('Select Number Of Days',min_value=2,max_value=100)

data_type = st.sidebar.multiselect('Pick Data Types',data_types)
cases_df = get_historic_cases(country,days)
deaths_df = get_historic_deaths(country,days)
recoveries_df = get_historic_recoveries(country,days)

historic_df = pd.concat([cases_df,deaths_df,recoveries_df],axis=1).astype(int)

daily_cases_df = get_daily_cases(country,days)  
daily_deaths_df = get_daily_deaths(country,days)
daily_recoveries_df = get_daily_recoveries(country,days)

daily_df = pd.concat([daily_cases_df,daily_deaths_df,daily_recoveries_df],axis=1).astype(int)


yesterday_cases_df = get_yesterday_cases(country)  
yesterday_deaths_df = get_yesterday_deaths(country)
yesterday_recoveries_df = get_yesterday_recoveries(country)

col4,col5 = st.columns(2)
col4.metric('Country',country)
col5.image(f"https://flagcdn.com/72x54/{flag_codes[country]}.png")
col1,col2,col3  = st.columns(3)
col1.metric('Total cases',yesterday_cases_df)
col2.metric('Total deaths',yesterday_deaths_df)
col3.metric('Total recoveries',yesterday_recoveries_df)

st.write(f"You have selected {days} days" )
st.line_chart(daily_df[data_type])
st.line_chart(daily_df[data_type])

st.write(historic_df)
st.write(daily_df)






st.title("What Is Coronavirus ?")
st.video(f"https://www.youtube.com/watch?v=sHP0UIdZyI4")
st.title("What should we do to prevent covid ?")
st.video(f"https://www.youtube.com/watch?v=6XdjmB4IY3M")


st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://ichef.bbci.co.uk/news/976/cpsprodpb/14A35/production/_115033548_gettyimages-1226314512.jpg")
    }
   .sidebar .sidebar-content {
        background: url("https://cwinc.org/wp-content/uploads/2020/03/COVID-19-Clipart.jpg")
    }
    .standard-text {font-size:50px;}
    .title-text {font-size:36px;}
    </style>
    """,
    unsafe_allow_html=True
)








st.image(
            "https://image.shutterstock.com/image-vector/stay-home-safe-social-media-600w-1692271513.jpg",
            width=700, # Manually Adjust the width of the image as per requirement
        )



st.markdown("<h4 style='text-align: center; color: white;'>YOU HAVE REACHED THE END</h4>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: yellow;'>THANK YOU !</h1>", unsafe_allow_html=True)
