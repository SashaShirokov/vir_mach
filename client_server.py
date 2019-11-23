from remote import Remote as r


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
