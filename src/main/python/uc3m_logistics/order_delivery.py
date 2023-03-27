"""Autores: Natalia Rodríguez Navarro, Alberto Penas Díaz

order_delivery.py: Contiene la clase OrderDelivery"""

import json

class OrderDelivery():
    """
    Class representing the information of a delivered product
    """
    def __init__(self, tracking_code, date):
        self.__delivery_day = date
        self.__tracking_code = tracking_code

    def __str__(self):
        return json.dumps(self.__dict__)

    @property
    def delivery_day(self):
        """
        Attribute representing the delivery day of the product
        """
        return self.__delivery_day

    @property
    def tracking_code(self):
        """
        Attribute representing the delivery day of the product
        """
        return self.__tracking_code
