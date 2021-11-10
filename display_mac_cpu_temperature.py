### Name of the script: display_mac_cpu_temperature.py
### Author: Venkat Akula ###
### Last updated: 11/10/2021 ###
### Description ###
### This code is written for Mac OS
### Starts simple HTTP server provided with GET method
### Displays hostname, current timestamp and CPU temperature
### When the temperatus is above threshold limit
###    - it is displayed in red color and
###    - generates voice message
#################################################################
import datetime
import os
import re
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8000
temperature_threshold = 60

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.hostname = socket.gethostname()
        self.timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
        self.cpu_die_temperature = os.popen('sudo powermetrics -n1 -i1 --samplers smc |grep -i "CPU die temperature"').read()
        self.cpu_temperature = float(re.findall("\d+\.\d+", self.cpu_die_temperature)[0])
        
        self.wfile.write(f'<h3 style="color:blue">HostName: {self.hostname} </h3>'.encode())
        self.wfile.write(f'<h3>Date_Time: {self.timestamp}</h3>'.encode())

        if self.cpu_temperature > temperature_threshold:
            self.wfile.write(f'<h3 style="color:red">{self.cpu_die_temperature}</h3>'.encode())
            os.system('say "CPU temperature is more than the threshold"')
        else:
            self.wfile.write(f'<h3 style="color:green">{self.cpu_die_temperature}</h3>'.encode())
        
        self.wfile.write(f'<body>Threshold temperature: {temperature_threshold} C</body>'.encode())


if __name__ == "__main__":
    if os.name != 'posix':
        exit("This code is written for Mac")
    
    with HTTPServer((hostName, serverPort), handler) as webServer:
        print(f'Server started http://{hostName}:{serverPort}')
        print('Press ^C to terminate...')

        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass
        
        webServer.server_close()
        print("Server stopped.")
