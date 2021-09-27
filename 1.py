name = input ("Введите имя_")
Sname = input ("Введите фамилию_")
date = int(input ("дата рождения_"))
print (name, Sname, date, sep = "_")
name, Sname = Sname, name
print(name, Sname, date+60, sep = "_")
