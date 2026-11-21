import matplotlib.pyplot as plt

from noise_snr import calculate_snr

distances = [0.1 + i * 0.1 for i in range(100)]
frequencies = [5, 10, 20, 30]

for frequency in frequencies:
    snr_values = [
        calculate_snr(distance, frequency)
        for distance in distances
    ]
    plt.plot(distances, snr_values, label=f"{frequency} kHz")

plt.xlabel("Distance (km)")
plt.ylabel("Estimated SNR (dB)")
plt.title("Estimated underwater acoustic SNR")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("snr_vs_distance.png", dpi=300)
plt.show()