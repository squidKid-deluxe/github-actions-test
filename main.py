import requests

print("Fetching data...")

data = requests.get("https://example.com").text

print("Writing to file...")

with open("index.html", "w") as handle:
  handle.write(data)
  handle.close()
  
print("All done!")
