import urllib2
import json
import time
import os 
import datetime

# base api url
base_api_url = "https://kb-dsp-server.herokuapp.com"

# the user name and password of the user
username ="tcveshu@gmail.com"
password = "topcoder"

# polling interval in second
pollinterval = 30 

# download folder
download_folder= 'missions'

# checks if there are new missions to download
# if new mission is found will return the id to download
def check_mission(token):
   request = urllib2.Request(base_api_url+"/api/v1/missions")
   request.add_header("Authorization", "Bearer %s" % token)   
   result = urllib2.urlopen(request)
   return json.load(result)

# download the mission file and save in the current folder
def download_mission(mission_id, token, filename):
    try:
        req = urllib2.Request(base_api_url+"/api/v1/missions/{0}/download".format(mission_id))
        req.add_header("Authorization", "Bearer %s" % token)
        result= urllib2.urlopen(req)
        with open(filename, "wb") as file:
            file.write(result.read())
        print "new mission downlaoded successfully"
    except Exception, e:
        print str(e)

# gets the access token for user
def get_access_token():
    req = urllib2.Request(base_api_url+"/api/v1/users/auth")
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps({"email": username, "password": password}))
    return json.load(response)["accessToken"]

# main function that runs in given interval
def main():
    try:
        print "checking for new missions"
        token = get_access_token()
        missions= check_mission(token)
        for mission in missions:
            id= mission["id"]
            
            filename = os.path.join(download_folder, id+".mission")
            isUpdated=False
            if os.path.isfile(filename):
                # check if mission is updated and later than we downloaded the mission file
                last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
                mission_time= datetime.datetime.strptime(mission["updatedAt"], '%Y-%m-%dT%H:%M:%S.%fZ')
                if(mission_time>  last_modified_time):
                    isUpdated=True
            
            if not os.path.isfile(filename) or isUpdated:
                print "found new mission, downloading the file"
                download_mission(id, token, filename)
                
    except Exception, e: 
        print str(e)

# check if folder exists or not, if not exists create it
if not os.path.exists(download_folder):
    os.makedirs(download_folder)
while True:
    main()
    time.sleep(pollinterval)

