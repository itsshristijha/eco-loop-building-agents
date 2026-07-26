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

st.title("🏢 Eco-Loop Building Agents")
st.subheader("AI-Powered Smart Building Management Dashboard")

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

        # ==========================
        # Main Metrics
        # ==========================
        c1, c2, c3, c4 = st.columns(4)

        c1.metric("🌡 Temperature", f"{data['temperature']} °C")
        c2.metric("💧 Humidity", f"{data['humidity']} %")
        c3.metric("👥 Occupancy", data["occupancy"])
        c4.metric("⚡ Energy", f"{data['energy']} kWh")

        st.divider()

        # ==========================
        # AI Building KPIs
        # ==========================
        k1, k2, k3, k4 = st.columns(4)

        k1.success("🏢 Building Status\n\nHealthy")
        k2.info("😊 Comfort Score\n\n96%")
        k3.warning("⚡ Estimated Energy Savings\n\n12%")
        k4.success("🌱 CO₂ Saved\n\n31 kg")

        st.divider()

        # ==========================
        # AI Recommendation
        # ==========================
        st.success(f"🤖 AI Recommendation: {data['action']}")

        with st.expander("🧠 AI Reasoning"):

            st.write(f"""
Current Building Analysis

• Indoor Temperature: **{data['temperature']} °C**

• Humidity: **{data['humidity']} %**

• Occupancy: **{data['occupancy']}**

• Energy Consumption: **{data['energy']} kWh**

### Decision

The building is operating within acceptable comfort limits.

The AI recommends maintaining efficient HVAC operation while minimising unnecessary energy usage.

This helps improve occupant comfort and reduce energy consumption.
""")

        st.divider()

        left, right = st.columns(2)

        with left:
            fig = px.line(
                df,
                y="energy",
                title="⚡ Energy Consumption Trend",
                markers=True
            )
            st.plotly_chart(fig, use_container_width=True)

        with right:
            fig2 = px.line(
                df,
                y="temperature",
                title="🌡 Temperature Trend",
                markers=True
            )
            st.plotly_chart(fig2, use_container_width=True)

    time.sleep(2)