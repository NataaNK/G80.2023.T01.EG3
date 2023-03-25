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

        self.assertEqual("c7d0c3b0098a98d782981e6c5d7f5a2808dd0c6841dd12c1932e9ad9499b243c",
                         my_order.send_product(input_file))

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

        self.assertEqual("Wrong input file data: should have 'OrderID' and 'ContactEmail'",
                         cm.exception.message)

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

        self.assertEqual("Wrong input file data: should have 'OrderID' and 'ContactEmail'",
                         cm.exception.message)

    # ELIMINACIÓN DEL NODO 18 (Sin nombre 1, OrderID):
    def test_send_product_deletion_32(self):

        input_file = JSON_TEST_PATH + "mytest32.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Wrong input file data: should have 'OrderID' and 'ContactEmail'",
                         cm.exception.message)

    # MODIFICACIÓN DEL NODO 20 (Igualdad distinta de ':' -> cubre el nodo 27):
    def test_send_product_modification_33(self):

        input_file = JSON_TEST_PATH + "mytest33.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 22 (Dos valores 1, MD5):
    def test_send_product_duplication_34(self):

        input_file = JSON_TEST_PATH + "mytest34.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Order ID should be a MD5", cm.exception.message)

    # ELIMINACIÓN DEL NODO 22 (Sin valor 1, MD5):
    def test_send_product_deletion_35(self):

        input_file = JSON_TEST_PATH + "mytest35.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Order ID should be a MD5", cm.exception.message)

    # DUPLICACIÓN DEL NODO 25 (Dos nombres 2, ContactEmail):
    def test_send_product_duplication_36(self):

        input_file = JSON_TEST_PATH + "mytest36.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Wrong input file data: should have 'OrderID' and 'ContactEmail'",
                         cm.exception.message)

    # ELIMINACIÓN DEL NODO 25 (Sin nombre 2, ContactEmail):
    def test_send_product_deletion_37(self):

        input_file = JSON_TEST_PATH + "mytest37.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Wrong input file data: should have 'OrderID' and 'ContactEmail'",
                         cm.exception.message)

    # DUPLICACIÓN DEL NODO 29 (Dos valores 2, email):
    def test_send_product_duplication_38(self):

        input_file = JSON_TEST_PATH + "mytest38.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Invalid Email Format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 29 (Sin valor 2, email):
    def test_send_product_deletion_39(self):

        input_file = JSON_TEST_PATH + "mytest39.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Invalid Email Format", cm.exception.message)

    # MODIFICACIÓN DEL NODO 31 (Otro valor en vez de '"' -> cubre el nodo 33, 34, 36, 37, 39, 40 y 46):
    def test_send_product_modification_40(self):

        input_file = JSON_TEST_PATH + "mytest40.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Json Decode Error - Wrong Json format", cm.exception.message)

    # MODIFICACIÓN DEL NODO 32 (Otro nombre 1 que no sea OrderID):
    def test_send_product_modification_41(self):

        input_file = JSON_TEST_PATH + "mytest41.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Wrong input file data: should have 'OrderID' and 'ContactEmail'",
                         cm.exception.message)

    # MODIFICACIÓN DEL NODO 35 (Valor 1 que no sea un MD5):
    def test_send_product_modification_42(self):

        input_file = JSON_TEST_PATH + "mytest42.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Order ID should be a MD5", cm.exception.message)

    # MODIFICACIÓN DEL NODO 38 (Nombre 2 distinto de ContactEmail):
    def test_send_product_modification_43(self):

        input_file = JSON_TEST_PATH + "mytest43.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Wrong input file data: should have 'OrderID' and 'ContactEmail'",
                         cm.exception.message)

    # DUPLICACIÓN DEL NODO 41 (Dos veces el nombre de un email):
    @freeze_time("2023-03-09")
    def test_send_product_duplication_44_valid_2(self):

        input_file = JSON_TEST_PATH + "mytest44.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        self.assertEqual("c7d0c3b0098a98d782981e6c5d7f5a2808dd0c6841dd12c1932e9ad9499b243c",
                         my_order.send_product(input_file))

    # ELIMINACIÓN DEL NODO 41 (Sin nombre del email):
    def test_send_product_deletion_45(self):

        input_file = JSON_TEST_PATH + "mytest45.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Invalid Email Format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 42 (Dos '@' en el email):
    def test_send_product_duplication_46(self):

        input_file = JSON_TEST_PATH + "mytest46.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Invalid Email Format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 42 (Sin '@' en el email):
    def test_send_product_deletion_47(self):

        input_file = JSON_TEST_PATH + "mytest47.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Invalid Email Format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 43 (Dos veces el nombre de un dominio):
    @freeze_time("2023-03-09")
    def test_send_product_duplication_48_valid_3(self):

        input_file = JSON_TEST_PATH + "mytest48.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        self.assertEqual("c7d0c3b0098a98d782981e6c5d7f5a2808dd0c6841dd12c1932e9ad9499b243c",
                         my_order.send_product(input_file))

    # ELIMINACIÓN DEL NODO 43 (Sin dominio en el email):
    def test_send_product_deletion_49(self):

        input_file = JSON_TEST_PATH + "mytest49.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Invalid Email Format", cm.exception.message)

    # DUPLICACIÓN DEL NODO 44 (Dos '.' en el email):
    def test_send_product_duplication_50(self):

        input_file = JSON_TEST_PATH + "mytest50.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Invalid Email Format", cm.exception.message)







    # DUPLICACIÓN DEL NODO 45 (Dos veces una extensión de prueba de 3 letras, en este caso no
    # será válido porque superará el máximo de tres letras):
    def test_send_product_duplication_52(self):
        input_file = JSON_TEST_PATH + "mytest52.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Invalid Email Format", cm.exception.message)

    # ELIMINACIÓN DEL NODO 45 (Sin extensión en el email):
    def test_send_product_deletion_53(self):
        input_file = JSON_TEST_PATH + "mytest53.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Invalid Email Format", cm.exception.message)

    # MODIFICACIÓN DEL NODO 47 (Usamos de prueba cambiar el nombre del email por un caracter
    # distinto de letras o numeros, por ello, en este caso no será válido):
    def test_send_product_modification_54(self):
        input_file = JSON_TEST_PATH + "mytest54.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Invalid Email Format", cm.exception.message)

    # MODIFICACIÓN DEL NODO 48 (Símbolo distinto que '@')
    def test_send_product_modification_55(self):
        input_file = JSON_TEST_PATH + "mytest55.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Invalid Email Format", cm.exception.message)

    # MODIFICACIÓN DEL NODO 49 (Usamos de prueba cambiar el dominio del email por un
    # caracter distinto de letras, por ello, en este caso no será válido):
    def test_send_product_modification_56(self):
        input_file = JSON_TEST_PATH + "mytest56.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Invalid Email Format", cm.exception.message)








    # MODIFICACIÓN DEL NODO 51 (Usamos en este caso una prueba que cambia la extensión
    # del email por algo distinto de letras, por ello, no será válido):
    def test_send_product_modification_58(self):
        input_file = JSON_TEST_PATH + "mytest58.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Invalid Email Format", cm.exception.message)

    # VALORES LÍMITE y CLASES DE EQUIVALENCIA

    # MODIFICACIÓN DEL NODO 35 (MD5 no válido de 31 dígitos)
    def test_send_product_modification_VL_59(self):

        input_file = JSON_TEST_PATH + "mytest59.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Order ID should be a MD5", cm.exception.message)

    # MODIFICACIÓN DEL NODO 35 (MD5 no válido de 33 dígitos)
    def test_send_product_modification_VL_60(self):

        input_file = JSON_TEST_PATH + "mytest60.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Order ID should be a MD5", cm.exception.message)

    # MODIFICACIÓN DEL NODO 35 (MD5 no válido de 32 dígitos NO hexadecimal)
    def test_send_product_modification_CE_61(self):

        input_file = JSON_TEST_PATH + "mytest61.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Order ID should be a MD5", cm.exception.message)

    # MODIFICACIÓN DEL NODO 51 (Dominio de 1 letra)
    @freeze_time("2023-03-09")
    def test_send_product_modification_VL_62_valid_4(self):

        input_file = JSON_TEST_PATH + "mytest62.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        self.assertEqual("c7d0c3b0098a98d782981e6c5d7f5a2808dd0c6841dd12c1932e9ad9499b243c",
                         my_order.send_product(input_file))

    # MODIFICACIÓN DEL NODO 51 (Dominio de 2 letras)
    @freeze_time("2023-03-09")
    def test_send_product_modification_VL_63_valid_5(self):

        input_file = JSON_TEST_PATH + "mytest63.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        self.assertEqual("c7d0c3b0098a98d782981e6c5d7f5a2808dd0c6841dd12c1932e9ad9499b243c",
                         my_order.send_product(input_file))

    # MODIFICACIÓN DEL NODO 51 (Dominio de 4 letras)
    def test_send_product_modification_VL_64(self):

        input_file = JSON_TEST_PATH + "mytest64.json"

        my_order = OrderManager()
        my_order.register_order(ORDER_DATA[0], ORDER_DATA[1], ORDER_DATA[2], ORDER_DATA[3],
                                ORDER_DATA[4])

        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(input_file)

        self.assertEqual("Invalid Email Format", cm.exception.message)



if __name__ == '__main__':
    unittest.main()