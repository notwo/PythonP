import os

class CustomerCSV():
    def __init__(self, master=None, **key):
        self.filename = key.get('key').get('filename')
        self.header = key.get('key').get('header')
        crnt_dir = os.path.abspath('./data/')
        self.csv = os.path.join(crnt_dir, self.filename)

    def first_open(self):
        crnt_dir = os.path.abspath('./')
        path = os.path.join(crnt_dir, 'data')
        if not os.path.isdir(path):
            os.mkdir(path)

    def read_csv(self):
        data = []
        searched_data = []
        if not os.path.exists(self.csv):
            self.write_header()

        f = open(self.csv, 'r')
        # read header info
        f.readline()
        lines = f.readlines()
        for str in lines:
            # delete unknown last empty items...
            if str == '\n':
                continue
            data.append(str.split(','))
            searched_data.append(str.split(','))
        f.close()
        return [data, searched_data]

    def write_header(self):
        f = open(self.csv, 'w')
        f.write(self.header)
        f.close()

    def write_all_data(self, data):
        f = open(self.csv, 'a')
        f.write('\n')
        g = (d for d in data)
        for line in g:
            str = ','.join(line)
            f.write(str)
        f.close()

    def write_record(self, record):
        f = open(self.csv, 'a')
        f.write(record)
        f.close()
