def sumar_rango_recursivo(lista, pi, pf):
    if pi > pf:
        return 0
    return lista[pi - 1] + sumar_rango_recursivo(lista, pi + 1, pf)

def main():
    print("--- Suma en Rango de una Lista (Recursivo) ---")
    
    entrada = input("Ingrese los números de la lista separados por comas (ej. 2, 4, 6, 3): ")
    try:
        lista = [float(x.strip()) for x in entrada.split(",") if x.strip() != ""]
        if all(x.is_integer() for x in lista):
            lista = [int(x) for x in lista]
    except ValueError:
        print("Entrada inválida. Debe ingresar números separados por comas.")
        return

    print(f"Lista cargada: {lista}")

    try:
        pi = int(input("Ingrese la posición inicial (PI, desde 1): "))
        pf = int(input("Ingrese la posición final (PF, desde 1): "))
    except ValueError:
        print("Las posiciones deben ser números enteros.")
        return
    if pi < 1 or pf > len(lista):
        print(f"Error: Las posiciones deben estar en el rango de 1 a {len(lista)}.")
        return
    if pi > pf:
        print("Error: PI no puede ser mayor que PF.")
        return

    #llamamos a la función recursiva
    resultado = sumar_rango_recursivo(lista, pi, pf)
    print(f"\nResultado de la suma entre la posición {pi} y {pf}: {resultado}")

if __name__ == "__main__":
    # prueba de el ejemplo del enunciado
    lista_ejemplo = [2, 4, 6, 3]
    pi_ejemplo = 2
    pf_ejemplo = 3
    res = sumar_rango_recursivo(lista_ejemplo, pi_ejemplo, pf_ejemplo)
    print(f"[Prueba de ejemplo] Lista: {lista_ejemplo}, PI: {pi_ejemplo}, PF: {pf_ejemplo}")
    print(f"Resultado obtenido: {res} (Esperado: 10)")
    print("-" * 50)
    
    main()
