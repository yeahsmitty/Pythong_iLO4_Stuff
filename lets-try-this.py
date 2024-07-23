import sys
import redfish
import json

# When running on the server locally use the following commented values
# HOST = "blobstore://."
# LOGIN_ACCOUNT = "None"
# LOGIN_PASSWORD = "None"

# When running remotely connect using the iLO address, iLO account name,
# and password to send https requests
SYSTEM_URL = "https://192.168.68.64"
LOGIN_ACCOUNT = "Justin"
LOGIN_PASSWORD = "welcome2"
DATA = '{"Oem": {"Hpe": {"FanPercentAdjust": 50}}}'

## Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=SYSTEM_URL, username=LOGIN_ACCOUNT,\
                                    password=LOGIN_PASSWORD)

# Login into the server and create a session
REDFISH_OBJ.login()

# Do a GET on a given path
RESPONSE = REDFISH_OBJ.get("/redfish/v1/Chassis/1/Thermal/")

# Do a PATCH to slow down fans
RESPONSE = REDFISH_OBJ.patch("/redfish/v1/Chassis/1/Thermal/ ", DATA)


# Print out the response
sys.stdout.write("%s\n" % RESPONSE)

# Logout of the current session
REDFISH_OBJ.logout()