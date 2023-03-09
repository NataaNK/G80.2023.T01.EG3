"""class for testing the regsiter_order method"""
import unittest
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""

    # Habria que fijar el time.stamp sino da un código distinto cada vez
    # pero si lo hacemos en el codigo no funcionara más
    # HACEMOS UN MOCKING:
    @freeze_time("2023-03-09")
    def test_register_order_ok_1(self):
        my_order = OrderManager()
        my_value = my_order.register_order(product_Id="3662168005326", address="calle colmenarejo",
                   zip_code="28345", phone="123456789", order_types="premium")
        self.assertEqual(my_value, "01da32c860838bff 48130F48f8b22D56")

    # Hay que comprobar también que se guarda en un fichero, para comprobar
    # que el fichero no ha cambiado hacemos un hash del fichero y si es el mismo
    # no ha cambiado
    def test_register_order_ok_1(self):


    def test_register_order_nok_1(self):
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.register_order(product_id="3662168005326a", address="calle colmenarejo",
                     order_type="premium", phone="123456789", zip_code="28345")

        self.assertEqual(cm.exception.message, "Invalid EAN13 code string")


if __name__ == '__main__':
    unittest.main()
