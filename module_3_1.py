calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()

    len_string = len(string)
    stringUP = string.upper()
    string_low = string.lower()
    string_tuple = (len_string, stringUP, string_low)
    return string_tuple

def is_contains(string,list_to_search):
    count_calls()
    list_to_search = str(list_to_search)
    list_to_search = list_to_search.upper()

    if string.upper() in list_to_search:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)




