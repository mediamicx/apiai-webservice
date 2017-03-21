#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "report.bug":
        return {}
    result = req.get("result")
    # bug = req.get("resolvedQuery")
    parameters = result.get("parameters")
    # browser = parameters.get("Browser")
    # os = parameters.get("OS")
    link = parameters.get("Link")

    # cost = {'Europe':100, 'North America':200, 'South America':300, 'Asia':400, 'Africa':500}

    # speech = "The cost of shipping to " + zone + " is " + str(cost[zone]) + " euros."

    # speech = "Vielen Dank. Ich habe folgendes Verstanden. Das Problem: " + bug + ". Das Problem kann man auf/in  " + os + " im " + browser + " nachvollziehen. Link oder Screenshot: " + link
    speech = "Danke." + link

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-webservice"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0') 
