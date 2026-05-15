# test_emotion_detection.py
from emotion_detection import emotion_detector

# Contoh beberapa teks untuk dites
teks_list = [
    "I am very happy with the results!",
    "I am scared of the upcoming exam.",
    "I feel sad about the news.",
    "I am angry that this happened."
]

for teks in teks_list:
    hasil = emotion_detector(teks)
    print(f"Teks: {teks}")
    print(f"Hasil Deteksi: {hasil}")
    print("-" * 40)
