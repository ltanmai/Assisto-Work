import librosa
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

audio_path = 'audio file wav.wav'
audio, sr = librosa.load(audio_path, sr=None)
mfccs = librosa.feature.mfcc(audio, sr=sr)

scaler = StandardScaler()
mfccs_scaled = scaler.fit_transform(mfccs.T)
kmeans = KMeans(n_clusters=2)  # Adjust based on the expected number of speakers
speaker_labels = kmeans.fit_predict(mfccs_scaled)

for i, label in enumerate(speaker_labels):
    print(f"Time Segment {i}: Speaker {label}")
