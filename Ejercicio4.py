def f(x):
    return -1 / (x - 1.5) - 2

def df(x):
    # Derivada de f(x) para el método de Newton-Raphson
    return 1 / ((x - 1.5)**2)

def newton_raphson(x0, max_iter):
    print(f"\n--- Método Abierto: Newton-Raphson (Valor inicial x0 = {x0}) ---")
    x = x0
    print(f"{'Iter':<5} | {'x':<12} | {'f(x)':<12}")
    print("-" * 35)
    for i in range(1, max_iter + 1):
        print(f"{i:<5} | {x:<12.5f} | {f(x):<12.5f}")
        # Evitar error si justo cae en la asíntota
        if abs(x - 1.5) < 1e-10:
            print("Error: El cálculo cayó en la asíntota vertical.")
            break
        x = x - f(x) / df(x)

def biseccion(a, b, max_iter):
    print(f"\n--- Método Cerrado: Bisección (Intervalo [{a}, {b}]) ---")
    if f(a) * f(b) >= 0:
        print("No hay cambio de signo en el intervalo.")
        return
    
    print(f"{'Iter':<5} | {'a':<8} | {'b':<8} | {'xm':<10} | {'f(xm)':<10}")
    print("-" * 50)
    for i in range(1, max_iter + 1):
        xm = (a + b) / 2
        print(f"{i:<5} | {a:<8.4f} | {b:<8.4f} | {xm:<10.5f} | {f(xm):<10.5f}")
        if f(a) * f(xm) < 0:
            b = xm
        else:
            a = xm


newton_raphson(1.3, 5)  # Converge rápidamente a la raíz (x=1)
newton_raphson(2.4, 5)  # Diverge alejándose de la raíz

# Usamos [0.5, 1.4] como intervalo cerrado válido en el primer cuadrante
biseccion(0.5, 1.4, 10)