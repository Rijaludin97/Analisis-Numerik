# Algoritma1

x_awal1 = 100000.0
x_selanjutnya1 = 0.00001
for _ in range(100000):
  x_awal1 += x_selanjutnya1
print(f"Hasil Algoritma 1 : {x_awal1}")

# Algoritma 2

total2 = 0.0
x_awal2 = 0.00001
for _ in range(100000):
  total2 += x_awal2
total2 += 100000
print(f"Hasil Algoritma 2 : {total2}")
