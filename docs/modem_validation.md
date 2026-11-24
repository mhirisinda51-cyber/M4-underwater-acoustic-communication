\# Validation with Commercial Underwater Acoustic Modems



\## Purpose



The model estimates underwater acoustic transmission loss, signal-to-noise ratio (SNR), theoretical channel capacity, and propagation delay. These estimates are compared with published specifications of commercial underwater acoustic modems to assess whether the model produces plausible results.



\## Published specifications



| Modem | Frequency band | Published data rate | Published range |

|---|---|---:|---:|

| Teledyne Benthos ATM series | LF: 9–14 kHz; MF: 16–21 kHz; Band C: 22–27 kHz | PSK: 2,560–15,360 bps; MFSK: 140–2,400 bps | Typical: LF ≥ 6 km; MF ≥ 4 km; Band C ≥ 2 km |

| UNAVLAB uWave | Not stated in the cited specification | Up to 634 bps | Up to 1,000 m |



Sources:

\- Teledyne Benthos, \*Acoustic Modem Selection Guide\*:  

&#x20; https://www.teledynemarine.com/brands/benthos/acoustic-modems

\- UNAVLAB, \*uWave Modem Specification\*:  

&#x20; https://docs.unavlab.com/documentation/EN/uWAVE/uWAVE\_Specification\_en.html



\## Comparison method and limitations



The model uses a fixed bandwidth of 1 kHz and illustrative source and noise levels. The commercial modem specifications report data rates and ranges under their own operating conditions.



The model frequencies of 10 kHz and 20 kHz fall within the published LF and MF bands of the Teledyne Benthos ATM series, respectively. The model will be evaluated at 1 km, 2 km, 5 km, and 10 km, using 20 kHz as a representative frequency within the MF band.



The model's Shannon capacity is a theoretical upper bound, not a guaranteed practical data rate. Manufacturer specifications describe performance under particular operating conditions and do not guarantee the same results in every underwater environment.



A direct numerical comparison would require matching the model's frequency, bandwidth, source level, noise assumptions, and operating conditions to those of a specific modem. Since the cited specifications do not provide all these matching parameters, the comparison is qualitative at this stage.



\## Preliminary conclusion



The published modem specifications provide useful reference points for evaluating the model's estimated communication range and data rate. However, differences between the model and commercial specifications cannot be interpreted as evidence that either is incorrect, because the model uses simplified assumptions and the operating conditions may differ.



The current comparison therefore serves as a preliminary plausibility check. A quantitative validation would require more detailed manufacturer data and model inputs matched to a specific modem and operating scenario.

