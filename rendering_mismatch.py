"""
Script that renders randomly generated web pages in servo and firefox and reports the screenshots of both the engines for same file.
"""
import os
import webdriver
import subprocess

encoding = 'utf8'

#Starting servo
# os.chdir("..")
# p1 = subprocess.call('./mach run --webdriver 7002 --resolution 400x300', shell = True)

cmds = ['cd ..', './mach run --webdriver 7002 --resolution 400x300']
p = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE,
             stdout=subprocess.PIPE, stderr=subprocess.PIPE)

for cmd in cmds:
    p.stdin.write(cmd + "\n")
p.wait()
p1 = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE,
             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p1.stdin.write('SESSIONID=$(curl -X POST -d "{}" http://localhost:7002/session | jq -r ".value.sessionId")' + '\n')
p1.wait()
file_url = 'file://'
#Change your url here based on file location/web address

# url = 'http://example.org'

#Here since we are fixing number of html pages generated to 5, we keep the same value here
for x in range(1):
    url = file_url+'/home/harvey/Random-web-content-generator---CSC-517-OSS-Project/Generated_HTML_Files/file'+str(x)+'.html'
    p1.stdin.write("curl -v -X POST -d" + "'{"+'"url"'+": "+ '"'+url+'"'+"}'")
    # p1.wait()
    p1.stdin.write('curl -v http://localhost:7002/session/${SESSIONID}/screenshot | jq -r ".value" | base64 -d > test'+str(x)+'.png')
    p1.wait()

p1.stdin.close()
p.stdin.close()
# p2 = subprocess.call('SESSIONID=$(curl -X POST -d "{}" http://localhost:7002/session | jq -r ".value.sessionId")', shell = True)


