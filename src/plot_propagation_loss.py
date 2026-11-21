import numpy as np
import matplotlib.pyplot as plt
from propagation_loss import transmission_loss

distances = np.linspace(0.1, 10, 100)
frequencies = [5, 10, 20, 30]

for frequency in frequencies:
    losses = [transmission_loss(d, frequency) for d in distances]
    plt.plot(distances, losses, label=f"{frequency} kHz")

plt.xlabel("Distance (km)")
plt.ylabel("Transmission loss (dB)")
plt.title("Estimated underwater acoustic transmission loss")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("propagation_loss.png", dpi=300)
plt.show()