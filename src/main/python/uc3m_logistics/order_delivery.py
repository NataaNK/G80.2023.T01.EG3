"""MODULE: order_delivery. Contains the delivery order class"""
import json
from datetime import datetime

class OrderDelivery():
    """Class representing the information of a delivered product"""
    def __init__(self, tracking_code, date = datetime.timestamp(datetime.utcnow())):
        # Si no se especifica ninguna fecha, por defecto se introduce la fecha actual
        self.__delivery_day = date
        self.__tracking_code = tracking_code

    def __str__(self):
        return json.dumps(self.__dict__)

    @property
    def delivery_day(self):
        """
        Atribute representing the delivery day of the product
        """
        return self.__delivery_day

    @property
    def tracking_code(self):
        """
        Atribute representing the delivery day of the product
        """
        return self.__tracking_code
