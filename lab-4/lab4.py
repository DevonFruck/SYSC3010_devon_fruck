import http.client
import urllib.parse
import time
key = "AT68QYQ94MQEWXL3" # Put your API Key here

def send_data():

    params = urllib.parse.urlencode({'field1': 'L3-T-1', 'field2':'devonfruck@cmail.carleton.ca', 'field3': 'b', 'key':key })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")

    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        conn.close()
     
    except:
        print("connection failed")

    
if __name__ == "__main__":
    send_data()

