import math
from noise_snr import calculate_snr

# Temporary assumption for the first test: 1 kHz bandwidth.
# This is not a specification for a real acoustic modem.
BANDWIDTH_HZ = 1000

DISTANCES_KM = [0.1, 1, 5, 10]
FREQUENCIES_KHZ = [5, 10, 20, 30]


def shannon_capacity(snr_db, bandwidth_hz):
    """Calculate theoretical Shannon capacity in bits per second."""
    snr_linear = 10 ** (snr_db / 10)
    return bandwidth_hz * math.log2(1 + snr_linear)
if __name__ == "__main__":
    print(f"Theoretical capacity (bps), bandwidth = {BANDWIDTH_HZ} Hz")
    print("Distance (km) | " + " | ".join(
        f"{frequency} kHz" for frequency in FREQUENCIES_KHZ
    ))

    for distance in DISTANCES_KM:
        capacities = [
            shannon_capacity(
                calculate_snr(distance, frequency),
                BANDWIDTH_HZ
            )
            for frequency in FREQUENCIES_KHZ
        ]

        print(f"{distance:>13.1f} | " + " | ".join(
            f"{capacity:>8.1f}" for capacity in capacities
        ))