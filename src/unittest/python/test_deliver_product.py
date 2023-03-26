"""Autores: Natalia Rodríguez Navarro, Alberto Penas Díaz

test_deliver_product.py: Clase para testear el método deliver_product()
de OrderManager"""

from unittest import TestCase
import json
import os
from pathlib import Path
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

class TestDeliverProduct(TestCase):
    @freeze_time("2023-03-09")
    def test_deliver_product(self):
        # CÓDIGO DE PRUEBA. PARA PROBAR EL FUNCIONAMIENTO DE RF3
        prueba = OrderManager()
        prueba.deliver_product("c7d0c3b0098a98d782981e6c5d7f5a2808dd0c6841dd12c1932e9ad9499b243c")

        prueba2 = OrderManager()
        prueba2.deliver_product("59adf8977b25f2ba3d4e989c51ac1f6dfce29544fe01bc84770f9afad42290ee")

        prueba3 = OrderManager()
        prueba3.deliver_product("ebf15a34d6451a7314a74ac395bfcc3d00e5e34a0fafe51fe9e1d0680928294d")
