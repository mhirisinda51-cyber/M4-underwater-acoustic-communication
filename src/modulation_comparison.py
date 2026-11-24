import matplotlib.pyplot as plt


# Idealized modulation comparison.
# Assumption: all schemes use the same symbol rate.
# Data rate = symbol rate * bits carried by each symbol.

MODULATIONS = {
    "BPSK": {
        "bits_per_symbol": 1,
        "robustness": "High",
    },
    "QPSK": {
        "bits_per_symbol": 2,
        "robustness": "High to medium",
    },
    "8-PSK": {
        "bits_per_symbol": 3,
        "robustness": "Medium",
    },
    "16-QAM": {
        "bits_per_symbol": 4,
        "robustness": "Lower",
    },
}

SYMBOL_RATE = 1000  # symbols per second (1 ksymbol/s)


def calculate_data_rate(bits_per_symbol, symbol_rate):
    """Return ideal uncoded data rate in bits per second."""
    return bits_per_symbol * symbol_rate


def main():
    print("Idealized modulation comparison")
    print(f"Assumed symbol rate: {SYMBOL_RATE} symbols/s")
    print("Modulation | Bits/symbol | Ideal data rate (bps) | Relative robustness")
    print("-" * 75)

    names = []
    data_rates = []

    for name, properties in MODULATIONS.items():
        bits = properties["bits_per_symbol"]
        rate = calculate_data_rate(bits, SYMBOL_RATE)

        print(
            f"{name:<10} | {bits:^11} | {rate:^21} | "
            f"{properties['robustness']}"
        )

        names.append(name)
        data_rates.append(rate)

    plt.figure(figsize=(8, 5))
    plt.bar(names, data_rates)
    plt.xlabel("Modulation scheme")
    plt.ylabel("Ideal data rate (bps)")
    plt.title("Ideal Data Rate at the Same Symbol Rate")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("docs/modulation_comparison.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()