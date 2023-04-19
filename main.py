from flask import Flask, redirect, url_for, render_template, request, jsonify
from pymodbus.client import ModbusTcpClient
from os import system
import json

# from pymodbus.client import AsyncModbusSerialClient
app = Flask(__name__)


@app.route("/modbus/tcpip/ReadOutput", methods=["POST"])
def readOutput():
    request_data = request.get_json()
    ip = request_data['IpAddress']
    try:
        client = ModbusTcpClient(ip)
        client.connect()
        r = client.read_coils(136,8)
        client.close()
        return jsonify(r.bits), 201
    except:
        print("An exception occurred")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, )
