import subprocess
import getpass
import argparse


class Remote():
    def __init__(self, host=None, pswfile=None, command=None):
        if host is None:
            self.host = input('Enter a host: ')
        else:
            with open(host, 'r') as f:
                self.host = f.read()[:-1]

        if pswfile is None:
            self.mode = '-p'

            self.password = getpass.getpass("Password: ")
        else:
            self.pswfile = pswfile
            self.mode = '-f'

        if command is None:
            self.type_command = input('Enter ssh for ssh command or scp for scp command: ')
            if self.type_command == 'scp':
                self.scp_command = input('Enter a source and destination: ').split()
            else:
                self.ssh_command = input('Enter a command: ').split()

        self.create_command(self.type_command)

    def create_command(self, type_of_command):
        if type_of_command == 'ssh':
            self.command_final = ['sshpass', self.mode, self.pswfile,
                                  'ssh', self.host]
            self.command_final.extend(self.ssh_command)
        elif type_of_command == 'scp':
            self.command_final = ['sshpass', self.mode, self.pswfile,
                                  'scp', '-P', '22']
            self.command_final.extend(self.scp_command)
        else:
            input('Please, enter the correct command.')

    def execute(self):
        p1 = subprocess.run(self.command_final, capture_output=True, text=True)
        return p1
