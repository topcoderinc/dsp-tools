# GROUND STATION MISSION POLLER

Poller that would poll the server periodically to check if there is a new scheduled mission, and would download the mission file if so.

# prerequisites
1. python 2.7.6
2. ubuntu

# Configuration
Configure following in agent/poller.py file
1. base_api_url - the base API url
2. username - the username of username (email)
3. password - the password of the user
4. pollinterval - the poll interval in second
5. download_folder - the folder in which the mission file will be downloaded.

# deployment
1. go to the agent folder
```bash
cd agent
```

2. run 
```bash
python poller.py
```
