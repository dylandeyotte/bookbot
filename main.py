from stats import word_count, character_count, sort_dict
import sys
    
def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book = sys.argv[1]
    print(f' BOOKBOT '.center(33, '=') + f'\nAnalyzing book found at {book}...' )
    print(f' Word Count '.center(33, '-'))
    print(word_count(book))
    print(f' Character Count '.center(33, '-'))
    for item in sort_dict(book):
        char = item['char']
        if char.isalpha():
            print(f'{char}: {item['num']}')
    print(f' End '.center(33, '='))
    
    

main()

