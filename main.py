from flask import Flask, redirect, url_for, render_template, request, jsonify
from pymodbus.client import ModbusTcpClient
from os import system
# from pymodbus.client import AsyncModbusSerialClient
app = Flask(__name__)

@app.route("/modbus", methods=["POST"])
def modbus():
    request_data = request.get_json()
    if request_data['Type'] == "HoldingRegister":
        if request_data['Protocol'] == "TCP/IP":
            ip = request_data['IpAddress']
            client = ModbusTcpClient(ip)
            client.connect()
            client.write_register(request_data['Address'], request_data['Value'])
            client.close()
            # return jsonify("ok")
        elif request_data['Protocol'] == "RS485":
            print('hola')
            # client = AsyncModbusSerialClient("Com")
            # await client.connect()
            # await client.write_register(request_data['Address'], request_data['Value'])
    elif request_data['Type'] == "ReadHoldingRegister":
        if request_data['Protocol'] == "TCP/IP":
            ip = request_data['IpAddress']
            client = ModbusTcpClient(ip)
            client.connect()
            register1=request_data['Address']
            register = client.read_input_registers(request_data['Address'])
            client.close()
            #print(register.registers[0])
            #return json(register)
            return print("El valor del registro",register1,"con la ip:",ip,"es:",register.registers[0])
    elif request_data['Type'] == "ReadHoldingRegisterS":
            if request_data['Protocol'] == "TCP/IP":
                ip = request_data['IpAddress']
                client = ModbusTcpClient(ip)
                client.connect()
                register = client.read_input_registers(request_data['Address'])
                client.close()
                # print(register.registers[0])
                # return json(register)
                return print("El valor del sensor", register.registers[0])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, )
