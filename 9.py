import requests

url = "https://petstore.swagger.io/v2/store/inventory"

print("Fetching pet store inventory...")

response = requests.get(url)
data = response.json()

print("Pet Store Inventory:")
for status, count in data.items():
    print(f"{status.capitalize()}: {count} pets")
    