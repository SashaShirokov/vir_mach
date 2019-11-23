from remote import Remote as r
import json


class MyServer(object):
    _instance = None

    def __new__(self, hostfile, passfile):
        self.hostfile = hostfile
        self.passfile = passfile
        if not self._instance:
            self._instance = super(MyServer, self).__new__(self)
            self.server = r(self.hostfile, self.passfile)
        return self._instance


s = MyServer('hosts.txt', 'passwords.txt')

with open('result.txt', 'w') as f:
    f.write(s.server.execute())


with open('result.txt', 'r') as f:
    res = []
    res_json = {}
    a = f.read().split('\n')
    for i, l in enumerate(a):
        if i == 4 or i == len(a) - 2:
            res.append(l)
    for i, l in enumerate(res):
        d = l.split()
        if i == 0:
            res_json['serverIP'] = d[3]
            res_json['clientIP'] = d[8]
        else:
            res_json['Interval'] = d[2]
            res_json['Transfer'] = d[4]
            res_json['Bandwidth'] = d[6]
    print(res_json)
