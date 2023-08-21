import requests
import json
import csv

class Exercise:
    def __init__(self, api_url, csv_filename):
        self.api_url = api_url
        self.csv_filename = csv_filename
    
    def make_request(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f'Request failed with status code: {response.status_code}')
        
    def parse_json(self, response_text):
        try:
            json_data = json.loads(response_text)
            return json_data
        except json.JSONDecodeError:
            raise Exception("Failed to parse JSON")

    def create_csv(self, json_data):
        with open(self.csv_filename, 'w', newline="") as csv_file:
            fieldnames = json_data[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader
            for row in json_data:
                writer.writerow(row)
                
class Sensor:
    def __init__(self):
        self.sense = SenseHat()
    
    def sensehat():
        pressure = int(self.sense.get_pressure())
        humidity = int(self.sense.get_humidity())
        self.sense.show_message(f"Pressure:{pressure}, Humidity{humidity}", scroll_speed=0.05)
        
            
def main():
    api_url = "https://restcountries.com/v3.1/all"
    csv_filename = "ExerciseClass.csv"
    
    ex = Exercise(api_url, csv_filename)  
    response_text = ex.make_request()
    json_data = ex.parse_json(response_text)
    ex.create_csv(json_data)
    
    print(f"CSV {csv_filename}file correctly created")
    
  #  sensor = Sensor()
# sensor.display_sensehat_data()
    
    
if __name__ == "__main__":
    main()

'''
 Writing a python program to make a HTTP GET request
Parsing JSON from the response text
Creating a CSV file from the JSON data
Make your python script executable
Display pressure/humidity on SenseHAT (integer)
Setup script run every 3 minutes via a cronjob
'''


