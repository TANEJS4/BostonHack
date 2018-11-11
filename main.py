import requests
import xml.etree.ElementTree as ET
from flask import Flask, render_template, request
app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello World"

@app.route('/')
def my_form():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    return processed_text

@app.route('/volume')
def volume():
    url = "http://192.168.1.17:8090/volume"
    r = requests.get(url)
    data = (r.text)
    print (data)
    return data

def info():
    url = "http://192.168.1.17:8090/volume"
    data = requests.get(url)
    tree =ET.parse(data)
    root = tree.getroot()
    attr = root.attrib
    splitAttr = atrr.split('=')
    deviceINFO = splitAttr[1]
    return deviceINFO

@app.route('/volumeChange')
def volumeChange():
    url = "http://192.168.1.17:8090/volume"
    data = '<volume>'+my_form_post+'</volume>'
    r = requests.post(url = url, data = data )
    result = (r.text)
    return result


@app.route('/')
def getSlaveStatus():
    url = "http://192.168.1.17:8090/volumeChange"
    data = requests.get(url)
    tree =ET.parse(data)
    root = tree.getroot()
    attr = root.attrib
    splitAttr = atrr.split('=')
    deviceINFO = splitAttr[1]
    return deviceINFO

@app.route('/removeSlave')
def removeSlave():
    url = "http://192.168.1.17:8090/removeZoneSlave"
    if (getSlaveStatus()!= 0):
        data = '<zone master=' + info() + '><member ipaddress=' getSlaveStatus()' + '>+ info() + '</member></zone>'
    r = requests.post(url = url, data = data )
    return r

@app.route('/speaker')
def lowSpeaker():
    url = "http://192.168.1.17:8090/speaker"
    data = "<play_info><app_key>your_app_key_here</app_key><url>https://raw.githubusercontent.com/TANEJS4/BostonHack/master/LowFrequency.mp3</url><service>service text</service><reason>reason text</reason><message>message text</message><volume>40</volume></play_info>"
    r = requests.post(url = url, data = data)
    return r


@app.route('/speaker')
def highSpeaker():
    url = "http://192.168.1.17:8090/speaker"
    data = "<play_info><app_key>your_app_key_here</app_key><url>https://raw.githubusercontent.com/TANEJS4/BostonHack/master/highFrequency.mp3</url><service>service text</service><reason>reason text</reason><message>message text</message><volume>40</volume></play_info>"
    r = requests.post(url = url, data = data)
    return r



if __name__ == '__main__':
    print("Please connect your phone to your speaker via wifi")
    print("Your IP address can be found by:" +
            "Going into to your BOSE SoundTouch app -> Tap hamburger menu  -> Select settings -> choose your BOSE device -> get the IP Address ")

    iP = input("Please enter your speaker's IP address")
    app.run(debug=True)
