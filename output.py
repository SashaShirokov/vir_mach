import client_server as cs
import json


class Output:
    def __init__(self, hostfile, passfile):
        self.final_res = {
            'error': '',
            'result': '',
            'status': ''
        }
        self.s = cs.MyServer(hostfile, passfile)
        self.write_res()
        self.get_res()
        self.print_res()

    def write_res(self):
        with open('result.txt', 'w') as f:
            p = self.s.server.execute()
            self.final_res['status'] = p.returncode
            if p.returncode == 1:
                self.final_res['error'] = p.stderr
            f.write(p.stdout)

    def get_res(self):
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

            self.final_res['result'] = res_json

    def print_res(self):
        print(self.final_res)
        with open('final_res.txt', 'w') as f:
            f.write(str(self.final_res))


o = Output('hosts.txt', 'passwords.txt')
