#!/usr/bin/python3

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#
#
#	File Name 	 	: ARUPSEKport_scanner
#	Author	 	 	:ARUP BASAK
#	last modified	: 15 jan 2021
#	Language		: Python
#	python version 	: python3.9
#	Requirment 		: re , nmap3 , threading , os , subprocess , time , sys , pyfiglet
#   github          : https://github.com/ArupSEK/
#	
#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# 
#    ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____      
#    |  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \     
#    | |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |    
# _ _|  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < _ _ 
#(_|_)_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_(_|_)
#
#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import pyfiglet
from termcolor import colored
from argparse import ArgumentParser
import socket
from threading import Thread
from time import time
from datetime import datetime
front_banner=pyfiglet.figlet_format(" PORT SCANNER")
print(colored(front_banner,'green'))

#Banner
print("_"*50)
print("_"*50)
print(colored("Scanning Taget: ",'green'))
print(colored("Scanning started at: " +str(datetime.now()),'green'))
print("_"*50)
print("_"*50) 




open_ports = []

def prepare_arg():
    """prepare arguments
    return:
        args(argparse.Namespace)
    """
    # optionl arguments
    parser = ArgumentParser(description=colored("Python Based Fast Port Scanner",'green'),usage="%(prog)s 192.168.0.1",epilog="Example - %(prog)s -s 20 -e 65535 -t 500 -V 192.168.0.1")
    parser.add_argument("-s","--start",metavar="\b",dest="start",type=int,help="starting port",default=1) #metavar="/b" is used to manage the space in output/front
    parser.add_argument("-e","--end",metavar="\b",dest="end",type=int,help="Ending port",default=1023)
    parser.add_argument("-t","--threads",metavar="\b",dest="threads",type=int,help="thred to use",default=500)

    """if -V or --verbose used then acation value gives true value to dest and dest value will set to true,
    if not used then by default it is false
    """

    parser.add_argument("-V","--verbose",dest="verbose",action="store_true",help="verbose output")
    parser.add_argument("-v","--version",action="version",version="%(prog)s relase 1.0",help="disply version")

    #positionl argument
    parser.add_argument(metavar="IPv4",dest="ip",help="Host to scan")
    args = parser.parse_args()
    return args
def prepare_ports(start:int,end:int):
    """creating generator fuction for ports
    arguments:
     start(int) -starting port
     end(int) -end port
    """
    for port in range(start,end+1):
        yield port               # its store start to end port in memory like array and one time use

def scan_port():
    """scan ports"""
    while True:
        try:
            s =socket.socket()
            s.settimeout(1)
            port = next(ports)
            s.connect((arguments.ip,port)) 
            open_ports.append(port)  
            if arguments.verbose:
                print(f"\r{open_ports}",end="")
        except(ConnectionRefusedError,socket.timeout):
            continue
        except StopIteration:
            break     



def prepare_threads(threads:int):
    """ create, start, join threads 
    arguments:
        threads(int) -Number of threads to use 
    """
    thread_list = []
    for _ in range(threads+1):
        thread_list.append(Thread(target=scan_port)) # make tread and append on list
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
 
if __name__ == "__main__":
    arguments = prepare_arg()
    ports = prepare_ports(arguments.start,arguments.end)
    start_time =time()
    prepare_threads(arguments.threads)
    end_time = time()
    if arguments.verbose:
        print()
    print(colored(f"open Ports Found - {open_ports}",'green'))
    print(colored(f"Time Taken- {round(end_time-start_time,2)}",'green'))


    input()


