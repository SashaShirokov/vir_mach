import sys
sys.path.append('/home/aliaksandr/Desktop/Python/vir_mach/source')

import unittest
from unittest.mock import patch
import subprocess
import remote as r
import client_server as cs


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

#
# class TestRemote(unittest.TestCase):
#
#     def test_remote(self):
#         with patch('remote.Remote') as mocked_p:
#             p = r.Remote('hosts.txt', 'passwords.txt')
#             self.assertEqual(isinstance(p, tuple(r.Remote)), True)


print(sys.path)
if __name__ == '__main__':
    unittest.main()
