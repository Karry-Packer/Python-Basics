car = {
    "brand": "Tata Motors",
    "model": "Nexon",
    "year": 2020,
    "color": "Red",
}

for key in car:
    print(f"Key: {key}, Value: {car[key]}")

for key, value in car.items():
    print(f"Key: {key}, Value: {value}")    

for key in car.keys():
    print(f"Key: {key}")    