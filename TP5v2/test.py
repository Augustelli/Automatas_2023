from prueba import *
import unittest
from parameterized import parameterized


class TestPrueba(unittest.TestCase):

    @parameterized.expand([
        ('758103', True),
        ('1002266', True),
        ('1100014', True),
    ])
    def test_validacion_id(self, value, expected):
        self.assertEqual(validacion_id(value), expected)

    @parameterized.expand([
        ('5AA0184E-000001CA', True),
        ('00000019-00000082', True),
        ('5C9CAF5E-0000032B', True),
    ])
    def test_validacion_id_sesion(self, value, expected):
        self.assertEqual(validacion_id_sesion(value), expected)

    @parameterized.expand([
        ('024e31f0ae19df90', True),
        ('9bc9bd9e47abb8dd', True),
        ('afbec1338dec1769', True),
    ])
    def test_validacion_id_conexion_unico(self, value, expected):
        self.assertEqual(validacion_id_conexion_unico(value), expected)

    @parameterized.expand([
        ('invitado-deca', True),
        ('rezle-', True),
        ('urez', True),
        ('xabluce.ciero', True),
    ])
    def test_validacion_usuario(self, value, expected):
        self.assertEqual(validacion_usuario(value), expected)

    @parameterized.expand([
        ('192.168.247.11', True),
        ('192.168.247.20', True),
        ('192.168.247.18', True),
        ('192.168.1.20', True),
    ])
    def test_validacion_ip_nas_ap(self, value, expected):
        self.assertEqual(validacion_ip_nas_ap(value), expected)

    @parameterized.expand([
        ('2019-04-01', True),
        ('2019-04-02', True),
        ('2019-05-14', True),
        ('2021-01-11', True),
        ('2019/04-02', False),
        ('2019\05\14', False),
        ('2019/04/31', False),
        ('2019-05-29', True),
    ])
    def test_validacion_inicio_de_conexion_dia(self, value, expected):
        self.assertEqual(validacion_inicio_de_conexion_dia(value), expected)

    @parameterized.expand([
        ('10:14:57', True),
        ('15:15:04', True),
        ('12:52:59', True),
    ])
    def test_validacion_inicio_de_conexion_hora(self, value, expected):
        self.assertEqual(validacion_inicio_de_conexion_hora(value), expected)

    @parameterized.expand([
        ('2019-03-14', True),
        ('2019-03-28', True),
        ('2020-02-28', True),
        ('2019/04-02', False),
        ('2019\05\14', False),
        ('2019/04/31', False),
        ('2019-05-29', True),
    ])
    def test_validacion_fin_de_conexion_dia(self, value, expected):
        self.assertEqual(validacion_fin_de_conexion_dia(value), expected)

    @parameterized.expand([
        ('10:15:34', True),
        ('11:49:26', True),
        ('08:53:16', True),
    ])
    def test_validacion_fin_de_conexion_hora(self, value, expected):
        self.assertEqual(validacion_fin_de_conexion_hora(value), expected)

    @parameterized.expand([
        ('3041', True),
        ('259', True),
        ('24856', True),
    ])
    def test_validacion_session_time(self, value, expected):
        self.assertEqual(validacion_session_time(value), expected)

    @parameterized.expand([
        ('DC-9F-DB-12-F3-EA:HCDD', True),
        ('DC-9F-DB-12-F3-EA:HCDD', True),
        ('04-18-D6-21-9B-4C:HCDD', True),
    ])
    def test_validacion_mac_ap(self, value, expected):
        self.assertEqual(validacion_mac_ap(value), expected)

    @parameterized.expand([
        ('B4-BF-F6-DD-78-C3', True),
        ('30-4B-07-8A-55-EA', True),
        ('50-82-D5-B0-28-D5', True),
    ])
    def test_validacion_mac_cliente(self, value, expected):
        self.assertEqual(validacion_mac_cliente(value), expected)


if __name__ == '__main__':
    unittest.main()
