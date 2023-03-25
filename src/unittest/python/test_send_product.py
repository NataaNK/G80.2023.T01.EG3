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

    # TEST VÁLIDO:
    # MD5 válido con 32 hexadecimales
    # Nombre y dominio email válido
    # Extensión email de 3 letras
    @freeze_time("2023-03-09")
    def test_send_product_valid_1(self):

        # Vacío el store antes de empezar de nuevo los tests para que no se repita
        JSON_STORE_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/"
        file_store = JSON_STORE_PATH + "store_shipping_order.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        input_file = JSON_TEST_PATH + "mytest1.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        self.assertEqual("c7d0c3b0098a98d782981e6c5d7f5a2808dd0c6841dd12c1932e9ad9499b243c", my_order.send_product(input_file))

    # DUPLICACIÓN DEL NODO 1 ("dos json's"):
    def test_send_product_duplication_2(self):

        input_file = JSON_TEST_PATH + "mytest2.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 1 (fichero vacío):
    def test_send_product_deletion_3(self):

        input_file = JSON_TEST_PATH + "mytest3.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 2 (dos llaves de inicio):
    def test_send_product_duplication_4(self):

        input_file = JSON_TEST_PATH + "mytest4.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 2 (sin llave de inicio):
    def test_send_product_deletion_5(self):

        input_file = JSON_TEST_PATH + "mytest5.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 3 (Dos veces los datos detro de las llaves):
    def test_send_product_duplication_6(self):

        input_file = JSON_TEST_PATH + "mytest6.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 3 (Sin datos detro de las llaves):
    def test_send_product_deletion_7(self):

        input_file = JSON_TEST_PATH + "mytest7.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Wrong input file data: should have 'OrderID' and 'ContactEmail'", cm.exception.message)

    # DUPLICACIÓN DEL NODO 4 (Dos llaves al final):
    def test_send_product_duplication_8(self):

        input_file = JSON_TEST_PATH + "mytest8.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 4 (Sin llave final):
    def test_send_product_deletion_9(self):

        input_file = JSON_TEST_PATH + "mytest9.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # MODIFICACIÓN DEL NODO 5 (LLave de inicio distinta):
    def test_send_product_modification_10(self):

        input_file = JSON_TEST_PATH + "mytest10.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 6 (Dos veces campo 1, datos de OrderID):
    def test_send_product_duplication_11(self):

        input_file = JSON_TEST_PATH + "mytest11.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 6 (Sin campo 1, datos del OrderID):
    def test_send_product_deletion_12(self):

        input_file = JSON_TEST_PATH + "mytest12.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 7 (Dos veces el separador ','):
    def test_send_product_duplication_13(self):

        input_file = JSON_TEST_PATH + "mytest13.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 7 (Sin separador ','):
    def test_send_product_deletion_14(self):

        input_file = JSON_TEST_PATH + "mytest14.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 8 (Dos veces campo 2, datos del ContactEmail):
    def test_send_product_duplication_15(self):

        input_file = JSON_TEST_PATH + "mytest15.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 8 (Sin campo 2, datos del ContactEmail):
    def test_send_product_deletion_16(self):

        input_file = JSON_TEST_PATH + "mytest16.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # MODIFICACIÓN DEL NODO 9 (Llave final distinta):
    def test_send_product_modification_17(self):

        input_file = JSON_TEST_PATH + "mytest17.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 10 (Etiqueta 1, "OrderID", dos veces):
    def test_send_product_duplication_18(self):

        input_file = JSON_TEST_PATH + "mytest18.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 10 (Sin etiqueta 1, "OrderID"):
    def test_send_product_deletion_19(self):

        input_file = JSON_TEST_PATH + "mytest19.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 11 (Dos igualdades -> esta prueba ya cubre al nodo 15):
    def test_send_product_duplication_20(self):

        input_file = JSON_TEST_PATH + "mytest20.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 11 (Sin igualdad -> esta prueba ya cubre al nodo 15):
    def test_send_product_deletion_21(self):

        input_file = JSON_TEST_PATH + "mytest21.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

   # DUPLICACIÓN DEL NODO 12 (Dos datos 1, "MD5"):
    def test_send_product_duplication_22(self):

        input_file = JSON_TEST_PATH + "mytest22.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

   # ELIMINACIÓN DEL NODO 12 (Sin dato 1, "MD5"):
    def test_send_product_deletion_23(self):

        input_file = JSON_TEST_PATH + "mytest23.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # MODIFICACIÓN DEL NODO 13 (Separador distinto de ','):
    def test_send_product_modification_24(self):

        input_file = JSON_TEST_PATH + "mytest24.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 14 (Dos etiquetas 2, "ContactEmail"):
    def test_send_product_duplication_25(self):

        input_file = JSON_TEST_PATH + "mytest25.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 14 (Sin etiqueta 2, "ContactEmail"):
    def test_send_product_deletion_26(self):

        input_file = JSON_TEST_PATH + "mytest26.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 16 (Dos datos 2, "email"):
    def test_send_product_duplication_27(self):

        input_file = JSON_TEST_PATH + "mytest27.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 16 (Sin dato 2, "email"):
    def test_send_product_deletion_28(self):

        input_file = JSON_TEST_PATH + "mytest28.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 17 (Dos comillas -> cubre el nodo 19, 21, 23, 24, 26, 28 y 30):
    def test_send_product_duplication_29(self):

        input_file = JSON_TEST_PATH + "mytest29.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 17 (Sin comillas -> cubre el nodo 19, 21, 23, 24, 26, 28 y 30):
    def test_send_product_deletion_30(self):

        input_file = JSON_TEST_PATH + "mytest30.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 18 (Dos nombre 1, OrderID):
    def test_send_product_duplication_31(self):

        input_file = JSON_TEST_PATH + "mytest31.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 18 (Sin nombre 1, OrderID):
    def test_send_product_deletion_32(self):

        input_file = JSON_TEST_PATH + "mytest32.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Wrong input file data: should have 'OrderID' and 'ContactEmail'", cm.exception.message)

if __name__ == '__main__':
    unittest.main()