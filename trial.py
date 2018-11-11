import requests
import xml.etree.ElementTree as ET
from flask import Flask, render_template, request
app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello World"

@app.route("/")
def homepage():
    """
    we want to input from user : IPADDress
    give prompt how he can find on the app
    1. connect your via wifi
    2. find iP THROUGH phone hamburger -> settinggs -> device -> IP address

     valid -> true
                 get target volume
            -> false
                try again
    store value => ipconfig:
        homepage.ipconfig()
    check if there is a zone
             -> True
             call removeSlave
             else continue
    """


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
    print ("Inside function")
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
    data = '<?xml version="1.0" encoding="UTF-8" ?><volume deviceID="' + info() + '><targetvolume>' + my_form_post + '</targetvolume><actualvolume>' + my_form_post +'</actualvolume><muteenabled>false</muteenabled></volume>'
    r = requests.post(url = url, data = data )
    data = (r.text)
    print (data)
    return data


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





if __name__ == '__main__':
    app.run(debug=True)
