import math
from noise_snr import calculate_snr

# Simplified reference values for an initial comparison.
# Required Eb/N0 values are approximate and assume an AWGN channel
# and a target BER around 1e-5. They are not underwater modem specifications.
MODULATIONS = {
    "BPSK": {"bits_per_symbol": 1, "required_ebn0_db": 9.6},
    "QPSK": {"bits_per_symbol": 2, "required_ebn0_db": 9.6},
    "16-QAM": {"bits_per_symbol": 4, "required_ebn0_db": 13.4},
}

BANDWIDTH_HZ = 1000
DISTANCES_KM = [0.1, 1, 5, 10]
FREQUENCIES_KHZ = [5, 10, 20, 30]


def required_snr_db(modulation):
    """Estimate required SNR, assuming symbol rate equals bandwidth."""
    ebn0_db = MODULATIONS[modulation]["required_ebn0_db"]
    bits_per_symbol = MODULATIONS[modulation]["bits_per_symbol"]
    return ebn0_db + 10 * math.log10(bits_per_symbol)


def compare_modulations(snr_db, bandwidth_hz):
    """Return estimated rates for modulations meeting their SNR threshold."""
    results = {}

    for modulation, parameters in MODULATIONS.items():
        threshold_db = required_snr_db(modulation)

        if snr_db >= threshold_db:
            results[modulation] = (
                parameters["bits_per_symbol"] * bandwidth_hz
            )
        else:
            results[modulation] = 0

    return results


if __name__ == "__main__":
    print("Illustrative modulation comparison")
    print(f"Assumed bandwidth: {BANDWIDTH_HZ} Hz")
    print("Rate is 0 when the estimated SNR is below the threshold.")
    print()

    for frequency in FREQUENCIES_KHZ:
        print(f"\nFrequency: {frequency} kHz")
        print("Distance (km) | SNR (dB) | BPSK | QPSK | 16-QAM (bps)")
        print("-" * 62)

        for distance in DISTANCES_KM:
            snr_db = calculate_snr(distance, frequency)
            rates = compare_modulations(snr_db, BANDWIDTH_HZ)

            print(
                f"{distance:13.1f} | {snr_db:8.2f} | "
                f"{rates['BPSK']:4} | {rates['QPSK']:4} | "
                f"{rates['16-QAM']:12}"
            )