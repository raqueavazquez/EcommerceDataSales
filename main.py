import filtro
import graficas
import ecuaciones

def mostrar_bienvenida():
    # Mostrar mensaje de bienvenida
    ...

def mostrar_opciones():
    # Mostrar las opciones disponibles al usuario
    ...

def solicitar_opcion():
    # Solicitar al usuario que ingrese una opción
    opcion = ...

    return opcion

def ciclo_programa():
    # Mantener el ciclo del programa hasta que el usuario decida salir
    while True:
        mostrar_bienvenida()
        mostrar_opciones()
        opcion = solicitar_opcion()

        if opcion == 1:
            # Filtrado de la base de datos
            datos = filtro.importar_datos('base_datos.csv')
            filtro_mostrado = filtro.aplicar_filtro(datos, filtro_seleccionado)
            filtro.guardar_datos(filtro_mostrado, 'datos_filtrados.csv')

        elif opcion == 2:
            # Mostrar gráfica de los datos filtrados
            datos_filtrados = filtro.importar_datos('datos_filtrados.csv')
            graficas.mostrar_grafica(datos_filtrados, tipo_grafica_seleccionado)
            graficas.guardar_grafica(datos_filtrados, tipo_grafica_seleccionado, 'grafica.png')

        elif opcion == 3:
            # Calcular variables representativas
            datos = filtro.importar_datos('base_datos.csv')
