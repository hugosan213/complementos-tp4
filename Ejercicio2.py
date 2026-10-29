def f(x):
    return x**3 - 7*x**2 + 14*x - 6

# Condiciones iniciales
a = 2.7
b = 3.2
tolerancia = 2.0
max_iter = 100


iteracion = 0
error_actual = 100.0
xm_anterior = 0.0

if f(a) * f(b) >= 0:
    print("El intervalo inicial no contiene un cambio de signo.")
else:
    print(f"{'Iter':<5} | {'a':<8} | {'b':<8} | {'xm':<8} | {'f(xm)':<9} | {'Error Ea (%)'}")
    print("-" * 65)
    
    while error_actual > tolerancia and iteracion < max_iter:
        iteracion += 1
        xm = (a + b) / 2
        
        # El error se calcula a partir de la segunda iteración
        if iteracion > 1:
            error_actual = abs((xm - xm_anterior) / xm) * 100
            error_str = f"{error_actual:.2f}%"
        else:
            error_str = "-"
            
        print(f"{iteracion:<5} | {a:<8.4f} | {b:<8.4f} | {xm:<8.4f} | {f(xm):<9.4f} | {error_str}")
        
        # Reemplazo de límites 
        if f(a) * f(xm) < 0:
            b = xm
        else:
            a = xm
            
        xm_anterior = xm

    print("-" * 65)
    print(f"Raíz encontrada: {xm:.5f} con un error de {error_actual:.2f}% tras {iteracion} iteraciones.")