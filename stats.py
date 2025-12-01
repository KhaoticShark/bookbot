def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}

    for ch in text :
        ch = ch.lower()
        if ch in char_counts :
            char_counts[ch] += 1
        else:
            char_counts[ch] = 1

    return char_counts  

def sort_on(items):
    return items["num"]

def sort_characters(char_dict):
    char_list = []
    for ch, count in char_dict.items():
        char_list.append({"char": ch, "num": count})
    char_list.sort(reverse=True, key=sort_on)  
    return char_list
