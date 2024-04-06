#!/usr/bin/env python3

#this is a portscaner that will scan the ports of a given ip address

import socket #importing the socket module

import sys #importing the sys module

from datetime import datetime #importing the datetime module

#this will define the target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #this translates the hostname to the ipv4 address

else:
    print("Wrong command!\n")

    print("Syntax: python3 portscanner.py <ip>") #this will print the correct syntax of the command

    sys.exit("Invalid command line arguments") #this will exit the program with an error message

#this is a welcome message
    
print(sys.version) 

#this will print a banner with information on the target
    
print("_" * 50,"\n")

print("Scanning target: " + target)

print("Time started: " + str(datetime.now()))

print("_" * 50, "\n")

#this will scan the ports

try:
    for port in range(1, 65535):

        scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #this will create a socket object

        socket.setdefaulttimeout(1) #this will set the timeout to 1 second

        result = scan.connect_ex((target, port)) #this will return an error indicator      

        if result == 0: #this should check if the port is open/closed
                
                print("Port {} is open".format(port)) #this will print the open port

        scan.close() #this will close the socket    

except KeyboardInterrupt:
    print("\n\nExiting due to user interruption...")
    sys.exit(0)

except socket.gaierror: #this will handle the error if the hostname could not be resolved
     
    print("\n\nHostname could not be resolved")
    sys.exit(0) 

except socket.error: #this will handle the error if the server is not responding       
     
    print("\n\nServer is not responding")

    sys.exit(0) 


#this will print the time the scan was completed    
    

print("_" * 50,"\n")

print("Time completed: " + str(datetime.now())) 

print("_" * 50) 

#this will print a closing message  

print("Port scanning completed!")

print("_" * 50,"\n")

print(datetime.now())

print("_" * 50)

print("Exiting program...")