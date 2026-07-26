def decide(data):
    
    temp = data["temperature"]
    humidity = data["humidity"]
    occupancy = data["occupancy"]
    energy = data["energy"]

    # High temperature
    if temp > 27:
        return "Decrease Cooling Setpoint to 22°C"

    # Low temperature
    elif temp < 20:
        return "Increase Heating Setpoint to 24°C"

    # High occupancy
    elif occupancy > 80:
        return "Increase Ventilation and Fresh Air Supply"

    # High humidity
    elif humidity > 65:
        return "Enable Dehumidification Mode"

    # Low humidity
    elif humidity < 30:
        return "Enable Humidification Mode"

    # High energy usage
    elif energy > 220:
        return "Reduce HVAC Fan Speed to Save Energy"

    # Low occupancy and moderate temperature
    elif occupancy < 20 and 22 <= temp <= 25:
        return "Enable Energy Saving Mode"

    else:
        return "Maintain Current HVAC Settings"