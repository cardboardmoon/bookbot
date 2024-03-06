def main():
    words = get_contents("books/frankenstein.txt").split()
    print(f"There are {len(words)} words in Frankenstein.\n")
    final_list = sort_list(character_count())
    for _dict in final_list:
        print("The '{}' character was found {} times".format(_dict["character"], _dict["count"]))

def get_contents(text):
    with open(text) as f:
        file_contents = f.read()
    return file_contents

def character_count():
    lowered = get_contents("books/frankenstein.txt").lower()
    chars = list(lowered)
    char_dict_list = []
    for char in chars:
        if char.isalpha():
            for dict in char_dict_list:
                if dict["character"] == char:
                    dict["count"] += 1
                    break
            else:
                char_dict_list.append({"character": char, "count": 1})
    return char_dict_list

def sort_on(_dict):
    return _dict["count"]

def sort_list(_list):
    _list.sort(reverse=True, key=sort_on)
    return _list

main()
