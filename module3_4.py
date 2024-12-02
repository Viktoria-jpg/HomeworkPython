def single_root_words(root_word, *other_words):
    same_words = []
    root_word.lower()
    other_words = list(other_words)
    for number in range(len(other_words)):
        ind = 0
        for letter in (other_words[number]).lower():
            for check in (root_word):
                if letter == check:
                    ind = ind + 1
                    if ind == len(root_word) or ind == len(other_words[number]):
                        same_words.append(other_words[number])
                        break

    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', ' richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
