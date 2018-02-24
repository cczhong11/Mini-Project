from flask import Flask, request
import requests
import json
pythonServiceHostName = "http://task3-service.default.svc.cluster.local"
#pythonServiceHostName = "http://172.17.0.1:6000"
app = Flask(__name__, static_folder='site', static_url_path='')


@app.route("/", methods=['GET'])
def handle():
    return app.send_static_file("index.html")


@app.route("/python", methods=['GET', 'POST'])
def handlePython():
    if request.method == 'POST':
        print("---")
        try:
            code = request.form['code']
            print(code)
        except:
            code = request.json['code']
            print(code)
        data = {}
        data["code"] = code
        data["Content-Type"] = "application/json"
        r = requests.post(pythonServiceHostName + "/py/eval",
                          data=json.dumps(data))

        # This should return the stdout and stderr in json format
        # return the exact response fom pyService.py only!
        # Your code should handle 'code' as an argument in both
        # request.form and request.json
        ### BEGIN STUDENT CODE ###
        ### END STUDENT CODE ###
        return r.text
    else:
        return app.send_static_file("python.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
