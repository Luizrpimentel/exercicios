import matplotlib.pyplot as plt
import numpy as np


vendas = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)

plt.figure(figsize=(15, 3))
plt.subplot(131)
plt.bar(meses,vendas)
plt.subplot(132)
plt.scatter(meses,vendas)
plt.subplot(133)
plt.plot(meses,vendas)
plt.show()