from flask import Flask, redirect, url_for, render_template, request, jsonify
from pymodbus.client import ModbusTcpClient
from os import system

# from pymodbus.client import AsyncModbusSerialClient
app = Flask(__name__)


@app.route("/modbus/tcpip/writeCoils", methods=["POST"])
def modbus():
    request_data = request.get_json() # Obtiene los datos enviados en la solicitud POST en formato JSON
    ip = request_data['IpAddress'] #Almacena el valor en la variable ip
    try:
        client = ModbusTcpClient(ip) # Crea una conexión con el dispositivo Modbus a través de la dirección IP
        client.connect() #Inicia la conexion
        client.write_register(request_data['Address'], request_data['Value'],)
        # Escribe los valores el registro, las direccion y el valor es pedido mediante dos variables que se obtienen
        # por medio de postman Address (la direccion del registro), Value (el valor que se quiere escribir)
        client.close() # Cierra la conexión con el dispositivo Modbus
        return jsonify(True), 201 # Devuelve una respuesta JSON con un valor booleano "True"
    except:
        print("An exception occurred") #Si ocurre una excepción, imprime un mensaje de error en la consola


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, )
