import os
import time
from ftplib import FTP

# Local path to the weather data file
#DATA_FILE = r"C:\Users\aidroom\Documents\WXStationLog\CR1000_RF407_SkiSF_Met.dat"
DATA_FILE = r"C:\Users\marzi\OneDrive - University of New Mexico\CE DEPARTMENT\WX STATIONS\STATIONS\Ski SF Station\CR1000_RF407_SkiSF_Met [OLD Nov-Dec2023].dat"
OUTPUT_HTML = "weather_data.html"

# FTP credentials for uploading the file
FTP_SERVER = "ftp.skisantafe.com"  # Replace with your FTP server
FTP_USERNAME = "WeatherStation"    # Replace with your username
FTP_PASSWORD = "W3@ther2024"    # Replace with your password
FTP_DIRECTORY = "/public_html/weather"  # Target directory on the server

def parse_weather_data():
    """Read and parse the latest weather data from the .dat file."""
    if not os.path.exists(DATA_FILE):
        print("Data file not found.")
        return [], []

    with open(DATA_FILE, "r") as file:
        lines = file.readlines()

    # Extract headers and the latest row of data
    headers = lines[0].strip().split(",")  # Header row
    latest_data = lines[-1].strip().split(",")  # Latest data row
    return headers, latest_data

def generate_html(headers, latest_data):
    """Generate an HTML file with the latest weather data."""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Ski Santa Fe Weather Data</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; }}
            table {{ width: 80%; margin: auto; border-collapse: collapse; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: center; }}
            th {{ background-color: #4CAF50; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>Ski Santa Fe Weather Station</h1>
        <table>
            <tr>
                {''.join(f'<th>{header}</th>' for header in headers)}
            </tr>
            <tr>
                {''.join(f'<td>{data}</td>' for data in latest_data)}
            </tr>
        </table>
        <p>Last Updated: {time.strftime('%Y-%m-%d %H:%M:%S')}</p>
    </body>
    </html>
    """
    with open(OUTPUT_HTML, "w") as file:
        file.write(html)
    print("HTML file generated.")

def upload_to_ftp():
    """Upload the generated HTML file to the FTP server."""
    try:
        ftp = FTP(FTP_SERVER)
        ftp.login(FTP_USERNAME, FTP_PASSWORD)
        ftp.cwd(FTP_DIRECTORY)

        with open(OUTPUT_HTML, "rb") as file:
            ftp.storbinary(f"STOR {OUTPUT_HTML}", file)

        ftp.quit()
        print("HTML file uploaded successfully.")
    except Exception as e:
        print(f"FTP upload failed: {e}")

if __name__ == "__main__":
    # Parse data, generate HTML, and upload every 10 minutes
    while True:
        headers, latest_data = parse_weather_data()
        if headers and latest_data:
            generate_html(headers, latest_data)
            upload_to_ftp()
        else:
            print("No data found to update.")
        
        # Wait for 10 minutes before updating again
        time.sleep(600)