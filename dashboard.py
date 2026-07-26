import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import time

st.set_page_config(
    page_title="Eco Loop Building Agents",
    page_icon="🏢",
    layout="wide"
)

st.title("🏢 Eco Loop Building Agents")
st.subheader("AI Powered Smart Building Dashboard")

placeholder = st.empty()

history = []

while True:

    response = requests.get("http://127.0.0.1:8000/simulate")

    data = response.json()

    history.append(data)

    if len(history) > 20:
        history.pop(0)

    df = pd.DataFrame(history)

    with placeholder.container():

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("🌡 Temperature", f"{data['temperature']} °C")
        c2.metric("💧 Humidity", f"{data['humidity']} %")
        c3.metric("👥 Occupancy", data["occupancy"])
        c4.metric("⚡ Energy", f"{data['energy']} kWh")

        st.success(f"🤖 AI Recommendation: {data['action']}")

        fig = px.line(
            df,
            y="energy",
            title="Energy Consumption"
        )

        st.plotly_chart(fig, use_container_width=True)

        fig2 = px.line(
            df,
            y="temperature",
            title="Temperature Trend"
        )

        st.plotly_chart(fig2, use_container_width=True)

    time.sleep(2)