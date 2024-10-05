import streamlit as st  
import requests  

# Function to get geolocation from IP  
def get_geolocation(ip_address):  
    try:  
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')  
        if response.status_code == 200:  
            data = response.json()  
            lat = data.get('latitude')  
            lon = data.get('longitude')  
            return lat, lon, data.get('city'), data.get('region'), data.get('country')  
        else:  
            return None, None, None, None, None  
    except Exception as e:  
        st.error(f"An error occurred: {e}")  
        return None, None, None, None, None  

# Streamlit UI  
st.markdown('<div class="title"> GEOLOCATION TRACKER </div>', unsafe_allow_html=True)  

# Start of form1  
form1 = st.form("Input GEOLOCATION TRACKER")  
form1.markdown("""  
    <div class="form1-wrapper">  
        <div class="subheader"> Please enter this IP : </div>  
        <div class="input-field">  
            """, unsafe_allow_html=True)  
feature = form1.text_input(" ", key='IP_')  
form1.markdown("</div></div>", unsafe_allow_html=True)  # Closing input-field div  
predict_button = form1.form_submit_button("Search")  

# CSS styles  
form1.markdown("""  
    <style>  
    body {  
        background-color: black;  /* Main background color */  
        color: white;  /* Default text color */  
    }  
    .form1-wrapper {  
        background-color: #87CEEB; /* Sky Blue background for form1 */  
        padding: 20px;  
        border-radius: 8px;  
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);  
    }  
    .title {  
        font-size: 36px;  
        font-weight: bold;  
        color: #228B22;  /* Forest Green for the title */  
    }  
    .subheader {  
        font-size: 20px;  
        color: #8B4513;  /* Brown color for form1 text */  
    }  
    .input-field {  
        margin: 10px 0;  
    }  
    .stButton > button {  
        background-color: gray;  /* Gray background color for the button */  
        color: white;  /* White text for the button */  
        padding: 10px;  
        border-radius: 5px;  
    }  
    .stButton > button:hover {  
        background-color: red;  /* Red on hover */  
    }  
    </style>  
""", unsafe_allow_html=True)  

# If the button is clicked, get the geolocation  
if predict_button:  
    lat, lon, city, region, country = get_geolocation(feature)  

    if lat is not None and lon is not None:  
        # Show the location on the map  
        st.success("IP Address: {}".format(feature))  
        st.write("Location: {}, {}, {}".format(city, region, country))  

        # Display the map  
        st.map(data={  
            'lat': [lat],  
            'lon': [lon]  
        })  
    else:  
        st.error("Could not fetch geolocation data.")