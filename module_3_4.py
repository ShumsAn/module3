def single_root_words(root_word,*other_words):
    same_words = []

    for i in other_words:
        if i.upper() in root_word.upper():
            same_words.append(i)
        elif root_word.upper() in i.upper():
            same_words.append(i)

        # if i.upper().count(root_word.upper()) >= 1:
        #      same_words.append(i)
        # elif root_word.upper().count(i.upper()) >= 1:   -     тоже рабочий метод
        #      same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)


