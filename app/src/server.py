import os
import json
from flask import Flask, request, jsonify

server = Flask(__name__) #, static_url_path='/static', static_folder='src/static')

@server.route("/")
def hello():
    return server.send_static_file('./index.html')

@server.route("/scripts/getEvents.js")
def a():
    return server.send_static_file('./scripts/getEvents.js')

@server.route("/api/v1/events", methods=["GET"])
def events():
    if 'browser' not in request.args:
        return '{"error":"No browser provided"}'

    browser = request.args['browser']
    resp = {"browser": browser, "events":[], "logs":""}
    events_path = 'src/browser_events/%s_events.txt'%(browser)
    if not os.path.isfile(events_path):
        resp["logs"] = "no events file found for this browser"
        return json.dumps(resp)
    
    with open(events_path, 'r') as f:
        resp["events"] = json.load(f)
    
    os.system("ls")
    return json.dumps(resp)

@server.route("/api/v1/events", methods=["PUT"])
def b():
    if 'browser' not in request.args:
        return '{"error":"No browser provided"}'
    if 'browser' not in request.args:
        return '{"error":"No browser provided"}'
    browser = request.args['browser']
    resp = {"logs":""}
    events_path = 'src/browser_events/%s_events.txt'%(browser)

    with open(events_path, 'w') as f:
        pass
        f.write(json.dumps(request.json, indent=4))
    resp["logs"] = "ok";
    return json.dumps(resp)

if __name__ == "__main__":
    server.run()

