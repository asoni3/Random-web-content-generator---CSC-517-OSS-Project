import os
import subprocess
import json
import requests

cmds = ['cd ..', './mach run --webdriver 7002 --resolution 400x300']
p = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE,
             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for cmd in cmds:
    p.stdin.write(cmd.encode('utf-8'))


url = 'http://localhost:7002/session'
payload = "{}"
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=payload, headers=headers)
json_string = r.json()
for x in range(1):
    json_data = {}
    json_data['url'] = 'file://file'+str(x)+'.html'
    json_data = json.dumps(json_data)
    
    url2 = 'http://localhost:7002/session/'+json_string['value']['sessionId']+'/url'
    payload2 = json_data
    headers2 = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r2 = requests.post(url2, data=payload2, headers=headers2)
    
    curl_command2 = 'curl -v http://localhost:7002/session/'+json_string['value']['sessionId']+'/screenshot | jq -r ".value" | base64 -d > testing'+str(x)+'.png'
    
    p = subprocess.Popen(curl_command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    os.system(curl_command2)
