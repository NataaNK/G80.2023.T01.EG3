"""Autores: Natalia Rodríguez Navarro, Alberto Penas Díaz

test_deliver_product_tests.py: Clase para testear el método deliver_product()
de OrderManager"""

import unittest
import shutil
import json
import os
from pathlib import Path
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

class TestDeliverProduct(unittest.TestCase):
    """
    Clase para testear el método deliver_product()
    de OrderManager
    """
    def test_deliver_product_ok_1(self):
        """
        Path = 1_2_4_7_8_10_11_13_15_16_18_19_22_23_24: Caso válido en el que ya existe
        información en el store_deliveries.json y el order type es PREMIUM
        """
        my_delivery = OrderManager()
        # El método debe devolver True
        self.assertTrue(my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                                    "08dd0c6841dd12c1932e9ad9499b243c"))

        # Ahora, comprobamos que los datos que se han metido en el json son los correctos.
        # Abrimos el fichero que guarda la información de las entregas
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_deliveries.json",
                  "r", encoding="UTF-8", newline="") as file:
            deliveries = json.load(file)

        found = False
        i = 0
        while not found and i < len(deliveries):
            item = deliveries[i]
            if (item["_OrderDelivery__delivery_day"] == 1678406400.0
                    and item["_OrderDelivery__tracking_code"] ==
                        "c7d0c3b0098a98d782981e6c5d7f5a2808dd0c6841dd12c1932e9ad9499b243c"):
                found = True
            i += 1

        self.assertTrue(found)


    def test_deliver_product_nok_2(self):
        """
        Path = 1_3: El SHA-256 de entrada no es válido
        """
        my_delivery = OrderManager()

        with self.assertRaises(OrderManagementException) as order_except:
            my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                        "08dd0c6841dd12c1932e9ad9499b243")

        self.assertEqual("Tracking Code should be a SHA256", order_except.exception.message)


    def test_deliver_product_nok_3(self):
        """
        Path = 1_2_5: El almacén store_shipping_order no existe
        """
        # Eliminamos el fichero para realizar el test
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json",
                  "r", encoding="UTF-8", newline="") as file:
            shippings = json.load(file)

        if os.path.isfile(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                             "json_files/store_shipping_order.json"):
            os.remove(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                             "json_files/store_shipping_order.json")

        my_delivery = OrderManager()

        with self.assertRaises(OrderManagementException) as order_except:
            my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                        "08dd0c6841dd12c1932e9ad9499b243c")

        self.assertEqual("Wrong store shipping file path", order_except.exception.message)

        # Volvemos a generar el fichero que existía antes
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json", "w",
                  encoding="UTF-8", newline="") as file:
            json.dump(shippings, file, indent=2)


    def test_deliver_product_nok_4(self):
        """
        Path = 1_2_6: No se puede decodificar el store_shipping_order.json
        """

        # Guardo la información del fichero antes de modificarlo
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json",
                  "r", encoding="UTF-8", newline="") as file:
            shippings = json.load(file)

        # Copiamos contenido de un json no decodificable en store_shipping_order para
        # que nos salte la excepción
        shutil.copy(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                       "json_files/json_tests/mytest1_delivery.json",
                    str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                       "json_files/store_shipping_order.json")

        my_delivery = OrderManager()

        with self.assertRaises(OrderManagementException) as order_except:
            my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                        "08dd0c6841dd12c1932e9ad9499b243c")

        self.assertEqual("Json Decode Error - Wrong Json format", order_except.exception.message)

        if os.path.isfile(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                             "json_files/store_shipping_order.json"):
            os.remove(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src"
                                             "/json_files/store_shipping_order.json")

        # Volvemos a generar el fichero que existía antes
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json", "w",
                  encoding="UTF-8", newline="") as file:
            json.dump(shippings, file, indent=2)


    def test_deliver_product_nok_5(self):
        """
        Path = 1_2_4_8_9: No entramos en el bucle para buscar el envío ya que el almacén
        está vacío
        """

        # Salvaguardamos la información que había en el almacén
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json",
                  "r", encoding="UTF-8", newline="") as file:
            shippings = json.load(file)

        # Vacíamos el almacén
        new_list = []
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json", "w",
                  encoding="UTF-8", newline="") as file:
            json.dump(new_list, file, indent=2)

        my_delivery = OrderManager()

        with self.assertRaises(OrderManagementException) as order_except:
            my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                        "08dd0c6841dd12c1932e9ad9499b243c")

        self.assertEqual("Shipping Order not Found", order_except.exception.message)

        if os.path.isfile(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                             "json_files/store_shipping_order.json"):
            os.remove(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                             "json_files/store_shipping_order.json")

        # Volvemos a generar el fichero que existía antes
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json", "w",
                  encoding="UTF-8", newline="") as file:
            json.dump(shippings, file, indent=2)


    def test_deliver_product_nok_6(self):
        """
        Path = 1_2_4_7_8_9: El SHA-256 de entrada no está en la lista de store_deliveries
        """
        my_delivery = OrderManager()

        with self.assertRaises(OrderManagementException) as order_except:
            my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                        "08dd0c6841dd12c1932e9ad9499b243d")

        self.assertEqual("Shipping Order not Found", order_except.exception.message)


    def test_deliver_product_ok_7(self):
        """
        Path = 1_2_4_7_8_10_12_13_15_16_18_19_22_23_24: Caso válido en el que ya existe
        información en el store_deliveries.json y el order type es REGULAR
        """
        my_delivery = OrderManager()
        # La función debe delvolver True
        self.assertTrue(my_delivery.deliver_product("ebf15a34d6451a7314a74ac395bfcc3d"
                                                    "00e5e34a0fafe51fe9e1d0680928294d"))

        # Ahora, comprobamos que los datos que se han metido en el json son los correctos.
        # Abrimos el fichero que guarda la información de las entregas
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_deliveries.json",
                  "r", encoding="UTF-8", newline="") as file:
            deliveries = json.load(file)

        found = False
        i = 0
        while not found and i < len(deliveries):
            item = deliveries[i]
            if (item["_OrderDelivery__delivery_day"] == 1678924800.0
                    and item["_OrderDelivery__tracking_code"] ==
                        "ebf15a34d6451a7314a74ac395bfcc3d00e5e34a0fafe51fe9e1d0680928294d"):
                found = True
            i += 1

        self.assertTrue(found)

    def test_deliver_product_nok_8(self):
        """
        Path = 1_2_4_7_8_10_11_13_14: Delivery day inválido porque
        delivery_day != my_delivery_day
        """

        # Guardo la información del fichero antes de modificarlo
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json",
                  "r", encoding="UTF-8", newline="") as file:
            shippings = json.load(file)

        # Copiamos contenido de un json con un delivery day inválido en store_shipping_order para
        # que nos salte la excepción
        shutil.copy(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                       "json_files/json_tests/mytest2_delivery.json",
            str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                               "json_files/store_shipping_order.json")

        my_delivery = OrderManager()

        with self.assertRaises(OrderManagementException) as order_except:
            my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                        "08dd0c6841dd12c1932e9ad9499b243c")

        self.assertEqual("Invalid Delivery Day", order_except.exception.message)

        if os.path.isfile(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                             "json_files/store_shipping_order.json"):
            os.remove(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                             "json_files/store_shipping_order.json")

        # Volvemos a generar el fichero que existía antes
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json", "w",
                  encoding="UTF-8", newline="") as file:
            json.dump(shippings, file, indent=2)

    @freeze_time("2023-01-01")
    def test_deliver_product_nok_9(self):
        """
        Path = 1_2_4_7_8_10_11_13_15_14: Delivery day inválido porque
        delivery_day > hoy
        """
        my_delivery = OrderManager()

        with self.assertRaises(OrderManagementException) as order_except:
            my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                        "08dd0c6841dd12c1932e9ad9499b243c")

        self.assertEqual("Invalid Delivery Day", order_except.exception.message)


    def test_deliver_product_nok_10(self):
        """
        Path = 1_2_4_7_8_10_11_13_15_16_17: Corrupt SHA-256, no coincide el generado con el
        registrado
        """

        # Guardo la información del fichero antes de modificarlo
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json",
                  "r", encoding="UTF-8", newline="") as file:
            shippings = json.load(file)

        # Copiamos contenido de un json con datos modificados para que el SHA-256 no coincida
        # con los datos y salte la excepción
        shutil.copy(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                       "json_files/json_tests/mytest3_delivery.json",
            str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                               "json_files/store_shipping_order.json")

        my_delivery = OrderManager()

        with self.assertRaises(OrderManagementException) as order_except:
            my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                        "08dd0c6841dd12c1932e9ad9499b243c")

        self.assertEqual("Invalid or Corrupt SHA-256 Code", order_except.exception.message)

        if os.path.isfile(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                             "json_files/store_shipping_order.json"):
            os.remove(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                         "json_files/store_shipping_order.json")

        # Volvemos a generar el fichero que existía antes
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json", "w",
                  encoding="UTF-8", newline="") as file:
            json.dump(shippings, file, indent=2)


    def test_deliver_product_ok_11(self):
        """
        Path = 1_2_4_7_8_10_11_13_15_16_18_20_23_24: Caso válido en el que aún no existe
        el almacén store_deliveries.json y hay que crearlo
        """

        # Salvaguardamos la información del fichero y lo eliminamos si existe
        deliveries = None
        if os.path.isfile(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                             "json_files/store_deliveries.json"):
            with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                         "json_files/store_deliveries.json",
                      "r", encoding="UTF-8", newline="") as file:
                deliveries = json.load(file)
            os.remove(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                         "json_files/store_deliveries.json")

        my_delivery = OrderManager()
        # La función debe delvolver True
        self.assertTrue(my_delivery.deliver_product("4bab3094ecf6f34afe70c175a3e2ffaf"
                                                    "c407a59056eb5cccb4232158deb64dae"))

        # Ahora, comprobamos que los datos que se han metido en el json son los correctos.
        # Abrimos el fichero que guarda la información de las entregas
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_deliveries.json",
                  "r", encoding="UTF-8", newline="") as file:
            my_deliveries = json.load(file)

        found = False
        i = 0
        while not found and i < len(my_deliveries):
            item = my_deliveries[i]
            if (item["_OrderDelivery__delivery_day"] == 1678406400.0
                    and item["_OrderDelivery__tracking_code"] ==
                        "4bab3094ecf6f34afe70c175a3e2ffafc407a59056eb5cccb4232158deb64dae"):
                found = True
            i += 1

        self.assertTrue(found)

        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_deliveries.json",
                  "r", encoding="UTF-8", newline="") as file:
            new_deliveries = json.load(file)

        if os.path.isfile(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                             "json_files/store_deliveries.json"):
            os.remove(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                         "json_files/store_deliveries.json")
        # Rescatamos la información que había anteriormente en el archivo
        if deliveries:
            if new_deliveries[0] not in deliveries:
                deliveries.append(new_deliveries[0])

        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_deliveries.json", "w",
                  encoding="UTF-8", newline="") as file:
            json.dump(deliveries, file, indent=2)

    def test_deliver_product_nok_12(self):
        """
        Path = 1_2_4_7_8_10_11_13_15_16_18_21: Existe store_deliveries pero no es decodificable
        """

        # Guardo la información del fichero antes de modificarlo
        existia = True
        if os.path.isfile(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                             "json_files/store_deliveries.json"):
            with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                         "json_files/store_deliveries.json",
                      "r", encoding="UTF-8", newline="") as file:
                deliveries = json.load(file)
        else:
            existia = False
            with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                         "json_files/store_deliveries.json", "w",
                      encoding="UTF-8", newline="") as file:
                json.dump(["eliminable"], file, indent=2)

        # Copiamos contenido de un json con datos modificados para que no sean decodificables
        shutil.copy(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                       "json_files/json_tests/mytest1_delivery.json",
            str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                               "json_files/store_deliveries.json")

        my_delivery = OrderManager()

        with self.assertRaises(OrderManagementException) as order_except:
            my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                        "08dd0c6841dd12c1932e9ad9499b243c")

        self.assertEqual("Json Decode Error - Wrong Json format", order_except.exception.message)

        if os.path.isfile(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                             "json_files/store_deliveries.json"):
            os.remove(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                         "json_files/store_deliveries.json")

        # Volvemos a generar el fichero que existía antes
        if existia:
            with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                         "json_files/store_deliveries.json", "w",
                      encoding="UTF-8", newline="") as file:
                json.dump(deliveries, file, indent=2)

    def test_deliver_product_ok_13(self):
        """
        Path = 1_2_4_7_8_10_11_13_15_16_18_19_23_24: Caso válido en el que ya existe
        información en el store_deliveries.json y el pedido ya está registrado
        """
        my_delivery_repetido = OrderManager()
        my_delivery = OrderManager()
        # Nos aseguramos que el pedido está antes en la lista de pedidos entregados
        my_delivery_repetido.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                             "08dd0c6841dd12c1932e9ad9499b243c")
        # El método debe devolver True
        self.assertTrue(my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                                    "08dd0c6841dd12c1932e9ad9499b243c"))

        # Ahora, comprobamos que los datos que se han metido en el json son los correctos.
        # Abrimos el fichero que guarda la información de las entregas
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_deliveries.json",
                  "r", encoding="UTF-8", newline="") as file:
            deliveries = json.load(file)

        found = False
        i = 0
        while not found and i < len(deliveries):
            item = deliveries[i]
            if (item["_OrderDelivery__delivery_day"] == 1678406400.0
                    and item["_OrderDelivery__tracking_code"] ==
                        "c7d0c3b0098a98d782981e6c5d7f5a2808dd0c6841dd12c1932e9ad9499b243c"):
                found = True
            i += 1

        self.assertTrue(found)

    def test_deliver_product_ok_14(self):
        """
        Pasa por el bucle 1 vez
        """
        # Guardo la información del fichero antes de modificarlo
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json",
                  "r", encoding="UTF-8", newline="") as file:
            shippings = json.load(file)

        # Copiamos contenido de un json que contenga la información del envío el primero
        shutil.copy(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                       "json_files/json_tests/mytest4_delivery.json",
            str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                               "json_files/store_shipping_order.json")

        my_delivery = OrderManager()

        self.assertTrue(my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                                    "08dd0c6841dd12c1932e9ad9499b243c"))

        # Ahora, comprobamos que los datos que se han metido en el json son los correctos.
        # Abrimos el fichero que guarda la información de las entregas
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_deliveries.json",
                  "r", encoding="UTF-8", newline="") as file:
            deliveries = json.load(file)

        found = False
        i = 0
        while not found and i < len(deliveries):
            item = deliveries[i]
            if (item["_OrderDelivery__delivery_day"] == 1678406400.0
                    and item["_OrderDelivery__tracking_code"] ==
                    "c7d0c3b0098a98d782981e6c5d7f5a2808dd0c6841dd12c1932e9ad9499b243c"):
                found = True
            i += 1

        self.assertTrue(found)

        if os.path.isfile(
                str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                   "json_files/store_shipping_order.json"):
            os.remove(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                         "json_files/store_shipping_order.json")

        # Volvemos a generar el fichero que existía antes
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json", "w",
                  encoding="UTF-8", newline="") as file:
            json.dump(shippings, file, indent=2)

    def test_deliver_product_ok_15(self):
        """
        Pasa por el bucle 2 veces
        """

        # Guardo la información del fichero antes de modificarlo
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json",
                  "r", encoding="UTF-8", newline="") as file:
            shippings = json.load(file)

        # Copiamos contenido de un json que contenga la información del envío en el
        # segundo lugar de la lista
        shutil.copy(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                       "json_files/json_tests/mytest5_delivery.json",
            str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                               "json_files/store_shipping_order.json")

        my_delivery = OrderManager()

        self.assertTrue(my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                                    "08dd0c6841dd12c1932e9ad9499b243c"))

        # Ahora, comprobamos que los datos que se han metido en el json son los correctos.
        # Abrimos el fichero que guarda la información de las entregas
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_deliveries.json",
                  "r", encoding="UTF-8", newline="") as file:
            deliveries = json.load(file)

        found = False
        i = 0
        while not found and i < len(deliveries):
            item = deliveries[i]
            if (item["_OrderDelivery__delivery_day"] == 1678406400.0
                    and item["_OrderDelivery__tracking_code"] ==
                        "c7d0c3b0098a98d782981e6c5d7f5a2808dd0c6841dd12c1932e9ad9499b243c"):
                found = True
            i += 1

        self.assertTrue(found)

        if os.path.isfile(
                str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                   "json_files/store_shipping_order.json"):
            os.remove(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                         "json_files/store_shipping_order.json")

        # Volvemos a generar el fichero que existía antes
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json", "w",
                  encoding="UTF-8", newline="") as file:
            json.dump(shippings, file, indent=2)

    def test_deliver_product_ok_16(self):
        """
        Pasa por el bucle max-1 veces. Es decir, buscamos un envío que está el penúltimo
        en el store_shippings, ya que el número máximo de veces que podríamos pasar por el
        bucle es el tamño de la lista en el store_shippings
        """

        # Guardo la información del fichero antes de modificarlo
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json",
                  "r", encoding="UTF-8", newline="") as file:
            shippings = json.load(file)

        # Copiamos contenido de un json que contenga la información del envío en el
        # penúltimo lugar de la lista
        shutil.copy(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                       "json_files/json_tests/mytest6_delivery.json",
            str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                               "json_files/store_shipping_order.json")

        my_delivery = OrderManager()

        self.assertTrue(my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                                    "08dd0c6841dd12c1932e9ad9499b243c"))

        # Ahora, comprobamos que los datos que se han metido en el json son los correctos.
        # Abrimos el fichero que guarda la información de las entregas
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_deliveries.json",
                  "r", encoding="UTF-8", newline="") as file:
            deliveries = json.load(file)

        found = False
        i = 0
        while not found and i < len(deliveries):
            item = deliveries[i]
            if (item["_OrderDelivery__delivery_day"] == 1678406400.0
                    and item["_OrderDelivery__tracking_code"] ==
                        "c7d0c3b0098a98d782981e6c5d7f5a2808dd0c6841dd12c1932e9ad9499b243c"):
                found = True
            i += 1

        self.assertTrue(found)

        if os.path.isfile(
                str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                   "json_files/store_shipping_order.json"):
            os.remove(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                         "json_files/store_shipping_order.json")

        # Volvemos a generar el fichero que existía antes
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json", "w",
                  encoding="UTF-8", newline="") as file:
            json.dump(shippings, file, indent=2)

    def test_deliver_product_ok_17(self):
        """
        Pasa por el bucle max veces. Es decir, buscamos un envío que está el último
        en el store_shippings
        """

        # Guardo la información del fichero antes de modificarlo
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json",
                  "r", encoding="UTF-8", newline="") as file:
            shippings = json.load(file)

        # Copiamos contenido de un json que contenga la información del envío en el
        # último lugar de la lista
        shutil.copy(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                       "json_files/json_tests/mytest7_delivery.json",
            str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                               "json_files/store_shipping_order.json")

        my_delivery = OrderManager()

        self.assertTrue(my_delivery.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a28"
                                                    "08dd0c6841dd12c1932e9ad9499b243c"))

        # Ahora, comprobamos que los datos que se han metido en el json son los correctos.
        # Abrimos el fichero que guarda la información de las entregas
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_deliveries.json",
                  "r", encoding="UTF-8", newline="") as file:
            deliveries = json.load(file)

        found = False
        i = 0
        while not found and i < len(deliveries):
            item = deliveries[i]
            if (item["_OrderDelivery__delivery_day"] == 1678406400.0
                    and item["_OrderDelivery__tracking_code"] ==
                        "c7d0c3b0098a98d782981e6c5d7f5a2808dd0c6841dd12c1932e9ad9499b243c"):
                found = True
            i += 1

        self.assertTrue(found)

        if os.path.isfile(
                str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                   "json_files/store_shipping_order.json"):
            os.remove(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                         "json_files/store_shipping_order.json")

        # Volvemos a generar el fichero que existía antes
        with open(str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/"
                                     "json_files/store_shipping_order.json", "w",
                  encoding="UTF-8", newline="") as file:
            json.dump(shippings, file, indent=2)

if __name__ == '__main__':
    unittest.main()
