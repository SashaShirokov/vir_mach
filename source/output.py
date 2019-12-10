import json

import client_server as cs


class Output:
    def __init__(self, hostfile, passfile):
        self.final_res = {
            'error': '',
            'result': '',
            'status': ''
        }
        self.my_status = 0
        self.server = cs.MyServer(hostfile, passfile)
        self.write_res()
        if self.my_status is 1:
            self.get_res()
        else:
            self.get_final_res()
        self.print_res()

    def write_res(self):
        with open('result.txt', 'w') as f:
            process = self.server.remote_server.execute()
            self.final_res['status'] = process.returncode
            if (process.returncode is 0 and process.stdout is '') or (process.returncode is 0 and process.stdout[0] is '-'):
                self.my_status = 1
            if process.returncode != 0:
                self.final_res['error'] = process.stderr
            f.write(process.stdout)

    def get_res(self):
        with open('result.txt') as f:
            result_temp = []
            result_json_format = {}
            all_lines = f.read().split('\n')

            ''' Since the output of iperf3 in json is too complicated,
            I cut the necessary information out of the regular output. That's why I have to do all manipulation with the lines downwards.
            '''
            for ind, line in enumerate(all_lines):
                if ind is 4 or ind is len(all_lines) - 2:
                    result_temp.append(line)
            for ind, line in enumerate(result_temp):
                line_split = line.split()
                if ind is 0:
                    result_json_format['serverIP'] = line_split[3]
                    result_json_format['clientIP'] = line_split[8]
                else:
                    result_json_format['Interval'] = line_split[2]
                    result_json_format['Transfer'] = line_split[4]
                    result_json_format['Bandwidth'] = line_split[6]

            self.final_res['result'] = result_json_format

    def get_final_res(self):
        with open('result.txt') as f:
            self.final_res['result'] = f.read()

    def print_res(self):
        print(self.final_res)
        with open('final_res.txt', 'w') as f:
            f.write(str(self.final_res))
