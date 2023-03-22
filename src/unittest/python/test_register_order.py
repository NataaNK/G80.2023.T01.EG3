"""class for testing the regsiter_order method"""
import unittest
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
        my_order = OrderManager()
        my_value = my_order.register_order("8435464158875", "premium", "Calle colmenarejo",
                                           "123456789", "28345")
        self.assertEqual("01da32c860838bff48130F48f8b22D56", my_value)

    # Hay que comprobar también que se guarda en un fichero, para comprobar
    # que el fichero no ha cambiado hacemos un hash del fichero y si es el mismo
    # no ha cambiado


if __name__ == '__main__':
    unittest.main()
