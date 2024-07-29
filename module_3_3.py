
#1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
#1.1 Вызов функции с разным количеством аргументов
print_params()
print_params(2,8,9)
print_params(a = 'Строка :"а",')
print_params(b = 25)
print_params(c = [1,2,3])

#2.Распаковка параметров:
values_list = [1,[2,3],'Four']
values_dict = {'a':1,'b':2,'c':3}

print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)


#4. Вне задания
def append_to_list(item, list_my=None):
  if list_my is None:
    list_my = []
    list_my.append(item)
    print('Список не получил параметров значения взяты из item:',list_my)
  else:
      print(item,list_my)


append_to_list(('item = 3',3),('list = 2',2))
append_to_list([1,2,3])
