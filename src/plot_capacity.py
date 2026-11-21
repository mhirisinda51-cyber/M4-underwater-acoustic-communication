import numpy as np
import matplotlib.pyplot as plt

from noise_snr import calculate_snr
from capacity_model import shannon_capacity, BANDWIDTH_HZ

distances = np.linspace(0.1, 10, 100)
frequencies = [5, 10, 20, 30]

for frequency in frequencies:
    capacities = [
        shannon_capacity(
            calculate_snr(distance, frequency),
            BANDWIDTH_HZ
        )
        for distance in distances
    ]
    plt.plot(distances, capacities, label=f"{frequency} kHz")

plt.xlabel("Distance (km)")
plt.ylabel("Theoretical capacity (bps)")
plt.title("Estimated underwater acoustic communication capacity")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("capacity_vs_distance.png", dpi=300)
plt.show()