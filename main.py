from flask import Flask, redirect, url_for, render_template, request, jsonify
from pymodbus.client import ModbusTcpClient
from os import system

# from pymodbus.client import AsyncModbusSerialClient
app = Flask(__name__)


@app.route("/modbus/tcpip/ReadInputs", methods=["POST"])
def readInputs():
    request_data = request.get_json()
    ip = request_data['IpAddress']
    try:
        client = ModbusTcpClient(ip)
        client.connect()
        input= client.read_input_registers(request_data['Address'])
        client.close()
        puerto=input.registers[0]
           
        return jsonify(format(puerto,'#08b')), 201
    
    except:
        print("no funciona")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, )
