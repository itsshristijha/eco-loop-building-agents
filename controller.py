from energyplus_wrapper import simulate
from agent import decide

def run_controller():

    data = simulate()

    # AI Recommendation
    action = decide(data)

    # Comfort Score
    comfort_score = 100

    if data["temperature"] < 20 or data["temperature"] > 26:
        comfort_score -= 10

    if data["humidity"] < 35 or data["humidity"] > 60:
        comfort_score -= 5

    if data["energy"] > 220:
        comfort_score -= 10

    # Building Status
    if comfort_score >= 90:
        building_status = "Healthy"
    elif comfort_score >= 75:
        building_status = "Warning"
    else:
        building_status = "Critical"

    # Estimated Energy Savings
    energy_savings = round(max(0, (250 - data["energy"]) / 250 * 100), 1)

    # Estimated CO₂ Saved
    co2_saved = round(energy_savings * 2.6, 1)

    # AI Reasoning
    reasoning = (
        f"Temperature is {data['temperature']}°C, "
        f"Humidity is {data['humidity']}%, "
        f"Occupancy is {data['occupancy']}. "
        f"Energy usage is {data['energy']} kWh. "
        f"The AI recommends: {action}"
    )

    data.update({
        "action": action,
        "comfort_score": comfort_score,
        "building_status": building_status,
        "energy_savings": energy_savings,
        "co2_saved": co2_saved,
        "reasoning": reasoning
    })

    return data