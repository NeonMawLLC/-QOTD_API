import requests
import datetime

# Citadel Siphon: Simple Data Retrieval
# Purpose: Fetch public metadata and archive locally.

def siphon_data():
    url = "https://api.quotable.io/random" # Public API node
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            entry = f"[{datetime.datetime.now()}] {data['author']}: {data['content']}\n"
            
            with open("siphon_log.txt", "a") as f:
                f.write(entry)
            print("Data siphoned successfully.")
    except Exception as e:
        print(f"Siphon Error: {e}")

if __name__ == "__main__":
    siphon_data()
