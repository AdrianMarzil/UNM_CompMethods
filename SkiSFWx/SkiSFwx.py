from flask import Flask, jsonify
import os

app = Flask(__name__)

DATA_FILE = "weather_data.dat"  # Path to your .dat file

@app.route('/get_weather_data', methods=['GET'])
def get_weather_data():
    try:
        # Read the .dat file
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                data = file.readlines()

            # Parse the last N lines (e.g., latest 50 records)
            latest_data = [line.strip() for line in data[-50:]]  # Adjust for your needs
            
            # Convert into a list of dictionaries (or send raw lines)
            table_data = []
            for row in latest_data:
                fields = row.split(",")  # Assuming comma-separated values
                table_data.append({
                    "Timestamp": fields[0],
                    "RecordNumber": fields[1],
                    "TempMax": fields[2],
                    "TempMin": fields[3],
                    "TempAvg": fields[4],
                    "WindChill": fields[5],
                    "WindMax": fields[6],
                    "WindMin": fields[7],
                    "WindAvg": fields[8],
                    "WindDir": fields[9],
                    "Humidity": fields[10],
                    "DewPoint": fields[11],
                    "Pressure": fields[12],
                    "BatteryVoltage": fields[13],
                    "PanelTemp": fields[14],
                })

            return jsonify(table_data)  # Send data as JSON
        else:
            return jsonify({"error": "Data file not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
