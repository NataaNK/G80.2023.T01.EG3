from unittest import TestCase
import json
import os
from pathlib import Path
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

# Global Variables
JSON_TEST_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/json_tests/"
ORDER_DATA = ["8435464158875", "premium", "Avenidas Contrarrevolucionarias", "123456789", "28345"]

class TestSendProduct(TestCase):
    @freeze_time("2023-03-09")
    def test_send_product_valid_1(self):

        input_file = JSON_TEST_PATH + "mytest1.json"

        with open(input_file, "r", encoding="UTF-8", newline="") as file:
            order_request_list = json.load(file)

        my_order = OrderManager()
        md5 = my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3], ORDER_DATA[4])
        print(md5)

        self.assertEqual(my_order.send_product(input_file), "webo")