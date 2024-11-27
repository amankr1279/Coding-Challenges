# Coding Challenges Fyi- Build You Own Load Balancer

This project is an implementation of a simple load balancer catering 3 backend servers. 

## Architecture

The repository contains of 3 entities:-

### Load Balancer
It is a java based Spring-boot project that connects to 3 backend servers and forwards requests to them in a **round-robin** way. 

- It runs on port `8080` and exposes a GET API `/home`.
- Uses round-robin algorithm for load distribution. 
- Can handle upto 200 concurrent requests because of inbuilt tomcat server usage.
- it sends requests to only those servers who are healthy.  


### Backend Servers
There are 3 backend servers that will actually implement the request from end-user. The servers are single-threaded and handle 1 request at a time
 
- The servers run on ports: `8081`, `8082` and `8083`. 
- They have 2 GET endpoints:- `/` and `/ping`.
- `/` is for handling requests received from the Load Balancer. 
- `/ping` is for getting health status of the server. 


### Poller
Poller is a python script whose purpose is to ping every backend server every 10 seconds to know their health status. The health status of servers is stored in a file `health_status.json`. Poller runs independently of backend servers and the Load Balancers. 


## Usage

Follow these steps for getting started:-
1. Go to `ccldb` directory.
2. Create a json file `health_status.json` and populate it as follows
```json
{
    "server1": false,
    "server2": false,
    "server3": false
}
```
3. There are 2 modes :-
    1. All servers healthy.
    2. Some server(s) are healthy.
4. Start the poller and Load Balancer in different terminals. 
5. Hit the `/home` API of Load Balancer multiple times and observe how it goes to different servers.
6. We can also down or up a server and see how does it affect load distribution. 

```bash
python3 poller.py
mvn clean install
mvn spring-boot:run
``` 

### All Servers are healthy

1. Go to `servers` directory.
2. Run `python3 launch_servers.py`.

### Some Servers are healthy

1. Go to `servers` directory.
2. Open 3 terminals and each terminal launch a server.

All servers are flask based

```bash
python3 server1.py
python3 server2.py
python3 server3.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)