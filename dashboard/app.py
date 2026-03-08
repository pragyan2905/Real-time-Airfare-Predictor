import streamlit as st
import requests

st.set_page_config(page_title="Flight Price Prediction")

st.title("Flight Price Prediction")

# Inputs

stops = st.slider("Stops", 0, 3, 1)

days_until_departure = st.slider(
    "Days Until Departure",
    1,
    180,
    30
)

route_avg_price = st.number_input(
    "Route Average Price",
    value=240.0
)

route_price_std = st.number_input(
    "Route Price Std",
    value=20.0
)

airline_frequency = st.slider(
    "Airline Frequency",
    1,
    20,
    5
)


# Prediction button

if st.button("Predict Price"):

    payload = {
        "stops": stops,
        "days_until_departure": days_until_departure,
        "route_avg_price": route_avg_price,
        "route_price_std": route_price_std,
        "airline_frequency": airline_frequency
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload,
            timeout=10
        )

        prediction = response.json()

        st.success(
            f"Predicted Price: ${round(prediction['predicted_price'],2)}"
        )

    except Exception as e:

        st.error(f"Error connecting to API: {e}")