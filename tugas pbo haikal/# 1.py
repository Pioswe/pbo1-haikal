# 1. Perulangan hingga 100 dengan output khusus
for i in range(1, 101):
    if i % 5 == 0:
        print("Haikal Putra Syamsu")
    elif i % 3 == 0:
        continue
    else:
        print(i)

# 2a. Program bebas dengan if else pada For Loops
for i in range(1, 11):
    if i % 2 == 0:
        print(f"For Loop: {i} is an even number.")
    else:
        print(f"For Loop: {i} is an odd number.")

# 2b. Program bebas dengan if else pada While Loops
counter = 1
while counter <= 10:
    if counter % 2 == 0:
        print(f"While Loop: {counter} is an even number.")
    else:
        print(f"While Loop: {counter} is an odd number.")
    counter += 1

# 3. Variabel array dan menampilkan nilai dengan perulangan for
my_array = [1, 3, 5, 7, 9]

for value in my_array:
    print(f"Array Value: {value}")
