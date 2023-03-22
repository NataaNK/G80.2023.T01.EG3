"""Autores: Natalia Rodríguez Navarro, Alberto Penas Díaz

OrderManager.py: En este módulo se valida el código de barras según
la norma EAN13. También se generan las excepciones"""

import re
from .order_request import OrderRequest

# GLOBAL VARIABLES
eanPattern = re.compile("[0-9]{13}")

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
            return not validate

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
        return validate

    def register_order(self, product_id, order_type, delivery_address, phone_number, zip_code):
        """
        Recibe la información de un pedido y si los datos recibidos son correctos,
        el componente obtendrá una firma mediante el algoritmo MD5. (Este valor MD5
        se obtiene del método __str__ de la clase OrderRequest. Esta firma será el
        identificador del pedido y en adelante se denominará OrderID. Además, se
        almacena en un fichero todos los datos de la solicitud.
        """
        my_order = OrderRequest(product_id, order_type, delivery_address, phone_number, zip_code)


        return my_order.order_id

