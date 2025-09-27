def word_count(book):
    split_book = get_book_text(book).split()
    count = len(split_book)
    return f'Found {count} total words'

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def character_count(book):
    char_dict = {}
    for char in get_book_text(book).lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict
    
def get_dict(dictionary):
    return dictionary['num']

def sort_dict(book):
    count = character_count(book)
    list1 = [{'char': char, 'num': num} for char, num in count.items()]
    list1.sort(key=get_dict, reverse=True)
    return list1
    