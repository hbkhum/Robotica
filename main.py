from flask import Flask, redirect, url_for, render_template, request, jsonify
from pymodbus.client import ModbusTcpClient
from os import system

# from pymodbus.client import AsyncModbusSerialClient
app = Flask(__name__)


<<<<<<< HEAD
@app.route("/modbus/tcpip/ReadInputs", methods=["POST"])
def readInputs():
=======
@app.route("/modbus/tcpip/ReadHoldingRegister", methods=["POST"])
def modbus():
>>>>>>> Cristian
    request_data = request.get_json()
    ip = request_data['IpAddress']
    pin= int(request_data['Pin'])
    pin = 2**(8-(9-pin))
    try:
        client = ModbusTcpClient(ip)
        client.connect()
<<<<<<< HEAD
        input = client.read_input_registers(int(request_data['Address']))
        client.close()
        port = int(input.registers[0])
        result = port & pin
        return jsonify(bool(result)), 201
=======
        reg = client.read_holding_registers(request_data['Address'], 1)
        client.close()
        return jsonify(reg.registers[0]), 201
>>>>>>> Cristian
    except:
        print("no funciona")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, )