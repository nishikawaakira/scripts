import os
import sys
import time
from datetime import datetime

args = sys.argv;

targetPath = "/var/www/html"
targetLength = "10"
if (len(args) > 1):
    targetPath = args[1]

if (len(args) > 2):
    targetLength = args[2]

if (targetLength.isdigit() == False):
    print('usage: targetLength is not integer')
    exit()

def getfilelist(found, path, targetLength):
    for root, dirs, files in os.walk(path):
        for filename in files:
            filepath = os.path.join(root, filename)
            timestamp = os.path.getmtime(filepath)
            if (len(found) < targetLength):
                found.append({"name":filepath, "timestamp": timestamp})
                found = sorted(found, key=lambda x:x["timestamp"], reverse=True)
            else:
                if (timestamp < found[targetLength-1]):
                    found[targetLength-1] = {"name":filepath, "timestamp": timestamp}
                    found = sorted(found, key=lambda x:x["timestamp"], reverse=True)

    return found

found = []
found = getfilelist(found, targetPath, int(targetLength))

for data in found:
    data["timestamp"] = datetime.fromtimestamp(data["timestamp"]).strftime("%Y/%m/%d %H:%M:%S")
    print(data)

