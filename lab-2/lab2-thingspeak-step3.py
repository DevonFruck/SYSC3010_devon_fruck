import requests

def read_data_thingspeak():
    URL= "https://api.thingspeak.com/channels/1155814/feeds.json?api_key="
    read_key= "DQ8BD020QX1WPVY5"
    header = "&results=2"
    new_url = URL + read_key + header

    get_data = requests.get(new_url).json()
    #print(get_data)

    print("Channel name: " + str(get_data["channel"]["name"]))
    print("Channel ID: " + str(get_data["channel"]["id"]))
    print("Feed:") #str(get_data["feeds"]["field1"])    

    fields = get_data['feeds']
    temp = []
        
    for i in fields:
        temp.append(i["field1"])
        
    print(temp)


if __name__ == "__main__":
    read_data_thingspeak()
