from energyplus_wrapper import get_building_data
from agent import recommend_hvac

def run_controller():
    data = get_building_data()
    return recommend_hvac(
        data["temperature"],
        data["humidity"],
        data["occupancy"],
        data["energy"]
    )