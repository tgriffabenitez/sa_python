# A partir de una lista de números calcular la suma de sus elementos. (sin utilizar sum())

num_list = [1, 1, 1, 1, 1]
total = 0

for i in range(len(num_list)):
    total += num_list[i]

print(total)