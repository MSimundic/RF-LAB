import re

LINE_START = ">>>  [Device Install (Hardware initiated)"
infile = r"setup.dev.log"


with open(infile) as f:
    for line in f:
        if LINE_START in line and "USBSTOR" in line:
            splitString = re.split("#|&", line)
            # print (x)
            print(f"Vendor: {splitString[2]}")
            print(f"Product ID: {splitString[3]}")
            print(f"Revision: {splitString[4]}")
            print(f"Serial number: {splitString[len(splitString)-3]}")

            splitString = re.split(" ", next(f))
            print(f"Date: {splitString[4]}")
            print(f"Time: {splitString[5]}")

