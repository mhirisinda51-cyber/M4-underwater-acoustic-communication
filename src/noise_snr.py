from propagation_loss import transmission_loss

# Illustrative assumptions for the first test.
# These are model inputs, not measured values.
SOURCE_LEVEL_DB = 190.0
NOISE_LEVEL_DB = 60.0

DISTANCES_KM = [0.1, 1, 5, 10]
FREQUENCIES_KHZ = [5, 10, 20, 30]


def calculate_snr(distance_km, frequency_khz):
    """Estimate SNR in dB using the current transmission-loss model."""
    loss_db = transmission_loss(distance_km, frequency_khz)
    return SOURCE_LEVEL_DB - loss_db - NOISE_LEVEL_DB


if __name__ == "__main__":
    print("Estimated SNR (dB)")
    print("Distance (km) | " + " | ".join(
        f"{frequency} kHz" for frequency in FREQUENCIES_KHZ
    ))

    for distance in DISTANCES_KM:
        values = [
            calculate_snr(distance, frequency)
            for frequency in FREQUENCIES_KHZ
        ]
        print(f"{distance:>13.1f} | " + " | ".join(
            f"{value:>8.2f}" for value in values
        ))