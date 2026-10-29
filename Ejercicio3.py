def f(x):
    return 4*x**4 - 9*x**2 + 14*x + 1

# Condiciones iniciales 
a = -3.0
b = -1.0
tolerancia = 5.0
max_iter = 100


iteracion = 0
error_actual = 100.0
xr_anterior = 0.0

if f(a) * f(b) >= 0:
    print("El intervalo inicial no contiene un cambio de signo.")
else:
    print(f"{'Iter':<5} | {'a':<8} | {'b':<8} | {'xr':<9} | {'f(xr)':<9} | {'Error Ea (%)'}")
    print("-" * 65)
    
    while error_actual > tolerancia and iteracion < max_iter:
        iteracion += 1
        
        # Fórmula del método de Falsa Posición
        xr = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        # El error se calcula a partir de la segunda iteración
        if iteracion > 1:
            error_actual = abs((xr - xr_anterior) / xr) * 100
            error_str = f"{error_actual:.2f}%"
        else:
            error_str = "-"
            
        print(f"{iteracion:<5} | {a:<8.4f} | {b:<8.4f} | {xr:<9.4f} | {f(xr):<9.4f} | {error_str}")
        
        # Reemplazo de límites
        if f(a) * f(xr) < 0:
            b = xr
        else:
            a = xr
            
        xr_anterior = xr

    print("-" * 65)
    print(f"Raíz encontrada: {xr:.4f} con un error de {error_actual:.2f}% tras {iteracion} iteraciones.")