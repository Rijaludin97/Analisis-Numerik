# Metode Bisection

import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter as pc

def f(x):
    return x**3 + x**2 - 3*x - 3

def bisection(a, b, tol=1e-6, max_iter=100):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("f(a) dan f(b) harus berlawanan tanda. Pilih interval lain.")
    history = []
    start = pc()
    for i in range(1, max_iter+1):
        c = (a + b) / 2.0
        fc = f(c)
        history.append((i, a, b, c, fc))
        print(f"Iter {i:2d}: a={a:.8f}, b={b:.8f}, c={c:.8f}, f(c)={fc:.8e}")
        if abs(fc) < tol or (b - a)/2.0 < tol:
            end = pc()
            print(f"\nAkar diperkirakan di x = {c:.12f}")
            print(f"f(c) = {fc:.12e}")
            print(f"Iterasi = {i}, waktu = {(end-start):.6f} s")
            return c, history
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    end = pc()
    print("\nMetode tidak konvergen dalam batas iterasi.")
    return c, history

akar, hist = bisection(1, 2, tol=1e-6, max_iter=100)

x_vals = np.linspace(0, 3, 400)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linewidth=0.8)
plt.scatter([h[3] for h in hist], [h[4] for h in hist], color='red', label='Titik tengah (iterasi)')
plt.title('Metode Bisection')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

print(f"\nHasil akhir: akar mendekati x = {akar:.6f}")

# Metode Newton-Raphson

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 + x**2 - 3*x - 3

def f_prime(x):
    return 3*x**2 + 2*x - 3

def newton_raphson(x0, tol=1e-6, max_iter=100):
    print("Iterasi\t   x\t\t   f(x)")
    nilai_x = []
    for i in range(max_iter):
        fx = f(x0)
        fpx = f_prime(x0)

        if fpx == 0:
            print("Turunan nol, metode berhenti.")
            break

        x1 = x0 - fx / fpx
        print(f"{i+1}\t{x0:.6f}\t{fx:.6f}")
        nilai_x.append(x1)

        if abs(x1 - x0) < tol:
            print("\nAkar ditemukan pada x =", x1)
            return x1, nilai_x

        x0 = x1

    print("\nMetode tidak konvergen.")
    return None, nilai_x

akar, nilai_x = newton_raphson(3)

x_vals = np.linspace(0, 3, 400)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linewidth=0.8)
plt.scatter(nilai_x, [f(x) for x in nilai_x], color='red', label='Nilai iterasi')
plt.title('Metode Newton-Raphson')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

# Metode Secant

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 + x**2 - 3*x - 3

def secant(x0, x1, tol=1e-6, max_iter=100):
    print("Iterasi\t   x0\t\t   x1\t\t   x2\t\tf(x2)")
    nilai_x = []
    for i in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)
        if f1 - f0 == 0:
            print("Error: karena pembagian dengan nol")
            break

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        f2 = f(x2)
        print(f"{i+1}\t{x0:.6f}\t{x1:.6f}\t{x2:.6f}\t{f2:.6f}")
        nilai_x.append(x2)

        if abs(f2) < tol:
            print("\nAkar ditemukan pada x =", x2)
            return x2, nilai_x

        x0, x1 = x1, x2
    print("\nMetode tidak konvergen.")
    return None, nilai_x

akar, nilai_x = secant(2, 3)

x_vals = np.linspace(0, 4, 400)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linewidth=0.8)
plt.scatter(nilai_x, [f(x) for x in nilai_x], color='red', label='Nilai iterasi')
plt.title('Metode Secant')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
