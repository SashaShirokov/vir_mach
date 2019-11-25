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


class MyClient(object):
    def __init__(self, hostfile, passfile):
        self.hostfile = hostfile
        self.passfile = passfile

    def run(self):
        self.client = r(self.hostfile, self.passfile)
