### Name of the script: refreshUrl.py
### Author: Venkat Akula ###
### Last updated: 11/10/2021 ###
### Description ###
### This code is tested on a MacBook
### This script refreshes given url at specified time intervals
#################################################################
import webbrowser
from time import sleep

hostName = "localhost"
serverPort = 8000
refresh_interval = 5 #sec
url=f'http://{hostName}:{serverPort}'

if __name__ == "__main__":
    print(f'The page {url} will be refreshed at every {refresh_interval} sec')
    print('Press ^C to terminate...')
    while True:
        try:
            webbrowser.open(url)
            sleep(refresh_interval)
        except KeyboardInterrupt:
            exit("Closing the page")
