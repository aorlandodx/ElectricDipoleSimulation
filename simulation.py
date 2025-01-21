import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Parámetros de entrada
k = 8.9875e9  # Constante de Coulomb en (N*m^2) / C^2
q1 = -1  # Carga 1 en Coulombs
q2 = 1  # Carga 2 en Coulombs
x1, y1 = 0.25, 0  # Posición de la carga 1
x2, y2 = -0.25, 0  # Posición de la carga 2

# Función para calcular el campo eléctrico en un punto (x, y)
def campo_electrico(x, y):
    """
    Parámetros:
    - x (float): Posición en el eje x en (m)
    - y (float): Posición en el eje y en (m)
    
    Variables de salida:
    - Ex (float): Componente x del campo eléctrico en (N/C)
    - Ey (float): Componente y del campo eléctrico en (N/C)
    """
    r1 = np.sqrt((x - x1)**2 + (y - y1)**2)  # Distancia de la carga 1 al punto
    r2 = np.sqrt((x - x2)**2 + (y - y2)**2)  # Distancia de la carga 2 al punto
    
    # Componentes del campo eléctrico debido a cada carga
    Ex1 = k * q1 * (x - x1) / r1**3
    Ey1 = k * q1 * (y - y1) / r1**3
    Ex2 = k * q2 * (x - x2) / r2**3
    Ey2 = k * q2 * (y - y2) / r2**3
    
    # Sumamos las contribuciones de ambas cargas
    Ex = Ex1 + Ex2
    Ey = Ey1 + Ey2
    
    return Ex, Ey

# Creamos una malla de puntos para evaluar el campo eléctrico
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Cálculo del campo eléctrico en cada punto de la malla
Ex, Ey = campo_electrico(X, Y)

# Graficar el campo eléctrico
plt.figure(figsize=(8, 6))
plt.streamplot(X, Y, Ex, Ey, color='black', linewidth=1, arrowsize=1.5)
plt.gca().add_patch(Rectangle((x1 - 0.1, y1 - 0.1), 0.2, 0.2, color='blue', alpha=0.5, label='Carga negativa'))
plt.gca().add_patch(Rectangle((x2 - 0.1, y2 - 0.1), 0.2, 0.2, color='red', alpha=0.5, label='Carga positiva'))

plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Gráfica del campo vectorial')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.show()
