import unittest
import database as db
import helpers
import copy
import config
import csv

import sys
import os

# Añade la carpeta raíz del proyecto al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora se pueden importar correctamente
from gestor import database as db
from gestor import helpers
from gestor import config

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('15J', 'Marta', 'Pérez'),
            db.Cliente('48H', 'Manolo', 'López'),
            db.Cliente('28Z', 'Ana', 'García'),
        ]

    def test_buscar_cliente(self):
        self.assertIsNotNone(db.Clientes.buscar('15J'))
        self.assertIsNone(db.Clientes.buscar('99X'))

    def test_crear_cliente(self):
        nuevo = db.Clientes.crear('39X', 'Héctor', 'Costa')
        self.assertEqual(nuevo.nombre, 'Héctor')

    def test_modificar_cliente(self):
        copia = copy.copy(db.Clientes.buscar('28Z'))
        modificado = db.Clientes.modificar('28Z', 'Mariana', 'Pérez')
        self.assertNotEqual(copia.nombre, modificado.nombre)

    def test_borrar_cliente(self):
        db.Clientes.borrar('48H')
        self.assertIsNone(db.Clientes.buscar('48H'))

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('23223S', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('48H', db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar('48H')
        db.Clientes.modificar('28Z', 'Mariana', 'Pérez')
        with open(config.DATABASE_PATH, newline="\n") as f:
            reader = csv.reader(f, delimiter=";")
            row = next(reader)
        self.assertEqual(row[0], '28Z')
        self.assertEqual(row[1], 'Mariana')
        self.assertEqual(row[2], 'Pérez')

if __name__ == '__main__':
    unittest.main()
