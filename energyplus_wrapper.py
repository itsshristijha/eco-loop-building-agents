import random

def simulate():

    temperature = round(random.uniform(21, 29), 2)
    humidity = round(random.uniform(40, 60), 2)
    occupancy = random.randint(5, 100)

    # Energy depends on occupancy
    energy = round(
        120 +
        occupancy * 1.4 +
        random.uniform(-10, 20),
        2
    )

    return {
        "temperature": temperature,
        "humidity": humidity,
        "occupancy": occupancy,
        "energy": energy
    }