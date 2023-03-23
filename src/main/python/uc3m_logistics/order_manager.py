"""Autores: Natalia Rodríguez Navarro, Alberto Penas Díaz

OrderManager.py: En este módulo se valida el código de barras según
la norma EAN13. También se generan las excepciones"""

import re
import json
from pathlib import Path
import os
from .order_management_exception import OrderManagementException
from .order_request import OrderRequest


# GLOBAL VARIABLES
eanPattern = re.compile("[0-9]{13}")
Phone_number_pattern = re.compile("[0-9]{9}")
zip_code_pattern = re.compile("[0-9]{5}")

class OrderManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(ean13_code):
        """
            Esta función verifica que el código proporcionado como ean13
            sea sintácticamente correcto ademmás de comprobar si el último
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

        if not validate:
            raise ValueError("Product ID should be an EAN13")

        return validate

    def validate_order_type(self, order_type):
        """
        Lanza una excepción si el tipo de de envío es incorrecto
        """
        if order_type != "premium" and order_type != "regular":
            raise ValueError("Invalid Order Type")

    def validate_deivery_address(self, delivery):
        """
        Lanza una excepción si la dirección es incorrecta
        (entre 20 y 100 caracteres con al menos 2 cadenas separadas por un espacio blanco)
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
        almacena en un fichero todos los datos de la solicitud.
        """
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

        my_order = OrderRequest(product_id, order_type, delivery_address,
                                phone_number, zip_code)

        JSON_STORE_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/"
        file_store = JSON_STORE_PATH + "store_order_request.json"

        try:
            with open(file_store, "r", encoding="UTF-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("Json Decode Error - Wrong Json format") from ex

        data_list.append(my_order.__dict__)

        try:
            with open(file_store, "w", encoding="UTF-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex

        return my_order.order_id