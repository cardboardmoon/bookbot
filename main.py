def main():
    words = get_contents("books/frankenstein.txt").split()
    print(f"There are {len(words)} words in Frankenstein.")
    #print(character_count())
    sort_list(convert_to_list(character_count()))

def get_contents(text):
    with open(text) as f:
        file_contents = f.read()
    return file_contents

def character_count():
    lowered = get_contents("books/frankenstein.txt").lower()
    chars = list(lowered)
    char_count = {}
    for char in chars:
        if char.isalpha():
            if char in char_count:
                char_count["count"] += 1 
            else:
                char_count["character"] = char
                char_count["count"] = 1 
    return char_count

def sort_on(_dict):
    return _dict["count"]

def convert_to_list(_dict):
    _list = []
    for i in _dict:
        _list.append({"character": i, "count": _dict[i]})
    return _list

def sort_list(list):
    sorted_list = list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
