import unittest
from app import api
from flask import url_for


class IpFondTestCase(unittest.TestCase):
    def setUp(self):
        self.app_context = api.test_request_context()
        self.app_context.push()
        self.client = api.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exist(self):
        self.assertIsNotNone(api, 'Api is None!')

    def test_get_one_ip_e(self):
        re = self.client.post(url_for('get_one_ip'), json={'ip': 'wrong'})
        self.assertEqual(re.status_code, 400)
        js = re.get_json()
        self.assertEqual(js['detail']['json']['ip'][0], '"wrong" is not a right IPV4 address', 'Wrong message test failed!')

    def test_get_one_ip_r(self):
        re = self.client.post(url_for('get_one_ip'), json={'ip': '1.1.1.1'})
        self.assertEqual(re.status_code, 200)
        js = re.get_json()
        self.assertIn('ip_from', js, 'Get one ip return structure test failed!')

    def test_get_ips_e(self):
        re = self.client.post(url_for('get_ips'), json={'ips': ['1.1.1.1', 'wrong', '9.9.9.9']})
        self.assertEqual(re.status_code, 400)
        js = re.get_json()
        self.assertEqual(js['detail']['json']['ips']['1'][0], '"wrong" is not a right IPV4 address', 'Wrong message test failed!')

    def test_get_ips_r(self):
        re = self.client.post(url_for('get_ips'), json={'ips': ['1.1.1.1', '8.8.8.8', '9.9.9.9']})
        self.assertEqual(re.status_code, 200)
        js = re.get_json()
        self.assertIn('ip_from', js, 'Get ips return structure test failed!')
        self.assertEqual(type(['aa']), type(js['ip_from']), 'Get ips return structure test failed!')
        self.assertEqual(3, len(js['ip_from']), 'Get ips return structure test failed!')

    def test_about(self):
        re = self.client.get(url_for('get_about'))
        self.assertEqual(re.status_code, 200)
        te = re.get_json()
        self.assertIn('纯真网络 ', te['about'])

if __name__ == '__main__':
    unittest.main()
