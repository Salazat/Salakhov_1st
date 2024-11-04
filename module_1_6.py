my_dict = {'Azat' : 1994, 'Ruslan' : 1993, 'Bulat' : 1995}
print(my_dict)
print(my_dict.get('Azat'))
print(my_dict.get('Oleg', 'Такой тип данных отсутвует'))
my_dict.update({'Fagilja' : 1955, 'Iskander' : 1992})
print(my_dict)
a = my_dict.pop('Ruslan')
print(my_dict)
print(a)
my_set = {1, 1, 2, 2, 3, 3, 4, 5, 5, 'project' , True, float,}
print(my_set)
my_set.add(0)
my_set.add(50)
print(my_set)
my_set.discard(float)
print(my_set)

