import streamlit as st
import folium
from streamlit_folium import st_folium, folium_static
from folium.plugins import Geocoder

st.markdown("<h1 style='text-align: center; color: orange;'>MyTree App🌲</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: green;'>Calculator</h2>", unsafe_allow_html=True)
st.markdown("""
Are you wondering how much carbon you've created?
Worry less! Just Calculate.
In this app, first we can calculate the carbon.
First, we have transportation calculator.
""")

# st.markdown("<h3 style='text-align: center; color: green;'>Transportation</h3>", unsafe_allow_html=True)

gco2e = {
    'motorcycle' : 86.1,
    'car' : 35.1,
    'taxi' : 39.6,
    'bus' : 15.6,
    'train' : 19.8,
    'mrt' : 34.6
}

transportations = st.selectbox(
    'So, let me know one transportation you are using today?',
    ('Motorcycle', 'Car', 'Taxi', 'Bus', 'Train', 'MRT'))
transportations = transportations.lower()

km = st.number_input('How long is that in kilometer?', step=1)

co2total = round(gco2e[transportations]*km, 1)

st.markdown(f"""
Oh no! You have been emitting <b>{co2total} gCO2e</b> so far.
Let now we plant something for you. Let take that <b>{co2total} gCO2e</b>
into a credit for us to plant something. <a href="http://dana.id" target="_blank">Open e-wallet</a>.
""", unsafe_allow_html=True)

# st.markdown("<h3 style='text-align: center; color: green;'>Electronics</h3>", unsafe_allow_html=True)

# st.markdown(f"""
# Wait. You wanna track your electronics too? worry free!
# """)

# gco2e_electronics = {
#     'motorcycle' : 86.1,
#     'car' : 35.1,
#     'taxi' : 39.6,
#     'bus' : 15.6,
#     'train' : 19.8,
#     'mrt' : 34.6
# }

# electronics = st.selectbox(
#     'So, let me know one transportation you are using today?',
#     ('Motorcycle', 'Car', 'Taxi', 'Bus', 'Train', 'MRT'))
# electronics = electronics.lower()

# hour = st.number_input('How long is that in hour?', step=1)

# co2total_electronics = round(gco2e_electronics[electronics]*hour, 1)

# st.markdown(f"""
# Oh no! You have been emitting <b>{co2total_electronics} gCO2e</b> so far in electronics.
# Let now we plant something for you. Let take that <b>{co2total} gCO2e</b>
# into a credit for us to plant something. <a href="http://dana.id" target="_blank">Open e-wallet</a>.
# """, unsafe_allow_html=True)


st.markdown("<h2 style='text-align: center; color: green;'>Choose where we could plant?</h2>", unsafe_allow_html=True)
st.markdown("""
You can choose where we wanna plant.
Why? Because sometimes we want tree to be planted 
right to our nearest village right, isn't it beautiful?
Don't worry! all your trees will be documented
and you can track the trees development.
""")

m = folium.Map()
region = Geocoder().add_to(m)
folium_static(m)