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

def pattern_search(david:str, sad:str):
    """
    :param david:
    :param sad:
    :return:
    """
    pattern_length = len(sad)
    sequence_length = len(david)
    found_positions = set()

    for i in range(sequence_length - pattern_length + 1):
        if david[i:i + pattern_length] == sad:
            found_positions.add(i)

    return found_positions

def binary_search(heh, number):
    """
    :param heh:
    :param number:
    :return:
    """
    kde_je = heh.index(number)
    if number not in heh:
        return None
    return kde_je

def main():
    file_name = "sequential.json"
    sad = "ATA"
    #read data
    seq = read_data(file_name, field="unordered_numbers")
    david = read_data(file_name, field="dna_sequence")
    heh = read_data(file_name, field="ordered_numbers")
    print(seq)
    print(david)
    print(heh)
    hledane_cislo = 0
    number = 25
    result = linear_search(seq, hledane_cislo)
    matches = pattern_search(david, sad)
    number_pos = binary_search(heh, number)
    return print(f"Hledané číslo jsme našli na indexu {result}. Patern jsme nalezli na indexu {matches}. Číslo se v posloupnosti nachází na místě {number_pos}.")

if __name__ == '__main__':
    main()