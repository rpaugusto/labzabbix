import requests
import json

# Grafana configuration
# Grafana server URL
GRAFANA_URL = 'http://192.168.0.100:3000'  # Replace with your Grafana URL

# Authentication credentials (username and password or API key)
GRAFANA_USERNAME = 'admin'  # Replace with your Grafana username
GRAFANA_PASSWORD = 'grafana'  # Replace with your Grafana password
GRAFANA_API_TOKEN = 'glsa_y5POB2jczeWzEUzWCvmqpm1r6syic7Ka_5769c173'  # Replace with your Grafana API Token 

# Headers for API requests (adjust as needed based on your authentication method)
headers = {
    "Content-Type": "application/json",  # Adjust based on content type (JSON or form data)
}

DASHBOARD_UID = 'c8a637ee-fa55-4982-9188-73b3132eb857'  # Replace with the UID of the dashboard you want to export
PANEL_ID = 1  # Replace with the ID of the panel you want to export
TIME_RANGE = 'now-7d/to/now'  # Replace with the desired time range

# Grafana Image Renderer configuration
RENDERER_URL = 'http://192.168.0.100:8081/render/d-solo'  # Replace with the renderer URL

def get_grafana_auth_token():
    # Create a session to maintain cookies for authentication
    session = requests.Session()

    # Authenticate and obtain an authentication token
    auth_data = {
        'user': GRAFANA_USERNAME,
        'password': GRAFANA_PASSWORD
    }

    response = session.post(f"{GRAFANA_URL}/login", headers=headers, json=auth_data)

    # Check if the login was successful (HTTP status code 200)
    if response.status_code == 200:
        print(f"Login successful - {response.text}")
        # Extract the authentication token from the response
        auth_token = response.headers.get("Authorization")
        
        if auth_token:
            print("Login successful")
            return auth_token
        else:
            print("Authentication token not found in response.")
            return None
        
    else:
        print(f"Login failed. Status code: {response.status_code} - {response.text}")
        return None

def export_panel_to_pdf(auth_session):
    # Get the panel URL
    panel_url = f"{GRAFANA_URL}/api/dashboards/uid/{DASHBOARD_UID}"

    # Prepare the API request headers
    headers = {
        'Authorization': f'Bearer {GRAFANA_API_TOKEN}',
        'Content-Type': 'application/json'
    }

    # Define the payload for the Image Renderer API
    payload = {
        'url': panel_url,
        'width': 1000,  # Adjust the width as needed
        'height': 500,  # Adjust the height as needed
        'timeout': 10000,  # Adjust the timeout as needed
        'format': 'pdf',
        'timeRange': TIME_RANGE
    }

    try:
        # Make a POST request to the Grafana Image Renderer API
        response = requests.post(RENDERER_URL, json=payload, headers=headers)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Save the PDF response content to a file
            with open('/tmp/panel_export.pdf', 'wb') as pdf_file:
                pdf_file.write(response.content)
            print("Panel exported to 'tmp/panel_export.pdf'")
        else:
            print(f"Failed to export panel. Status code: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    auth_session  = get_grafana_auth_token()
    export_panel_to_pdf(auth_session)