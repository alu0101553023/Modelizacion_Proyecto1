import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fila 1 (índice 0), desde columna E (índice 4)
x = np.arange(2000, 2025)

# Fila 2 (índice 1), desde columna E (índice 4)
y = np.array([579, 610, 595, 614, 607, 612, 608, 569, 601, 595, 633, 574, 600, 606, 532, 556, 569, 570, 564, 557, 558, 588, 541, 510, 507])

# Gráfica
plt.figure(figsize=(8, 8))
plt.plot(x, y, marker='o')
plt.xticks(np.arange(1999, 2025, 2))
plt.xlabel("Años", fontsize=12)
plt.ylabel("Consumo final de energía en los hogares per cápita (KGOE)", fontsize=12)
plt.grid(True)
plt.savefig('Dataset 3.png', dpi=300, bbox_inches='tight')
plt.show()