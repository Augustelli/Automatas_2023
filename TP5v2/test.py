from prueba import *
import unittest

class TestPrueba(unittest.TestCase):

    def test_id(self):
        self.assertEqual(validacion_id('758103'),True)
        self.assertEqual(validacion_id('1002266'),True)
        self.assertEqual(validacion_id('1100014'),True)

    def test_id_sesion(self):
        self.assertEqual(validacion_id_sesion('5AA0184E-000001CA'), True)
        self.assertEqual(validacion_id_sesion('00000019-00000082'), True)
        self.assertEqual(validacion_id_sesion('5C9CAF5E-0000032B'), True)



    def test_id_conexion_unico(self):
        self.assertEqual(validacion_id_conexion_unico('024e31f0ae19df90'), True)
        self.assertEqual(validacion_id_conexion_unico('9bc9bd9e47abb8dd'), True)
        self.assertEqual(validacion_id_conexion_unico('afbec1338dec1769'), True)


    def test_usuario(self):
        self.assertEqual(validacion_usuario('invitado-deca'), True)
        self.assertEqual(validacion_usuario('rezle-'), True)
        self.assertEqual(validacion_usuario('urez'), True)

    def test_ip_nas_ap(self):
        self.assertEqual(validacion_ip_nas_ap('192.168.247.11'), True)
        self.assertEqual(validacion_ip_nas_ap('192.168.247.20'), True)
        self.assertEqual(validacion_ip_nas_ap('192.168.247.18'), True)
    
    def test_inicio_de_conexion_dia(self):
        self.assertEqual(validacion_inicio_de_conexion_dia('2019-04-01'), True)
        self.assertEqual(validacion_inicio_de_conexion_dia('2019-04-02'), True)
        self.assertEqual(validacion_inicio_de_conexion_dia('2019-05-14'), True)

    def test_inicio_de_conexion_hora(self):
        self.assertEqual(validacion_inicio_de_conexion_hora('10:14:57'), True)
        self.assertEqual(validacion_inicio_de_conexion_hora('15:15:04'), True)
        self.assertEqual(validacion_inicio_de_conexion_hora('12:52:59'), True)

    def test_fin_de_conexion_dia(self):
        self.assertEqual(validacion_fin_de_conexion_dia('2019-03-14'), True)
        self.assertEqual(validacion_fin_de_conexion_dia('2019-03-28'), True)
        self.assertEqual(validacion_fin_de_conexion_dia('2020-02-28'), True)

    def test_fin_de_conexion_hora(self):
        self.assertEqual(validacion_fin_de_conexion_hora('10:15:34'), True)
        self.assertEqual(validacion_fin_de_conexion_hora('11:49:26'), True)
        self.assertEqual(validacion_fin_de_conexion_hora('08:53:16'), True)

    def test_session_time(self):
        self.assertEqual(validacion_session_time('3041'), True)
        self.assertEqual(validacion_session_time('259'), True)
        self.assertEqual(validacion_session_time('24856'), True)
    
    def test_mac_ap(self):
        self.assertEqual(validacion_mac_ap('DC-9F-DB-12-F3-EA:HCDD'), True)
        self.assertEqual(validacion_mac_ap('DC-9F-DB-12-F3-EA:HCDD'), True)
        self.assertEqual(validacion_mac_ap('04-18-D6-21-9B-4C:HCDD'), True)

    def test_mac_cliente(self):
        self.assertEqual(validacion_mac_cliente('B4-BF-F6-DD-78-C3'), True)
        self.assertEqual(validacion_mac_cliente('30-4B-07-8A-55-EA'), True)
        self.assertEqual(validacion_mac_cliente('50-82-D5-B0-28-D5'), True)


    


if __name__ == '__main__':
    unittest.main()
    