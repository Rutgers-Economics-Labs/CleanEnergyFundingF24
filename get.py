import requests
import json

with open("payload.txt", "r") as file:
    payload = file.read()

# Fetch the access token
def get_access_token():
    rest_url = "https://atlaspolicy.com/wp-json/wp/v2/powerbi/getToken"
    try:
        response = requests.get(rest_url)
        response.raise_for_status()
        access_token = response.text.replace('"', '')  # Clean up quotes
        return access_token
    except requests.exceptions.RequestException as e:
        print(f"Error fetching access token: {e}")
        return None

# Fetch data queries from Power BI
def get_data_queries(access_token, query_url):
    headers = {}

    with open("headers.txt", "r") as file:
        # read line by line
        # first line is the key, second line is the value
        key = file.readline().strip()[:-1]
        value = file.readline().strip()
        headers[key] = value

    try:
        response = requests.post(query_url, headers=headers, data=payload)
        print(response)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data queries: {e}")
        return None

# Main function
def main():
    # Step 1: Get Access Token
    access_token = get_access_token()
    if not access_token:
        print("Failed to retrieve access token.")
        return

    # Step 2: Define the query URL for Power BI
    query_url = "https://pbipeus22-eastus2.pbidedicated.windows.net/webapi/capacities/476E51DA-8F1B-4C51-9B6B-E48E5832ED65/workloads/QES/QueryExecutionService/automatic/public/query"

    # Step 3: Fetch the data
    data = get_data_queries(access_token, query_url)
    if data:
        # Step 4: Save JSON data to a file
        with open("powerbi_data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        print("Data queries saved to 'powerbi_data.json'.")
    else:
        print("Failed to fetch data queries.")

if __name__ == "__main__":
    main()
