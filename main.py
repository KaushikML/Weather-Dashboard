import streamlit as st
from backend import get_data
import  plotly.express as px
st.title("Weather Forecast for the Next days")
place=st.text_input("Place: ")

days=st.slider("Forecast Days",min_value=1,max_value=5,help="select the number of forecasted days")

option=st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next{days} days in {place}")

if place:
    try:
        filtered=get_data(place,days)
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered]
            dates=[dict["dt_txt"] for dict in filtered]
            figure=px.line(x=dates,y=temperatures,labels={"x":"Dates","y":"Temperatures(C)"})
            st.plotly_chart(figure)


        if option=="Sky":
            images={"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png","Snow":"images/snow.png"}

            sky_condition=[dict["weather"][0]["main"]for dict in filtered]
            image_paths=[images[condition] for condition in sky_condition]
            print(sky_condition)
            st.image(image_paths,width=115)
    except KeyError:
        st.write("Enter a correct place and check spellings.")