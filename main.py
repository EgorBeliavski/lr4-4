len = int(input("Введите количество строк в списке: ")) # ввод кол-ва строк в списке

arr =[0]*len # создание списка определенной длины

for i in range(0,len): # заполнение списка строками
    arr[i] = input("Введите строку: ")

arr_2 = [i + " " + i + " " + i for i in arr] # создание нового списка

print(arr_2)