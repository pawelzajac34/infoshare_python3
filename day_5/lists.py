names = ['pawel', 'michal', 'magda', 'ania', 'paulina',]
print('dlugosc listy names to:',len(names))

first_element = names[0]
last_element = names[-1]

#print('pierwszy i ostatni elemen',first_element,last_element)

# dodawanie elementu na koniec listy

names.append('sebastian')
print('aktualny stan listy po append:',names)
print('ostatni element to:',names[-1])

name_to_find = 'przemek'
names_count = names.count(name_to_find)
print('liczba osob o imieniu ',name_to_find,names_count)
name_to_find = 'ania'
names.append(name_to_find)
print('liczba osob o imieniu',name_to_find, names.count(name_to_find))

idx = names.index(name_to_find)
print('index of', name_to_find, idx)

# sprawdz czy name_to_find znajduje sie w liscie names
# jesli tak to wyswietl komunikat
# 'in'
if name_to_find in names:
    print('names_to_find zawiera sie w names')
else:
    print('nie zawiera sie')

second_row = names[1:3]
print(second_row)

# wyswietl kazdy element listy korzystajac z petli

for name in names:
    print(name)

