"""Autores: Natalia Rodríguez Navarro, Alberto Penas Díaz

OrderManager.py: En este módulo se recibe la información de un pedido,
se obtiene su firma MD5 y se guardan los datos en un fichero (antes se
valida el código del producto según la norma EAN13, los tipos de envíos,
las direcciones, teléfonos y códigos postales generando las excepciones
correspondientes cuando éstos no son válidos"""

import re
import json
from pathlib import Path
import os
import freezegun
import datetime
from datetime import datetime
from .order_management_exception import OrderManagementException
from .order_request import OrderRequest
from .order_shipping import OrderShipping
from .order_delivery import OrderDelivery


# GLOBAL VARIABLES
eanPattern = re.compile("[0-9]{13}$")
Phone_number_pattern = re.compile("[0-9]{9}$")
zip_code_pattern = re.compile("[0-9]{5}$")
md5_pattern = re.compile("[0-9A-Fa-f]{32}$")
email_pattern = re.compile("[a-z0-9]+@[a-z]+\.[a-z]{1,3}$")
sha256_pattern = re.compile("[a-fA-F0-9]{64}$")

class OrderManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(ean13_code):
        """
            Esta función verifica que el código proporcionado como ean13
            sea sintácticamente correcto además de comprobar si el último
            dígito de control es el correcto.
            :param ean13: str
            :return: bool
        """
        validate = True
        # Comprobación de sintaxis
        if eanPattern.fullmatch(ean13_code) is None:
            validate = False
        else:
            suma = 0
            # Índice
            i = 0
            # Según la  conveción EAN13 el último dígito del código debe
            # ser la resta de la potencia de diez más cercana a
            # la suma de los pares multiplicados por tres y los impares
            # menos ese mismo número.
            while i != len(ean13_code) - 1:
                suma += int(ean13_code[i]) * 3 \
                        if (i % 2) != 0 \
                        else int(ean13_code[i])
                i += 1

            if int(ean13_code[-1]) != (10 - suma % 10):
                validate = False

        # Lanzamos excepción si el código es incorrecto
        if not validate:
            raise ValueError("Product ID should be an EAN13")

        return validate

    def validate_order_type(self, order_type):
        """
        Lanza una excepción si el tipo de envío es incorrecto.
        No importa si introducen el tipo en mayúsculas o mínusculas.
        """
        if order_type.upper() != "PREMIUM" and order_type.upper() != "REGULAR":
            raise ValueError("Invalid Order Type")

    def validate_deivery_address(self, delivery):
        """
        Lanza una excepción si la dirección es incorrecta
        (entre 20 y 100 caracteres con al menos 2 cadenas separadas
        por un espacio blanco)
        """
        if len(delivery) < 20 or len(delivery) > 100:
            correct_lenght = False
        else:
            correct_lenght = True

        separation = False
        i = 0
        while not separation and i < len(delivery):
            if delivery[i] == ' ':
                separation = True
            i += 1

        if not correct_lenght or not separation:
            raise ValueError("Invalid Delivery Address")

    def validate_phone_number(self, number):
        """
        Lanza una excepción si el número de teléfono es incorrecto
        """
        if Phone_number_pattern.fullmatch(number) is None:
            raise ValueError("Invalid Phone Number")

    def validate_zip_code(self, zip):
        """
        Lanza una excepción si el código zip no es válido
        """
        validate = True
        if zip_code_pattern.fullmatch(zip) is None:
            validate = False
        else:
            if int(zip[0:2]) < 1 or int(zip[0:2]) > 52:
                validate = False

        if not validate:
            raise ValueError("Invalid Zip Code")


    def register_order(self, product_id, order_type, delivery_address, phone_number, zip_code):
        """
        Recibe la información de un pedido y si los datos recibidos son correctos,
        el componente obtendrá una firma mediante el algoritmo MD5. (Este valor MD5
        se obtiene del método __str__ de la clase OrderRequest. Esta firma será el
        identificador del pedido y en adelante se denominará OrderID. Además, se
        almacena en un fichero json todos los datos de la solicitud.
        """

        # Excepciones sobre los datos del pedido
        try:
            self.validate_ean13(product_id)
        except ValueError as vl:
            raise OrderManagementException("Product ID should be an EAN13") from vl

        try:
            self.validate_order_type(order_type)
        except ValueError as vl:
            raise OrderManagementException("Invalid Order Type") from vl

        try:
            self.validate_deivery_address(delivery_address)
        except ValueError as vl:
            raise OrderManagementException("Invalid Delivery Address") from vl

        try:
            self.validate_phone_number(phone_number)
        except ValueError as vl:
            raise OrderManagementException("Invalid Phone Number") from vl

        try:
            self.validate_zip_code(zip_code)
        except ValueError as vl:
            raise OrderManagementException("Invalid Zip Code") from vl

        # Generamos el objeto "pedido"
        my_order = OrderRequest(product_id, order_type, delivery_address,
                                phone_number, zip_code)

        # Añadimos la información del pedido a una lista de json's
        JSON_STORE_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/"
        file_store = JSON_STORE_PATH + "store_order_request.json"

        try:
            with open(file_store, "r", encoding="UTF-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("Json Decode Error - Wrong Json format") from ex

        # No meteremos información repetida
        if my_order.__dict__ not in data_list:
            data_list.append(my_order.__dict__)

        try:
            with open(file_store, "w", encoding="UTF-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex

        # Devolvemos el hash MD5
        return my_order.order_id

    def validate_content_json(self, load_json):
        """
        Recibe un json decodificado a diccionario y devuelve una excepción
        si no tiene la cantidad de contenido necesario para el método
        'send_product(). Es decir, si no contiene dos claves denominadas
        'OrderID' y 'ContactEmail'
        """
        validate = True
        OrderID = "OrderID"
        ContactEmail = "ContactEmail"

        if (OrderID not in load_json) or (ContactEmail not in load_json):
            validate = False

        if not validate:
            raise ValueError("Wrong input file data: should have 'OrderID' and 'ContactEmail'")

    def validate_md5(self, md5):
        """
        Lanza una excepción si el código md5 es inválido
        """
        if md5_pattern.fullmatch(md5) is None:
            raise ValueError("Invalid MD5")

    def validate_email(self, email):
        """
        Lanza una excepción si el email es inválido 
        """
        if email_pattern.fullmatch(email) is None:
            raise ValueError("Invalid Email Format")

    def send_product(self, input_file):

        # Abrimos el fichero json de entrada (información del envío) y lo decodificamos
        try:
            with open(input_file, "r", encoding="UTF-8", newline="") as file:
                input = json.load(file)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong input file path")
        except json.JSONDecodeError as ex:
            raise OrderManagementException("Json Decode Error - Wrong Json format") from ex

        # Comprobamos que la entrada contiene los datos necesarios
        try:
            self.validate_content_json(input)
        except ValueError as vl:
            raise OrderManagementException("Wrong input file data: should have 'OrderID' and 'ContactEmail'")

        # Guardamos la información del envío
        order_id = input["OrderID"]
        email = input["ContactEmail"]

        try:
            self.validate_md5(order_id)
        except ValueError as vl:
            raise OrderManagementException("Order ID should be a MD5") from vl

        try:
            self.validate_email(email)
        except ValueError as vl:
            raise OrderManagementException("Invalid Email Format") from vl

        # Abrimos el fichero que guarda la información de los pedidos
        try:
            with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/store_order_request.json", "r", encoding="UTF-8", newline="") as file:
                order_request_list = json.load(file)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong order request file path")
        except json.JSONDecodeError as ex:
            raise OrderManagementException("Json Decode Error - Wrong Json format") from ex

        # Comprobamos que existen los datos del pedido que se quiere enviar en
        # el almacén de pedidos. Una vez, encontrado ya no seguimos buscando
        found = False
        for i in order_request_list:
            if i["_OrderRequest__order_id"] == order_id:
                found = True
                product_id = request["_OrderRequest__product_id"]
                delivery_adress = request["_OrderRequest__delivery_address"]
                order_type = request["_OrderRequest__order_type"]
                phone_number = request["_OrderRequest__phone_number"]
                zip_code = request["_OrderRequest__zip_code"]
                time_stamp = request["_OrderRequest__time_stamp"]
            i += 1

        if not found:
            raise OrderManagementException("Order not Found")

        # Para comprobar que el OrderID coincide con los datos del pedido
        # (es decir, que no han sido manipulados). Generamos el MD5 que correspondería
        # a esos datos y ese tiempo
        time_freeze = datetime.fromtimestamp(time_stamp)
        freeze = freezegun.freeze_time(time_freeze)
        freeze.start()
        # Volvemos a generar el objeto en el mismo tiempo que fue creado
        order_check = OrderRequest(product_id, order_type, delivery_adress, phone_number, zip_code)
        freeze.stop()
        # Si el MD5 que acabamos de generar no coincide con el real, significa
        # que los datos han sido modificados
        if order_check.order_id != order_id:
            raise OrderManagementException("Invalid or Corrupt MD5 Hash")

        # Una vez comprobado, generamos un objeto de tipo OrderShipping, que nos generará
        # un código de rastreo SHA-256 correspondiente al pedido
        my_shipp = OrderShipping(product_id, order_id, email, order_type)

        # Una vez generado my_shipp, generamos un fichero en el que se almacenarán todos los envíos
        try:
            with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/store_shipping_order.json", "r", encoding="UTF-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("Json Decode Error - Wrong Json format") from ex

        # No meteremos información repretida
        if my_shipp.__dict__ not in data_list:
            data_list.append(my_shipp.__dict__)

        try:
            with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/store_shipping_order.json", "w", encoding="UTF-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex

        # Por último, devolvemos el código de rastreo
        return my_shipp.tracking_code

    def validate_sha256(self, sha):
        """
        Lanza una excepción si el código de registro SHA256 es inválido
        """
        if sha256_pattern.fullmatch(sha) is None:
            raise ValueError("Invalid SHA-256 Format")

    def deliver_product(self, tracking_number) -> bool:

        # Comprobamos que el SHA-256 es válido
        try:
            self.validate_sha256(tracking_number)
        except ValueError as vl:
            raise OrderManagementException("Tracking Code should be a SHA256") from vl

        # Abrimos el almacén con la información de los envíos
        try:
            with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/store_shipping_order.json", "r", encoding="UTF-8", newline="") as file:
                shippings = json.load(file)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong input file path")
        except json.JSONDecodeError as ex:
            raise OrderManagementException("Json Decode Error - Wrong Json format") from ex

        # Buscamos en el almacén si existe información sobre el envío
        # Una vez encontrado, no seguimos buscando
        found = False
        for shipp in shippings:
            if shipp["_OrderShipping__tracking_code"] == tracking_number:
                found = True
                product_id = shipp["_OrderShipping__product_id"]
                order_id = shipp["_OrderShipping__order_id"]
                delivery_email = shipp["_OrderShipping__delivery_email"]
                issued_at = shipp["_OrderShipping__issued_at"]
                delivery_day = shipp["_OrderShipping__delivery_day"]

        if not found:
            raise OrderManagementException("Shipping Order not Found")

        # Hay que volver a obtener el código de rastreo para comprobar que los
        # datos no han sido manipulados.
        # Para volver a obtener el SHA-256, hay que determinar cuál fue el tipo
        # de envío escogido
        delivery_time = delivery_day - issued_at
        if delivery_time <= (24*60*60):
            order_type = "premium"
            # Para comprobar que la fecha de envío es la correcta
            # volvemos a calcularla según el tipo de pedido
            my_delivery_day = issued_at + (24*60*60)
        else:
            order_type = "regular"
            my_delivery_day = issued_at + (7*24*60*60)

        # Compruebo si la fecha de entrega es igual a la registrada
        hoy = datetime.timestamp(datetime.utcnow())
        if delivery_day != my_delivery_day:
            raise OrderManagementException("Invalid Delivery Day")
        # Además, una vez entregado el pedido no es posible que la fecha de entrega
        # sea superior al día de hoy, por lo que tampoco será válida
        elif delivery_day < hoy:
            raise OrderManagementException("Invalid Delivery Day")

        # Una vez comprobada la fecha, generamos de nuevo el SHA-256
        time_freeze = datetime.fromtimestamp(issued_at)
        freeze = freezegun.freeze_time(time_freeze)
        freeze.start()
        # Volvemos a generar el objeto en el mismo tiempo que fue creado
        order_check = OrderShipping(product_id, order_id, delivery_email, order_type)
        freeze.stop()

        # Si el SHA256 que acabamos de generar no coincide con el real, significa
        # que los datos han sido modificados
        if order_check.tracking_code != tracking_number:
            raise OrderManagementException("Invalid or Corrupt SHA-256 Code")


        # Generamos el fichero donde se registrarán todas las entregas
        try:
            with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/store_deliveries.json", "r", encoding="UTF-8", newline="") as file:
                delivery_data = json.load(file)
        except FileNotFoundError as ex:
            delivery_data = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("Json Decode Error - Wrong Json format") from ex

        my_delivery = OrderDelivery(tracking_number, delivery_day)

        if my_delivery.__dict__ not in delivery_data:
            delivery_data.append(my_delivery.__dict__)

        try:
            with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/store_deliveries.json", "w", encoding="UTF-8", newline="") as file:
                json.dump(delivery_data, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex

        return True