import os

CSV_HEADER = "お客様氏名,郵便番号,住所,電話番号,送り先情報"

class CustomerCSV():
    def __init__(self, master=None, **key):
        self.filename = key.get('key').get('filename')
        self.data = key.get('key').get('data')
        self.searched_data = key.get('key').get('searched_data')
        crnt_dir = os.path.abspath('./data/')
        self.csv = os.path.join(crnt_dir, self.filename)

    def first_open(self):
        crnt_dir = os.path.abspath('./')
        path = os.path.join(crnt_dir, 'data')
        if not os.path.isdir(path):
            os.mkdir(path)

    def read_csv(self):
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
            self.data.append(str.split(','))
            self.searched_data.append(str.split(','))
        f.close()

    def write_header(self):
        f = open(self.csv, 'w')
        f.write(CSV_HEADER)
        f.close()
