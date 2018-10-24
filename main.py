import json
import sys
import requests as req
from datetime import datetime

#for visualization
import matplotlib.pyplot as plt
import numpy as np

#disable ssl warnings for better readability
import urllib3
urllib3.disable_warnings()


def makeRequest(url, header, data):
    # Start time count
    t0 = datetime.now()
    # Make request
    resp = req.post(url, data=json.dumps(data), headers=header, verify=False)
    # Stop time
    t1 = datetime.now()
    # Calculate elapsed time
    t_diff = t1 - t0
    #Convert timestamp into milliseconds
    elapsed_ms = int(((t_diff.days * 86400000) + (t_diff.seconds * 1000) + (t_diff.microseconds / 1000)) + 0.5)

    #Output
    print(type + " request " + str(i + 1) + ":\t" + str(elapsed_ms) + "ms\t" + " - " + str(resp.status_code))
    return elapsed_ms



#Retrieve parameters
type = sys.argv[1]
url = sys.argv[2]
img_url = sys.argv[3]
iterations = int(sys.argv[4])

#Prepare request
headers = {"Content-Type":"application/json"}
payload = {"imgurl":img_url}

#Initialize array for test results
times = np.empty(iterations, np.int32)

print("Platform: " + type)
for i in range(iterations):
    times[i] = makeRequest(url, header=headers, data=payload)

#Calculate charecteristics
print(times)
print(type + " Cold: " + str(times[0]))
print(type + " Median: " + str(np.median(times)) + "ms")
print(type + " Mean: " + str(np.mean(times)) + "ms")
print(type + " Max: " + str(np.max(times)) + "ms")
print(type + " Min: " + str(np.min(times)) + "ms")


#Create Plot
plt.plot(np.arange(1, iterations+1, dtype=np.int32), times)
plt.axis([1, iterations+1, np.min(times)*0.9, np.max(times)*1.1])
plt.title(type)
plt.xlabel('# des Versuchs')
plt.ylabel('Antwortzeit in Millisekunden')
#Save plot
plt.savefig("./ResultsImg/"+type + "-" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ".png")

