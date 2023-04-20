from flask import Flask, redirect, url_for, render_template, request, jsonify
from pymodbus.client import ModbusTcpClient
from os import system

app = Flask(__name__)

@app.route("/modbus/tcpip/ReadInputs", methods=["POST"])
def readInputs():
    request_data = request.get_json()
    ip = request_data['IpAddress']
    pin= int(request_data['Pin'])
    pin = 2**(8-(9-pin))
    try:
        client = ModbusTcpClient(ip)
        client.connect()
        input = client.read_input_registers(int(request_data['Address']))
        client.close()
        port = int(input.registers[0])
        result = port & pin
        return jsonify(bool(result)), 201
    except:
        print("no funciona")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, )