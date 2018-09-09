import re

class Util():
    def __init__(self):
        pass

    def change_all_records_to_str_in_array(self, array):
        return list(map(str, array))

    def change_all_records_to_str_in_array_without_newline(self, array):
        return list(map(lambda d: re.sub('\n|\r\n|\r', '', str(d)), array))

    def delete_last_str(self, target, char):
        if target[-1:] == char:
            target = target[:-1]
        return target
