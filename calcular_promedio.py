"""
Módulo: calcular_descuento
Descripción:
    Este programa permite calcular el precio final de un producto después
    de aplicarle un descuento. El usuario ingresa el precio y el porcentaje,
    y el sistema realiza el cálculo de forma clara y amigable.
"""


def calcular_precio_con_descuento(precio_original, porcentaje_descuento):
    """
    Calcula el precio final aplicando un descuento.

    Parámetros:
        precio_original (float): Precio inicial del producto.
        porcentaje_descuento (float): Descuento en porcentaje (0 a 100).

    Retorna:
        float: Precio final después de aplicar el descuento.
    """

    # Validamos que el porcentaje esté en el rango permitido.
    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("El porcentaje de descuento debe ser entre 0 y 100.")

    # Calculamos cuánto representa el descuento en dinero.
    valor_descuento = precio_original * (porcentaje_descuento / 100)

    # Calculamos el precio final restando el descuento al precio original.
    precio_final = precio_original - valor_descuento

    return precio_final


# EJECUCIÓN PRINCIPAL DEL PROGRAMA 
Los nombres de variables y funciones son claros y descriptivos --- Cumple
Hay una docstring o comentario inicial que explica el propósito --- Cumple                       
Los comentarios son útiles (no redundantes ni excesivos) --- cumple
La sangría y el espaciado son consistentes --- Cumple  
El código está bien estructurado (bloques lógicos, sin líneas inútiles) --- Cumple                
Se aplica la guía de estilo acordada --- Cumple  

Bien Henor esta elegante. 
ATT Jean Julio

if __name__ == "__main__":
    print("  ")
    print("  Bienvenido al Calculador de Descuentos  ")
    print("  ")

    try:
        # Pedimos el precio al usuario de forma clara y amigable.
        precio_ingresado = float(
            input("\n Ingresa el precio original del producto: ")
        )

        # Pedimos el porcentaje de descuento.
        descuento_ingresado = float(
            input(" Ingresa el porcentaje de descuento (%): ")
        )

        # Llamamos la función que hace el cálculo.
        precio_con_descuento = calcular_precio_con_descuento(
            precio_ingresado, descuento_ingresado
        )

        # Mostramos los resultados de forma clara.
        print("\n-----------------------------------------------")
        print("  RESULTADOS ")
        print("-----------------------------------------------")
        print(f" Precio original:          ${precio_ingresado:,.2f}")
        print(f"  Descuento aplicado:      {descuento_ingresado}%")
        print(f" Precio final a pagar:     ${precio_con_descuento:,.2f}")
        print("-----------------------------------------------")
        print(" ¡Gracias por usar el calculador!\n")

    except ValueError as error:
        # Se muestra un mensaje claro en caso de error.
        print(f"\n Ocurrió un error: {error}")
        print("Por favor ingresa valores numéricos válidos.\n")

