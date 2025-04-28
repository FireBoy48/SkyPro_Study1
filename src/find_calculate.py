import re


def find_str(some_str: str, some_list: list)-> list:
    result = []
    for dictionary in some_list:
        for string in dictionary:
            print(string)
            if re.findall(some_str, dictionary[string], flags=0):
                result.append(dictionary)
    return result


def find_cat(some_str: str, some_list: list)-> list:
    result = []
    for dictionary in some_list:
        for string in dictionary:
            print(string)
            if re.findall(some_str, string, flags=0):
                result.append(dictionary)
    return result