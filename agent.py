def recommend_hvac(temp, humidity, occupancy, energy):
    if temp > 26:
        action = "Decrease Cooling Setpoint to 22°C"
    elif temp < 20:
        action = "Increase Heating Setpoint to 24°C"
    else:
        action = "Maintain Current HVAC Settings"

    return {
        "temperature": temp,
        "humidity": humidity,
        "occupancy": occupancy,
        "energy": energy,
        "action": action
    }