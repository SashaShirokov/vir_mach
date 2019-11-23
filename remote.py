import subprocess
import getpass


class Remote():
    def __init__(self, host=None, pswfile=None, command=None):
        if host == None:
            self.host = input('Enter a host: ')
        else:
            with open(host, 'r') as f:
                self.host = f.read()[:-1]

        if pswfile == None:
            self.mode = '-p'
            self.password = getpass.getpass("Password: ")
        else:
            self.pswfile = pswfile
            self.mode = '-f'

        if command == None:
            self.type_command = input('Enter ssh for ssh command or scp for scp command: ')
            if self.type_command == 'scp':
                self.command = input('Enter a source and destination: ').split()
            else:
                self.command = input('Enter a command: ').split()

        self.create_command(self.type_command)

    def create_command(self, type):
        if type == 'ssh':
            self.command2 = ['sshpass', self.mode, self.pswfile,
                             'ssh', self.host]
            self.command2.extend(self.command)
        elif type == 'scp':
            self.command2 = ['sshpass', self.mode, self.pswfile,
                             'scp', '-P', '22']
            self.command2.extend(self.command)
        else:
            input('Please, enter the correct command.')

    def execute(self):
        if self.mode == '-f':
            p1 = subprocess.run(self.command2, capture_output=True, text=True)
        else:
            p1 = subprocess.run(self.command2, capture_output=True, text=True)

        if p1.returncode == 0:
            return p1.stdout
        else:
            return p1.stderr
