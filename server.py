from urllib import request
from flask import Flask
from flask import request, send_file, Response
import analytics
import requests
from datetime import date
from excel import ExcelGenerator
from workers import scanner
import threading

app = Flask(__name__)


@app.route("/", methods=["GET", "POST", "DELETE"])
def index():
    return { "status" : "unauthorized" }

@app.route("/report", methods=["GET"])
def report():
    module = request.args.get('module')
    items = requests.get("https://lara.barrancosecurity.me/kazas/report/{}".format(module))

    data = items.json()["data"]

    ExcelGenerator(
        data, "./reports/kazas-{}-{}.xlsx".format(module, date.today())
    ).generate()

    return send_file("reports/kazas-{}-{}.xlsx".format(module, date.today()))


@app.route("/scan", methods=["POST"])
def scan():
    with open("./scans/scan-{}.txt".format(date.today()), "w") as scan:
                scan.write("0")
                scan.close()
    content = request.json

    def long_running_task(**kwargs):
        scanner(content["module"])
        
        with open("./scans/scan-{}.txt".format(date.today()), "w") as scan:
                scan.write("done")
                scan.close()
    thread = threading.Thread(target=long_running_task, kwargs={
                    'post_data':  content})
    thread.start()

    return content


@app.route("/scan/session", methods = ["GET"])
def scanSession():
    with open("./scans/scan-{}.txt".format(date.today()), "r") as scan:
        count = scan.readline()
        scan.close()
        return {
            "count": count
        }



if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5001)
