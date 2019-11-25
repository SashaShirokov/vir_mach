import unittest
import client_server as cs
from unittest.mock import patch


class TestClientServer(unittest.TestCase):

    def test_server(self):
        with patch('client_server.MyServer') as mocked_p:
            s = cs.MyServer('hosts.txt', 'passwords.txt')
            s2 = cs.MyServer('hosts.txt', 'passwords.txt')
            self.assertEqual((id(s) == id(s2)), True)

    def test_client(self):
        s = cs.MyClient('hosts.txt', 'passwords.txt')
        s2 = cs.MyClient('hosts.txt', 'passwords.txt')
        self.assertEqual((id(s) == id(s2)), False)
        self.assertEqual(isinstance(s, cs.MyClient), True)
        self.assertEqual(isinstance(s2, cs.MyClient), True)


if __name__ == '__main__':
    unittest.main()
