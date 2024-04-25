import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from PIL import Image

GRAFANA_URL = "http://localhost:3000"
DASHBOARD_UID = "c8a637ee-fa55-4982-9188-73b3132eb857"
GRAFANA_API_TOKEN = "glsa_y5POB2jczeWzEUzWCvmqpm1r6syic7Ka_5769c173"
RENDERER_URL = "http://localhost:8081/render/d-solo"
TIME_RANGE = "now-24h/to/now"

def fetch_dashboard_panels():
    # Prepare the API request headers
    headers = {
        'Authorization': f'Bearer {GRAFANA_API_TOKEN}',
        'Content-Type': 'application/json'
    }

    # Make a GET request to fetch the dashboard details
    dashboard_url = f"{GRAFANA_URL}/api/dashboards/uid/{DASHBOARD_UID}"
    response = requests.get(dashboard_url, headers=headers)

    if response.status_code == 200:
        dashboard_data = response.json()
        return dashboard_data.get("dashboard", {}).get("panels", [])
    else:
        print(f"Failed to fetch dashboard. Status code: {response.status_code}")
        return []

def fetch_panel_image(panel_id):
    # Get the panel URL
    panel_url = f"{GRAFANA_URL}/d/{DASHBOARD_UID}/panel/{panel_id}"

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
        'format': 'png',  # Use PNG format for individual panels
        'timeRange': TIME_RANGE
    }

    # Make a POST request to the Grafana Image Renderer API
    response = requests.post(RENDERER_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        print(f"Failed to fetch panel {panel_id}. Status code: {response.status_code}")
        return None

def export_dashboard_to_pdf():
    panel_ids = [panel["id"] for panel in fetch_dashboard_panels()]

    # Create a PDF file
    pdf_buffer = BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=letter)

    # Set the initial position for the first panel
    x = 50
    y = 750

    for panel_id in panel_ids:
        panel_image = fetch_panel_image(panel_id)
        if panel_image:
            # Add the panel image to the PDF
            c.drawImage(panel_image, x, y, width=400, height=200)
            c.showPage()  # Add a new page for the next panel

    # Save the PDF
    c.save()

    # Write the PDF to a file
    with open('/tmp/dashboard_export.pdf', 'wb') as pdf_file:
        pdf_file.write(pdf_buffer.getvalue())

    print("Dashboard exported to 'tmp/dashboard_export.pdf'")

if __name__ == "__main__":
    export_dashboard_to_pdf()
