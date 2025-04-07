import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as json_file:
        seq = json.load(json_file)
    return seq[field]

def linear_search(seq, hledane_cislo):
    """
    :param seq:
    :param hledane_cislo:
    :return:
    """
    ind = []
    count = 0
    idx = 0
    while idx < len(seq):
        if seq[idx] == hledane_cislo:
            ind.append(idx)
            count += 1
        idx += 1
    return {"position": ind, "count": count}

def pattern_search(david, vzor):
    """
    :param david:
    :param vzor:
    :return:
    """
    int = []
    i = 0
    while i < len(david):
        if david[i] == vzor:
            int.append(i)
        i += 1
    return {"pozice": int}

def main():
    file_name = "sequential.json"
    #read data
    seq = read_data(file_name, field="unordered_numbers")
    david = read_data(file_name, field="dna_sequence")
    print(seq)

if __name__ == '__main__':
    main()