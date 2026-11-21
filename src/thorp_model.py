def thorp_absorption(frequency_khz):
    """
    Calculate underwater acoustic absorption using Thorp's formula.

    frequency_khz: frequency in kHz
    Returns: absorption coefficient in dB/km
    """
    f = frequency_khz

    alpha = (
        0.11 * f**2 / (1 + f**2)
        + 44 * f**2 / (4100 + f**2)
        + 2.75e-4 * f**2
        + 0.003
    )

    return alpha


if __name__ == "__main__":
    frequencies = [5, 10, 20, 30, 50]

    print("Thorp absorption model")
    print("Frequency (kHz) | Absorption (dB/km)")

    for frequency in frequencies:
        absorption = thorp_absorption(frequency)
        print(f"{frequency:>15} | {absorption:.3f}")