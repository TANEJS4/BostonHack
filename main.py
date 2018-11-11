import requests
import time
import xml.etree.ElementTree as ET
from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    return processed_text

# @app.route('/volume')
# def volume():
#     url = "http://192.168.1.17:8090/volume"
#     r = requests.get(url)
#     data = (r.text)
#     print (data)
#     return data

# def info():
#     url = "http://192.168.1.17:8090/volume"
#     data = requests.get(url)
#     tree = ET.parse(data)
#     root = tree.getroot()
#     attr = root.attrib
#     splitAttr = atrr.split('=')
#     deviceINFO = splitAttr[1]
#     return deviceINFO

@app.route('/<ipconfig>/volume/<v>/')
def volumeChange(ipconfig,v):
    url = 'http://' + ipconfig + ':8090/volume'
    r1 = requests.get(url)
    data1 = (r1.text)
    print (data1)
    data = '<volume>' + v + '</volume>'
    r = requests.post(url = url, data = data )
    result = (r.text)
    return data1


# @app.route('/<ipconfig>/')
# def getSlaveStatus(ipconfig):
#     url = 'http://' + ipconfig + ':8090/volume'
#     data = requests.get(url)
#     tree =ET.parse(data)
#     root = tree.getroot()
#     attr = root.attrib
#     splitAttr = atrr.split('=')
#     deviceINFO = splitAttr[1]
#     return deviceINFO


# @app.route('/removeSlave')
# def removeSlave():
#     url = "http://192.168.1.17:8090/removeZoneSlave"
#     if (getSlaveStatus()!= 0):
#         data = '<zone master=' + info() + '><member ipaddress=' getSlaveStatus()' + '>+ info() + '</member></zone>'
#     r = requests.post(url = url, data = data )
#     return r

@app.route('/<ipconfig>/speaker')
def lowSpeaker(ipconfig):
    url = 'http://' + ipconfig + ':8090/speaker'
    data = "<play_info><app_key>yMFGZBuUj8II9kMfFN8uw3aWfqczkzed</app_key><url>https://raw.githubusercontent.com/TANEJS4/BostonHack/master/LowFrequency.mp3</url><service>service text</service><reason>reason text</reason><message>message text</message><volume>40</volume></play_info>"
    r = requests.post(url = url, data = data)
    return r


@app.route('/<ipconfig>/speaker')
def highSpeaker(ipconfig):
    rl = 'http://' + ipconfig + ':8090/speaker'
    data = "<play_info><app_key>yMFGZBuUj8II9kMfFN8uw3aWfqczkzed</app_key><url>https://raw.githubusercontent.com/TANEJS4/BostonHack/master/highFrequency.mp3</url><service>service text</service><reason>reason text</reason><message>message text</message><volume>40</volume></play_info>"
    r = requests.post(url = url, data = data)
    return r



if __name__ == '__main__':
    app.run(debug=True)
