# ========================================================
# PROBLEMA 1 - Nivel de Compromiso de Sesiones de Clientes
# Autor: Juan Jose Velez Soto
# Grupo: 178
# Curso: Fundamentos de Programación - UNAD
# ========================================================

def clasificar_compromiso(duracion, clics):
    """
    Módulo (función) que calcula la clasificación de compromiso
    según la lógica de negocio del problema.
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


# Datos Iniciales: Matriz con 8 filas (más de las 5 requeridas)
sesiones = [
    [101, 250, 12],   # Alto
    [102, 45, 1],     # Bajo
    [103, 120, 5],    # Medio
    [104, 300, 15],   # Alto
    [105, 75, 9],     # Medio
    [106, 30, 10],    # Bajo (duración baja)
    [107, 200, 2],    # Bajo (pocos clics)
    [108, 190, 7]     # Medio
]

# Generar el informe solicitado
print("=== INFORME DE NIVEL DE COMPROMISO DE SESIONES ===")
print("{:<12} {:<15} {:<8} {:<15}".format("ID Cliente", "Duración (s)", "Clics", "Clasificación"))
print("-" * 55)

for sesion in sesiones:
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]
    clasificacion = clasificar_compromiso(duracion, clics)
    print("{:<12} {:<15} {:<8} {:<15}".format(id_cliente, duracion, clics, clasificacion))

print("\n=== Fin del reporte ===")
print(f"Total de sesiones analizadas: {len(sesiones)}")
