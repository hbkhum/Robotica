from flask import Flask, redirect, url_for, render_template, request, jsonify
from pymodbus.client import ModbusTcpClient
from os import system

# from pymodbus.client import AsyncModbusSerialClient
app = Flask(__name__)


@app.route("/modbus/tcpip/writeHoldingRegister", methods=["POST"])
def modbus():
    request_data = request.get_json()
    ip = request_data['IpAddress']
    try:
        client = ModbusTcpClient(ip)
        client.connect()
        client.write_register(request_data['Address'], request_data['Value'])
        client.close()
        return jsonify(True), 201
    except:
        print("An exception occurred")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, )
