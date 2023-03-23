"""class for testing the regsiter_order method"""
from unittest import TestCase
import json
import os
from pathlib import Path
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

class TestOrderManager(TestCase):
    """class for testing the register_order method"""

    # TESTS ALL CORRECT:

    @freeze_time("2023-03-09")
    def test_register_order_ok_1(self):
        """
        Comprobación de MD5 válido
        """
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/"
        file_store = JSON_FILES_PATH + "store_order_request.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_order = OrderManager()
        my_value = my_order.register_order("8435464158875", "premium", "Calle Colmenarejo, Galapagar",
                                           "123456789", "28345")

        self.assertEqual("ba862867cb7761b9364a35f6a8d9801c", my_value)

        """
        Comprobación de fichero generado válido
        """

        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/"
        file_store = JSON_FILES_PATH + "store_order_request.json"

        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        for item in data_list:
            if item["_OrderRequest__order_id"] == "ba862867cb7761b9364a35f6a8d9801c":
                found = True

        self.assertTrue(found)

    # TESTS PRODUCT ID:

    def test_register_order_nok_1(self):
        """
        Product ID Not a Number
        """
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.register_order("84354641588Aa", "premium", "Calle Colmenarejo, 5",
                                           "123456789", "28345")

        self.assertEqual("Product ID should be an EAN13", cm.exception.message)

    def test_register_order_nok_2(self):
        """
        Product ID Not Check Sum
        """
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.register_order("8435464158870", "premium", "Calle Colmenarejo, 5",
                                           "123456789", "28345")

        self.assertEqual("Product ID should be an EAN13", cm.exception.message)

    def test_register_order_nok_3(self):
        """
        Product ID 12 Digits
        """
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.register_order("843546415887", "premium", "Calle Colmenarejo, 5o",
                                           "123456789", "28345")

        self.assertEqual("Product ID should be an EAN13", cm.exception.message)

    def test_register_order_nok_4(self):
        """
        Product ID 14 Digits
        """
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.register_order("8435464158879", "premium", "Calle Colmenarejo, 5",
                                           "123456789", "28345")

        self.assertEqual("Product ID should be an EAN13", cm.exception.message)

    # TESTS ORDER_TYPE:

    @freeze_time("2023-03-09")
    def test_register_order_ok_2(self):
        """
        order_type = "regular"
        """
        my_order = OrderManager()
        my_value = my_order.register_order("8435464158875", "regular", "Calle Colmenarejo, 5",
                                           "123456789", "28345")

        self.assertEqual("4565371337e0ce39202cbdcba5ba7100", my_value)


        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/"
        file_store = JSON_FILES_PATH + "store_order_request.json"

        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        for item in data_list:
            if item["_OrderRequest__order_id"] == "4565371337e0ce39202cbdcba5ba7100":
                found = True

        self.assertTrue(found)

    def test_register_order_nok_5(self):
        """
        Order type Not Valid
        """
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.register_order("8435464158875", "apple", "Calle Colmenarejo, 5",
                                           "123456789", "28345")

        self.assertEqual("Invalid Order Type", cm.exception.message)

    # TESTS ADRESS:

    @freeze_time("2023-03-09")
    def test_register_order_ok_3(self):
        """
        Adress 20 char
        """
        my_order = OrderManager()
        my_value = my_order.register_order("8435464158875", "premium", "Calle Colmenarejo, 5",
                                           "123456789", "28345")

        self.assertEqual("bc468149c36d67d3e9a7e9fabf297f1a", my_value)


        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/"
        file_store = JSON_FILES_PATH + "store_order_request.json"

        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        for item in data_list:
            if item["_OrderRequest__order_id"] == "bc468149c36d67d3e9a7e9fabf297f1a":
                found = True

        self.assertTrue(found)

    @freeze_time("2023-03-09")
    def test_register_order_ok_4(self):
        """
        Adress 21 char
        """
        my_order = OrderManager()
        my_value = my_order.register_order("8435464158875", "premium", "Calle Colmenarejo, 52",
                                           "123456789", "28345")

        self.assertEqual("09e5d8f8ce7ca08b8aaf2aee97c0b6b5", my_value)


        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/"
        file_store = JSON_FILES_PATH + "store_order_request.json"

        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        for item in data_list:
            if item["_OrderRequest__order_id"] == "09e5d8f8ce7ca08b8aaf2aee97c0b6b5":
                found = True

        self.assertTrue(found)

    @freeze_time("2023-03-09")
    def test_register_order_ok_5(self):
        """
        Adress 99 char
        """
        my_order = OrderManager()
        my_value = my_order.register_order("8435464158875", "premium",
                                           "Calle Colmenarejo de los Rosales, Olivares del Júcar, Provincia de Madrid, España,  52, planta 12BA",
                                           "123456789", "28345")

        self.assertEqual("bbd5da1ff08e8c4239fd942fc9a0cdc7", my_value)


        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/"
        file_store = JSON_FILES_PATH + "store_order_request.json"

        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        for item in data_list:
            if item["_OrderRequest__order_id"] == "bbd5da1ff08e8c4239fd942fc9a0cdc7":
                found = True

        self.assertTrue(found)

    @freeze_time("2023-03-09")
    def test_register_order_ok_6(self):
        """
        Adress 100 char
        """
        my_order = OrderManager()
        my_value = my_order.register_order("8435464158875", "premium",
                                           "Calle Colmenarejo de los Rosales, Olivares del Júcar, Provincia de Madrid, España,  52, planta 12BAC",
                                           "123456789", "28345")

        self.assertEqual("54f0c7650120aa61b3fcf1cb67302ffa", my_value)


        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/"
        file_store = JSON_FILES_PATH + "store_order_request.json"

        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        for item in data_list:
            if item["_OrderRequest__order_id"] == "54f0c7650120aa61b3fcf1cb67302ffa":
                found = True

        self.assertTrue(found)

    @freeze_time("2023-03-09")
    def test_register_order_ok7(self):
        """
        More than one blank space
        """
        my_order = OrderManager()
        my_value = my_order.register_order("8435464158875", "premium", "C/ Colmenarejo, 5, Madrid",
                                           "123456789", "28345")

        self.assertEqual("060db6247d46e650f114162f6a1a7030", my_value)


        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/"
        file_store = JSON_FILES_PATH + "store_order_request.json"

        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        for item in data_list:
            if item["_OrderRequest__order_id"] == "060db6247d46e650f114162f6a1a7030":
                found = True

        self.assertTrue(found)

    def test_register_order_nok_6(self):
        """
        Address 19 char
        """
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.register_order("8435464158875", "premium", "Calle Colmenarjo, 5",
                                           "123456789", "28345")

        self.assertEqual("Invalid Delivery Address", cm.exception.message)

    def test_register_order_nok_7(self):
        """
        Address 101 char
        """
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.register_order("8435464158875", "premium",
                                               "Calle Colmenarejo de los Rosales, Olivaress del Júcar, Provincia de Madrid, España,  52, planta 12BAC",
                                               "123456789", "28345")

        self.assertEqual("Invalid Delivery Address", cm.exception.message)

    def test_register_order_nok_8(self):
        """
        Address Not blank spaces
        """
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.register_order("8435464158875", "premium", "CalleColmenarjo,5,Madrid",
                                           "123456789", "28345")

        self.assertEqual("Invalid Delivery Address", cm.exception.message)

    # TESTS PHONE NUMBER:

    def test_register_order_nok_9(self):
        """
        Phone Number 8 digits
        """
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.register_order("8435464158875", "premium", "Calle Colmenarejo, 5",
                                           "12345678", "28345")

        self.assertEqual("Invalid Phone Number", cm.exception.message)

    def test_register_order_nok_10(self):
        """
        Phone Number 10 digits
        """
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.register_order("8435464158875", "premium", "Calle Colmenarejo, 5",
                                               "1234567890", "28345")

        self.assertEqual("Invalid Phone Number", cm.exception.message)

    def test_register_order_nok_11(self):
        """
        Phone Number Not a Number
        """
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.register_order("8435464158875", "premium", "Calle Colmenarejo, 5",
                                           "1234567BA", "28345")

        self.assertEqual("Invalid Phone Number", cm.exception.message)

    # TESTS ZIP CODE


if __name__ == '__main__':
    unittest.main()
