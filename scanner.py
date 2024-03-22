import sys
import socket
from datetime import datetime

print(datetime.now())

print(sys.version)


def check_ip(target):

       target_split = target.split('.')
       
       for x in target_split:
             
               x = int(x)
                
               if(x in range(1,255)):
                       return True;
               else:
                       return False;   
                       
                       
       
       
if (len(sys.argv) == 2):
          target = socket.gethostbyname(sys.argv[1])
          
          if (check_ip(target) == True):
             
             print('IP ADDRESS CHECKED')
          
          else:
          
             print('Please, enter the correct form of IP address')
          
#elif(check_ip())



else:
          print('Invalid amount of arguments!')
          
          print('ArgError : python3 scanner.py <ip>' )
          
          
#socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((target, 777))     

#portscanner banner

print ('_'*50+'\n')

print("Scanning target: %s" %target)

print ("Time started: "+str(datetime.now()))

print ('_'*50)


try:

      for port in range(1,65535):
            
            scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            socket.setdefaulttimeout(1)
            
            result = scan.connect_ex((target,port))
            
            if (result == 0):
            
                print(f'Port {port} is open\n')
            
           # else:
              #  print(f'Port {port} is close')    
                #scan.close()
            scan.close()
except KeyboardInterrupt:
       print('\nExiting program!') 
       sys.exit
       
#except socket.error:
   #   print('Could not connect to the server')         