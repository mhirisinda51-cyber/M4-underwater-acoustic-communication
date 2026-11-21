import numpy as np
import matplotlib.pyplot as plt

from thorp_model import thorp_absorption

frequencies = np.linspace(1, 50, 500)
absorption = [thorp_absorption(f) for f in frequencies]

plt.figure(figsize=(8, 5))
plt.plot(frequencies, absorption)
plt.xlabel("Frequency (kHz)")
plt.ylabel("Absorption coefficient (dB/km)")
plt.title("Thorp's Formula: Underwater Acoustic Absorption")
plt.grid(True)
plt.tight_layout()

plt.savefig("thorp_absorption.png", dpi=300)
plt.show()