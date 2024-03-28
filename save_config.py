#!/usr/bin/python3
from netmiko import ConnectHandler
import sys,os

def save_config():
    #set connection variables
    router_ip= str(sys.argv[1])
    router_user=os.environ.get("router_user")
    router_pass=os.environ.get("router_pass")
    
    #declare device connection
    device = {
        'device_type':'cisco_ios',
        'ip': router_ip,
        'username': router_user,
        'password': router_pass,
    }
    try:
        # connect to the device
        with ConnectHandler(**device) as ssh_conn:
            ssh_conn.enable()
            
            #send the command needed to save the config
            output=ssh_conn.send_command("write memory")
            
            #return comment after save is completed
            print("configuration saved")
            
    #Raise exception if connection fails
    except Exception as e:
        print(f'Error: {e}')
if __name__ == "__main__":
    #call the function
    save_config()
    