import random

def get_building_data():
    return {
        "temperature": round(random.uniform(20, 32), 2),
        "humidity": round(random.uniform(35, 70), 2),
        "occupancy": random.randint(1, 50),
        "energy": round(random.uniform(100, 400), 2)
    }