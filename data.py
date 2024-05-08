import random
from datetime import datetime, timedelta
import json

# Generate random date within a range
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

# Generate random data
def generate_data(size):
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 2, 19)
    
    data = {
        "Date": [],
        "Temperature": [],
        "Humidity": [],
        "NDVI": []
    }
    
    for _ in range(size):
        data["Date"].append(random_date(start_date, end_date))
        data["Temperature"].append(random.randint(20, 30))  # Random temperature between 20 and 30
        data["Humidity"].append(random.randint(40, 60))     # Random humidity between 40 and 60
        data["NDVI"].append(round(random.uniform(0.6, 0.9), 2))  # Random NDVI between 0.6 and 0.9
    
    return data

generated_data = generate_data(50)  # Change 10 to the desired size of your dataset
print(json.dumps(generated_data, indent=2))
