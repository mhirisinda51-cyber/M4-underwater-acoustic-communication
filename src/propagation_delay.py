def propagation_delay(distance_km, sound_speed_m_s=1500):
    """Calculate one-way underwater acoustic propagation delay in seconds."""
    if distance_km < 0:
        raise ValueError("Distance cannot be negative.")
    if sound_speed_m_s <= 0:
        raise ValueError("Sound speed must be greater than zero.")

    distance_m = distance_km * 1000
    return distance_m / sound_speed_m_s


if __name__ == "__main__":
    distances = [0.1, 1, 5, 10]

    print("One-way underwater acoustic propagation delay")
    print("Distance (km) | Delay (s)")

    for distance in distances:
        delay = propagation_delay(distance)
        print(f"{distance:12.1f} | {delay:.2f}")