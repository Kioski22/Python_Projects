import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, ttk
import whisper
import threading
import os

# Load Whisper model once
model = whisper.load_model("medium")

# Global variable to store selected file path
selected_file = None

def transcribe_audio(file_path, output_box, progress_bar, start_button):
    try:
        progress_bar.start()
        start_button.config(state="disabled")

        output_box.insert(tk.END, f"\nTranscribing: {file_path}\n\n")
        result = model.transcribe(file_path, language="tl")
        output_box.insert(tk.END, "Transcription completed!\n")

        output_box.insert(tk.END, result["text"] + "\n\n---\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        progress_bar.stop()
        start_button.config(state="normal")

def open_file(label, start_button):
    global selected_file
    file_path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.mp3 *.m4a *.wav *.flac")]
    )
    if file_path:
        selected_file = file_path
        label.config(text=f"Selected File: {os.path.basename(file_path)}")
        start_button.config(state="normal")

def start_transcription(output_box, progress_bar, start_button):
    if selected_file:
        threading.Thread(target=transcribe_audio, args=(selected_file, output_box, progress_bar, start_button)).start()
    else:
        messagebox.showwarning("No File", "Please select an audio file first.")

def main_gui():
    root = tk.Tk()
    root.title("PSME TRANSCRIPT GEN. APP")
    root.geometry("750x550")

    # File Label
    file_label = tk.Label(root, text="No file selected", font=("Arial", 10))
    file_label.pack(pady=(10, 0))

    # Select File Button
    select_btn = tk.Button(root, text="Select Audio File", command=lambda: open_file(file_label, start_btn))
    select_btn.pack(pady=10)

    # Start Transcription Button
    start_btn = tk.Button(root, text="Start Transcription", state="disabled", command=lambda: start_transcription(output_box, progress, start_btn))
    start_btn.pack(pady=5)

    # Progress Bar
    progress = ttk.Progressbar(root, mode='indeterminate')
    progress.pack(fill="x", padx=20, pady=10)

    # Output Box
    output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 11))
    output_box.pack(expand=True, fill="both", padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_gui()
