from flask import Flask, render_template, request
import requests
import xmltodict
app = Flask(__name__)

@app.route("/")
def hello(): 
    return "Hello World"
#
# @app.route("/home")
# def home():
#     return "<h1>home   page</h1>"
#
# @app.route("/about")
# def about():
#     return "<h1>about page</h1>"
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

"""
@app.route('/volume', method=['GET'])
def volume(volume):
    url = "http://192.168.43.119:8090";
    vol_url = url + "/volume"
    repsonse = requests.get(vol_url)
    xml_response = response.text
    # Convert XML to dict and parse just the volume?
    dict_resp = xmltodict.parse(xml_response)
    if(dict_resp.ContainKey("actualVolume")):
        print("Actual volume: " + actualVolume);
"""
if __name__ == '__main__':
    app.run(debug=True)

#
# @app.route('/statusRoom', method=['GET'])
# def statusRoom():
#     url = "http://" + IP_ADDRESS_OF_SPEAKER + ":8090";
#     stat_url = url + "/getZone"
#     repsonse = requests.get(stat_url)
#     xml_response = response.text
#     dict_resp = xmltodict(xml_response)
#     if(dict_resp.ContainKey("actualVolume")){
#     print("Devices connected:" + member);
#     removeSlave();
#     }
#
#
# @app.route('/removeZoneSlave', method=['POST'])
# def removeSlave():
#     url = "http://" + IP_ADDRESS_OF_SPEAKER + ":8090";
#     spkrAround_url = url + "/removeZoneSlave"
#     repsonse = requests.get(spkrAround_url)
#     xml_response = response.text
#     dict_resp = xmltodict(xml_response)
#      #attribute to remove
