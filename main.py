from flask import Flask, redirect, url_for, render_template, request, jsonify
from pymodbus.client import ModbusTcpClient
from os import system

app = Flask(__name__)
@app.route("/modbus/tcpip/writeCoils", methods=["POST"])
def writeCoils():
    request_data = request.get_json()
    ip = request_data['IpAddress']
    try:
        client = ModbusTcpClient(ip)
        client.connect()
        v = [False,True,False,True,False,True,True,True]
        client.write_coils(136,v)
        r = client.read_coils(136,8)
        client.close()
        return jsonify(True), 201
    except:
        print("An exception occurred")