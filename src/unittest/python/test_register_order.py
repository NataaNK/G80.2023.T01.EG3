"""class for testing the regsiter_order method"""
import unittest
import os
from pathlib import Path
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

class TestOrderManager(unittest.TestCase):
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
        self.assertEqual("51fd83d6d7e9181181bc9676103a23f7", my_value)

    # Hay que comprobar también que se guarda en un fichero, para comprobar
    # que el fichero no ha cambiado hacemos un hash del fichero y si es el mismo
    # no ha cambiado
    @freeze_time("2023-03-09")
    def test_register_order_ok_2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_file/"
        file_store = JSON_FILES_PATH + "store_order_request.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_order = OrderManager()
        my_value = my_order.register_order("8435464158875", "premium", "Calle colmenarejo",
                                           "123456789", "28345")
        self.assertEqual("51fd83d6d7e9181181bc9676103a23f7", my_value)

        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)

        found = False

        for item in data_list:
            if item["_OrderRequest__order_id"] == "51fd83d6d7e9181181bc9676103a23f7":
                found = True

        self.assertTrue(found)


if __name__ == '__main__':
    unittest.main()
