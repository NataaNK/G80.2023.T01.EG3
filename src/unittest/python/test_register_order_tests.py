"""class for testing the regsiter_order method"""
import json
from unittest import TestCase
import os
from pathlib import Path
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

class TestOrderManager(TestCase):
    """class for testing the register_order method"""

    # Habría que fijar el time.stamp sino da un código distinto cada vez
    # pero si lo hacemos en el codigo no funcionara más
    # HACEMOS UN MOCKING:
    @freeze_time("2023-03-09")
    def test_register_order_ok_1(self):
        """
        Comprobación de MD5 válido
        """
        my_order = OrderManager()
        my_value = my_order.register_order("8435464158875", "premium", "Calle colmenarejo",
                                           "123456789", "28345")
        print(my_value)
        self.assertEqual("25f83613be1fe4590a114539c3472b97", my_value)

        """
        Comprobación de fichero generado válido
        """

        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/"
        file_store = JSON_FILES_PATH + "store_order_request.json"


        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        for item in data_list:
            if item["_OrderRequest__order_id"] == "25f83613be1fe4590a114539c3472b97":
                found = True

        self.assertTrue(found)
        #comentario de prueba

    def test_register_order_nok_1(self):
        """
        Product id Not a Number
        """
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.register_order("84354641588Aa", "premium", "Calle colmenarejo",
                                           "123456789", "28345")

        self.assertEqual(cm.exception.message, "Product ID should b")


if __name__ == '__main__':
    unittest.main()
