from flask import Flask, request, jsonify
import json
import os
app = Flask(__name__, static_url_path='')


@app.route("/py/eval", methods=['GET', 'POST'])
def handle():
    if request.method == 'POST':

        # Implementation goes here.
        #
        # Both stdout and stderr should be captured.
        # {"stdout": "<output_from_stdout>", "stderr": "<output_from_stderr>"}

        ### BEGIN STUDENT CODE ###
            # get data
        print(request.data)
        data = str(request.data, "utf-8")
        try:
            code = json.loads(data)["code"]
            with open("code.py", "w") as f:
                f.write(code)
            # run data
            os.system("python3 code.py > result     2>error")

            # get result
            with open("result") as f:
                result = f.read()
            with open("error") as f:
                error = f.read()
            print(request.data)
            return_value = {}
            return_value["stderr"] = error
            return_value["stdout"] = result
        except:
            return_value = {}
            return_value["stderr"] = ''
            return_value["stdout"] = ''
        return jsonify(return_value)
        ### END STUDENT CODE ###


if __name__ == '__main__':
    app.run(threaded=True, debug=True, host="0.0.0.0", port=6000)
