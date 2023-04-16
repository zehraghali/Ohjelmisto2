import requests

# Prompt user to enter a TV series name
search_query = input("Enter the name of a TV series: ")

# Send request to TVMaze API
response = requests.get("https://api.tvmaze.com/search/shows", params={"q": search_query})

# Check if response is valid
if response.status_code != 200:
    print(f"Error: {response.status_code}")
    exit()

# Parse the response and display information in the console
results = response.json()
for result in results:
    show = result["show"]
    print(f"Name: {show['name']}")
    print(f"Type: {show['type']}")
    print(f"Language: {show['language']}")
    print(f"Summary: {show['summary']}")
    print("----------------------------")
