# meeting_transcript_gui.py

import whisper
from pydub import AudioSegment
from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np
import os

import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

import tkinter as tk
from tkinter import filedialog, scrolledtext


from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# Ensure required resources are downloaded
nltk.download('punkt')

# Step 1: Convert audio to WAV format if needed
def convert_to_wav(input_audio_path):
    audio = AudioSegment.from_file(input_audio_path)
    wav_path = input_audio_path.rsplit('.', 1)[0] + '.wav'
    audio.export(wav_path, format='wav')
    return wav_path

# Step 2: Transcribe using Whisper
def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result['text']

# Step 3: Fake diarization using speaker embeddings
def split_by_speaker(audio_path):
    wav_fpath = Path(audio_path)
    wav = preprocess_wav(wav_fpath)
    encoder = VoiceEncoder()
    embeds, _, _ = encoder.embed_utterance(wav, return_partials=True)

    speaker_segments = []
    for i in range(0, len(embeds), 10):
        speaker = f"Speaker {i % 2 + 1}"
        segment = f"{speaker}: Segment {i//10 + 1}"
        speaker_segments.append(segment)
    return speaker_segments

# Step 4: Extract summary using sentence clustering
def summarize_text(text, num_sentences=5):
    sentences = sent_tokenize(text)
    if len(sentences) <= num_sentences:
        return text

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(sentences)

    n_clusters = min(num_sentences, len(sentences))
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(X)

    top_sentences = []
    for center in kmeans.cluster_centers_:
        closest, _ = min(enumerate(X), key=lambda x: np.linalg.norm(x[1] - center))
        top_sentences.append(sentences[closest])

    return "\n".join(top_sentences)

# Combine all steps
def run_transcription_pipeline(file_path, text_area):
    try:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, "Processing...\n")

        file_path = convert_to_wav(file_path)
        transcript = transcribe_audio(file_path)
        text_area.insert(tk.END, "Transcription completed.\n")

        speakers = split_by_speaker(file_path)
        text_area.insert(tk.END, "Speaker segments identified.\n")

        summary = summarize_text(transcript)
        text_area.insert(tk.END, "Summary generated.\n\n")

        global latest_output
        latest_output = (
            
    "================ TRANSCRIPT ================\n"
    f"{transcript}\n\n"
    "================ SPEAKER SEGMENTS ================\n"
    + "\n".join(speakers) + "\n\n"
    "================ SUMMARY ================\n"
    + summary
)

        text_area.insert(tk.END, latest_output)


    except Exception as e:
        text_area.insert(tk.END, f"\n⚠️ Error: {e}")

# GUI functions
def open_file(text_area):
    file_path = filedialog.askopenfilename()
    if file_path:
        run_transcription_pipeline(file_path, text_area)

def launch_gui():
    root = tk.Tk()
    root.title("🎙️ Meeting Transcript Generator")

    btn = tk.Button(root, text="Choose Audio File", command=lambda: open_file(text_area))
    btn.pack(pady=10)

    text_area = scrolledtext.ScrolledText(root, width=120, height=40, font=("Courier", 10))
    text_area.pack()

    root.mainloop()




def save_as_txt():
    if not latest_output:
        messagebox.showinfo("Info", "No transcript to save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(latest_output)
        messagebox.showinfo("Saved", f"Transcript saved to:\n{file_path}")

def save_as_pdf():
    if not latest_output:
        messagebox.showinfo("Info", "No transcript to save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                             filetypes=[("PDF files", "*.pdf")])
    if file_path:
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter
        y = height - 40
        for line in latest_output.split('\n'):
            c.drawString(40, y, line[:100])  # Line wrap at 100 characters
            y -= 14
            if y < 40:
                c.showPage()
                y = height - 40
        c.save()
        messagebox.showinfo("Saved", f"Transcript PDF saved to:\n{file_path}")

# Start the GUI
if __name__ == "__main__":
    launch_gui()
