from flask import Flask, redirect, url_for, render_template, request, jsonify
from pymodbus.client import ModbusTcpClient
from os import system

app = Flask(__name__)


##Alejandro
@app.route("/modbus/tcpip/ReadInput", methods=["POST"])
def readInput():
    request_data = request.get_json()
    ip = request_data['IpAddress']
    pin = int(request_data['Pin'])
    pin = 2 ** (8 - (9 - pin))
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


##Alberto
@app.route("/modbus/tcpip/ReadInputs", methods=["POST"])
def readInputs():
    request_data = request.get_json()
    ip = request_data['IpAddress']
    try:
        client = ModbusTcpClient(ip)
        client.connect()
        input = client.read_input_registers(int(request_data['Address']))
        client.close()
        puerto = input.registers[0]
        return jsonify(format(puerto, '#08b')), 201

    except:
        print("no funciona")


##Sergio
@app.route("/modbus/tcpip/ReadOutput", methods=["POST"])
def readOutput():
    request_data = request.get_json()
    ip = request_data['IpAddress']
    try:
        client = ModbusTcpClient(ip)
        client.connect()
        r = client.read_coils(int(request_data['Address']), 8)
        client.close()
        return jsonify(r.bits), 201
    except:
        print("An exception occurred")


##Eduardo
@app.route("/modbus/tcpip/WriteCoils", methods=["POST"])
def writeCoils():
    request_data = request.get_json()
    ip = request_data['IpAddress']
    v = request_data['OutPut']
    try:
        client = ModbusTcpClient(ip)
        client.connect()
        # v = [False,True,False,True,False,True,True,True]
        client.write_coils(int(request_data['Address']), v)
        ##r = client.read_coils(136,8)
        client.close()
        return jsonify(True), 201
    except:
        print("An exception occurred")


##Cristian
@app.route("/modbus/tcpip/ReadHoldingRegister", methods=["POST"])
def readHoldingRegister():
    request_data = request.get_json()
    ip = request_data['IpAddress']
    try:
        client = ModbusTcpClient(ip)
        client.connect()
        reg = client.read_holding_registers(int(request_data['Address']), 1)
        client.close()
        return jsonify(reg.registers[0]), 201
    except:
        print("An exception occurred")


##Alexis
@app.route("/modbus/tcpip/WriteHoldingRegister", methods=["POST"])
def writeHoldingRegister():
    request_data = request.get_json()  # Obtiene los datos enviados en la solicitud POST en formato JSON
    ip = request_data['IpAddress']  # Almacena el valor en la variable ip
    try:
        client = ModbusTcpClient(ip)  # Crea una conexi?n con el dispositivo Modbus a trav?s de la direcci?n IP
        client.connect()  # Inicia la conexion
        client.write_register(int(request_data['Address']), int(request_data['Value']), )
        # Escribe los valores el registro, las direccion y el valor es pedido mediante dos variables que se obtienen
        # por medio de postman Address (la direccion del registro), Value (el valor que se quiere escribir)
        client.close()  # Cierra la conexi?n con el dispositivo Modbus
        return jsonify(True), 201  # Devuelve una respuesta JSON con un valor booleano "True"
    except:
        print("An exception occurred")  # Si ocurre una excepci?n, imprime un mensaje de error en la consola


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, )