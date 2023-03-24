"""Autores: Natalia Rodríguez Navarro, Alberto Penas Díaz

Generador de excpciones para el módulo order_manager"""

class OrderManagementException(Exception):
    """Personalised exception for Order Management"""
    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        """gets the message value"""
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value
