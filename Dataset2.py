import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fila 1 (índice 0), desde columna E (índice 4)
x = np.arange(2000, 2023)

# Fila 2 (índice 1), desde columna E (índice 4)
y = np.array([381, 388, 397, 405, 414, 428, 442, 459, 481, 512, 545, 589, 637, 665, 694, 733, 772, 805, 840, 888, 946, 1016, 1090])

# Gráfica
plt.figure(figsize=(8, 8))
plt.plot(x, y, marker='o')
plt.xticks(np.arange(1999, 2024, 2))
plt.xlabel("Años", fontsize=12)
plt.ylabel("Capacidad renovable per cápita (Vatios per cápita)", fontsize=12)
plt.grid(True)
plt.savefig('Dataset 2.png', dpi=300, bbox_inches='tight')
plt.show()