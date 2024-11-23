import time
import requests
import json

DURATION = 10 # seconds

SERVERS = [
    "http://localhost:8081/ping",
    "http://localhost:8082/ping",
    "http://localhost:8083/ping"
    ]

while True:
    f = open("health_status.json", "r+")
    data:dict = json.load(f)
    for i,server in enumerate(SERVERS):
        try:
            print(f"GET {server}")
            response = requests.get(url=server, timeout=100)
            print(response.text)
            print(data)
            if response.ok:
                # make entry in DB that this server is healthy
                data[f"server{i+1}"] = True  
            else:
                raise Exception(f"Server{i+1} is unhealthy")
        except Exception as ex:
            print(ex)
            # make entry that server is not healthy
            data[f"server{i+1}"] = False
        f.seek(0)
        json.dump(data, fp=f, indent=4) 
        f.truncate()     
        time.sleep(DURATION)
