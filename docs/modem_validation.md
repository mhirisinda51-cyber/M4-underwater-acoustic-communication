\# Validation with Commercial Underwater Acoustic Modems



\## Purpose



The model estimates underwater acoustic transmission loss, SNR, theoretical

capacity, and propagation delay. These estimates should be compared with

published specifications of real acoustic modems.



\## Published specifications



| Modem | Frequency band | Published data rate | Published range |

|---|---:|---:|---:|

| Teledyne Benthos ATM series | LF: 9–14 kHz; MF: 16–21 kHz; Band C: 22–27 kHz | PSK: 2,560–15,360 bps; MFSK: 140–2,400 bps | Typical: LF ≥ 6 km; MF ≥ 4 km; Band C ≥ 2 km |

| UNAVLAB uWave | Not stated in the cited specification | Up to 634 bps | Up to 1,000 m |



Sources:

\- Teledyne Benthos, Acoustic Modem Selection Guide:

&#x20; https://www.teledynemarine.com/brands/benthos/acoustic-modems

\- UNAVLAB, uWave Modem Specification:

&#x20; https://docs.unavlab.com/documentation/EN/uWAVE/uWAVE\_Specification\_en.html



\## Important comparison notes



\- Manufacturer specifications describe performance under particular operating

&#x20; conditions. They are not guaranteed results for every underwater environment.

\- The model's Shannon capacity is a theoretical upper bound, not a practical

&#x20; modem data rate.

\- A direct numerical comparison requires matching the model's frequency,

&#x20; bandwidth, distance, source level, and noise assumptions to the modem's

&#x20; operating conditions.

\- The current model is simplified. Differences from published specifications

&#x20; should be discussed as limitations, not treated as proof that the modem or

&#x20; model is incorrect.

\## Preliminary comparison with the current model



The current model estimates theoretical capacity using a fixed bandwidth of 1 kHz and illustrative source and noise levels. The commercial modem specifications listed above report data rates and ranges under their own operating conditions.



The model frequencies of 10 kHz and 20 kHz fall within the published LF and MF bands of the Teledyne Benthos ATM series, respectively. However, the available specifications do not provide enough matching information about bandwidth, source level, noise, and operating conditions to make a direct numerical comparison.



Therefore, this comparison is qualitative at this stage. A quantitative validation requires matching the model inputs to the operating conditions of a specific modem.

