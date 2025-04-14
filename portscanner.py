#!/bin/python3
import socket
import sys
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  #Resolve hostname to IPv4
else:
    print("Invalid number of arguments.")
    print(f"Usage: python3 {sys.argv[0]} <ip>")
    sys.exit()

#Pretty banner
print("-" * 50)
print(f"Scanning target: {target}")
print(f"Scanning started at: {datetime.now()}")
print("-" * 50)

try:
    for port in range(1,1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))    #returns an error indicator
        if result == 0:                         #if port is open it will return 0
            print(f"Port {port}/tcp is open")
        s.close()
    print("-" * 50)
    print(f"Scanning completetd at {datetime.now()}")
    print("-" * 50)
except KeyboardInterrupt:
    print("\nProgram closed by user.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("Couldn't connect to target.")
    sys.exit()
except Exception as error:
    print(error)
    sys.exit()

