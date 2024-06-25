# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def main():
    book_path = "github.com/Phynix1973/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    count_chars(text)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_chars(text):
    
    str_lowered = text.lower()
    
    count_dict = {}

    for char in str_lowered:

        if char in count_dict:
            count_val = count_dict[char] + 1
            count_dict.update({char:count_val})
        else:
            count_dict.update({char:1})

    # convert dictionary to list of dictorionaries

    lst_dict = []
    for char, count in count_dict.items():
        #print(f"Character: {char}, Count: {count}")
        single_dict = {"char": char, "num": count}
        #print (single_dict)
        lst_dict.append(single_dict)
        

    lst_dict.sort(reverse=True,key=sort_on)
    for item in lst_dict:
        char=item["char"]
        num=item["num"]
        if char.isalpha():
            print(f"The '{char}' character was found {num} times")


# main
main()