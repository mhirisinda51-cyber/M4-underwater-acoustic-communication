import math
from thorp_model import thorp_absorption

def transmission_loss(distance_km, frequency_khz, spreading_factor=20):
    """
    Estimate underwater acoustic transmission loss.

    distance_km: distance in kilometres
    frequency_khz: acoustic frequency in kHz
    spreading_factor: 20 for ideal spherical spreading

    Returns transmission loss in dB.
    """
    if distance_km <= 0:
        raise ValueError("Distance must be greater than zero.")

    absorption_db_per_km = thorp_absorption(frequency_khz)

    # Spreading loss uses distance in metres, with a 1-metre reference.
    distance_m = distance_km * 1000
    spreading_loss_db = spreading_factor * math.log10(distance_m)

    # Absorption is expressed in dB/km, so use distance in kilometres.
    absorption_loss_db = absorption_db_per_km * distance_km

    return spreading_loss_db + absorption_loss_db

if __name__ == "__main__":
    distances = [0.1, 1, 5, 10]
    frequencies = [5, 10, 20, 30]

    print("Estimated transmission loss (dB)")
    print("Distance (km) | " + " | ".join(f"{f} kHz" for f in frequencies))

    for distance in distances:
        losses = [
            transmission_loss(distance, frequency)
            for frequency in frequencies
        ]
        print(f"{distance:12.1f} | " + " | ".join(f"{loss:.2f}" for loss in losses))