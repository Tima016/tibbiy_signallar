import mne
import numpy as np
import matplotlib.pyplot as plt

# EDF fayl manzili
edf_file_path = r'C:\\Users\\user\\suniy_intellekt\\path_to_extract_folder\\foredf\\Subject00_1.edf'

# Faylni o'qish
raw = mne.io.read_raw_edf(edf_file_path, preload=True)

# EEG signallarini olish (masalan, 'EEG Fp1' kanalini olish)
eeg_signal = raw.get_data(picks=['EEG Fp1'])[0]  # 'EEG Fp1' kanalining signali

# Namuna tezligi
sampling_rate = raw.info['sfreq']

# Vaqt domenida signalni ko'rsatish
plt.figure(figsize=(10, 6))
plt.plot(np.arange(len(eeg_signal)) / sampling_rate, eeg_signal)
plt.xlabel("Vaqt (soniya)")
plt.ylabel("Signal Amplitudasi")
plt.title(f"Jonli EEG Signal - {edf_file_path}")
plt.show()

# FFT yordamida spektral tahlil
frequencies, power = plt.psd(eeg_signal, NFFT=1024, Fs=sampling_rate)

# Chastota va kuch ko'rsatish
plt.figure(figsize=(10, 6))  # Yangi oyna yaratish
plt.plot(frequencies, power)
plt.xlabel('Chastota (Hz)')
plt.ylabel('Kuch (dB)')
plt.title('EEG Signalining Chastota Tahlili')
plt.show()
