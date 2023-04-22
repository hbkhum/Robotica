from flask import Flask, redirect, url_for, render_template, request, jsonify
from pymodbus.client import ModbusTcpClient
from os import system

# from pymodbus.client import AsyncModbusSerialClient
app = Flask(__name__)


@app.route("/modbus/tcpip/ReadHoldingRegister1", methods=["POST"])
def modbus():
    request_data = request.get_json()
    ip = request_data['IpAddress']
    try:
        client = ModbusTcpClient(ip)
        client.connect()
        reg=client.read_input_registers(request_data['Address'], 1)
        client.close()
        return jsonify(reg.register), 201
    except:
        print("An exception occurred")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, )
