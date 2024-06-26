import random
import numpy as np
import matplotlib.pyplot as plt
import time

 Исходные данные:
 print(random.sample(range(1, 18), 4))
 14, 2, 17, 1

 14 РАБОТАЕТ (Возвращает сортированный массив!)
def sort_radix(array, k):
	if (len(array)!=0):
		array_left = []
		array_right = []
		for element in array:
			if(len(bin(element).replace("0b", '')) < k):
				array_left.append(element)
			elif(bin(element)[-k] == '0'):
				array_left.append(element)
			else:
				array_right.append(element)
		if(k > 1):
			array_left = sort_radix(array_left, k-1)
			array_right = sort_radix(array_right, k-1)
		array = array_left + array_right
	return array



 2 РАБОТАЕТ
def sort_shaker(array):
	start = 0
	end = len(array)-1
	i = 0
	swapped = True
	while (swapped):
		swapped = False
		for i in range(start, end):
			if (array[i] > array[i+1]):
				array[i], array[i+1] = array[i+1], array[i]
				swapped = True

		if (swapped == False):
			break

		swapped = False

		end -= 1

		for i in range(end-1, start-1, -1):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
				swapped = True
		start += 1


 17 СТРАННО РАБОТАЕТ

def abs(vector, index):
	return(vector[0][index]**2 + vector[1][index]**2)**0.5

def c_swap(array, l, r, d):
	if (d == 1 and abs(array,l) > abs(array,r)) or (d == 0 and abs(array,l) < abs(array,r)):
		array[0][l], array[0][r] = array[0][r], array[0][l]
		array[1][l], array[1][r] = array[1][r], array[1][l]

def merge(a, b, cnt, d):
	if cnt > 1:
		k = int(cnt / 2)
		for i in range(b, b + k):
			c_swap(a, i, i + k, d)
		merge(a, b, k, d)
		merge(a, b + k, k, d)
 
 a - array, b = 0, cnt - len(a), u - 1

def sort_bitonic(a, b, cnt, d=1):
	if cnt > 1:
		k = int(cnt / 2)
		sort_bitonic(a, b, k, 1)
		sort_bitonic(a, b + k, k, 0)
		merge(a, b, cnt, d)



 1 РАБОТАЕТ
def sort_bubble(array):
	for i in range(len(array)):
		for j in range(len(array)-i-1):
			if (array[j][0] > array[j+1][0]):
				array[j], array[j+1] = array[j+1], array[j]
	return array





 Массив целых чисел
array_size = 999999
array_int = []
for i in range(array_size):
	array_int.append(random.randint(0, array_size))

 print(array_int)
array_int = sort_radix(array_int, 18)

print("Массив длинной " + str(len(array_int)) + " символов отсортирован (radix сортировка)")
 print(array_int)



 Массив float (99999 тоже соритруется, но очень долго. Ньюансы метода)
array_size = 9999
array_float = np.random.uniform(low = -1, high =  1, size = array_size)

 print(array_float)
sort_shaker(array_float)
 print("После:")
 print(array_float)
print("Массив длинной " + str(len(array_float)) + " символов отсортирован (shaker сортировка)")



 Масств точек компл. плоскости r = 17/5
r = 17/5
array_size = 42000
array_2d = [[],[]]
for i in range(array_size):
	x = np.random.uniform(-r, r)
	y = np.random.uniform(-(r**2-x**2)**0.5, (r**2-x**2)**0.5)
	array_2d[0].append(x)
	array_2d[1].append(y)

sort_bitonic(array_2d, len(array_2d), 1)
 for i in range(len(array_2d[0])):
 	print(abs(array_2d, i))
print("Массив длинной " + str(len(array_2d[0])) + " символов отсортирован (bitonic сортировка)")



 Массив слов
file = open("book.txt", 'r', encoding="utf-8")
array_text = []
sumbols_to_remove = "\","
for line in file:
	for word in line.split(' '):
		if (word != '' and word != '\n' and word != '-'):
			for symbol in sumbols_to_remove:
				word.replace(symbol, '')
			array_text.append(word.replace('\n', ''))
 print(array_text)
timer_start = time.time()
sort_bubble(array_text)
timer_stop = time.time()
print("файл длинной " + str(len(array_text)) + " слов отсортирован  методом bubble за " + str((timer_stop - timer_start) * 1000 ) + " мс")
