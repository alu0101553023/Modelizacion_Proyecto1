import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo Excel
archivo = "dataset1.xlsx"
df = pd.read_excel(archivo, header=None)

# Fila 1 (índice 0), desde columna E (índice 4)
x = df.iloc[0, 4:].to_numpy()

# Fila 2 (índice 1), desde columna E (índice 4)
y = df.iloc[1, 4:].to_numpy()

# Gráfica
plt.figure(figsize=(8, 8))
plt.plot(x, y, marker='o')
plt.xticks(np.arange(1998, 2026, 2))
plt.xlabel("Años", fontsize=12)
plt.ylabel("Emisiones de dióxido de carbono (CO2) (total) excluyendo LULUCF (Mt CO2e)", fontsize=12)
plt.legend()
plt.grid(True)
plt.savefig('Dataset 1.png', dpi=300, bbox_inches='tight')
plt.show()