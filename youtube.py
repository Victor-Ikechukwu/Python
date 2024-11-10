import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo("Success", "Download complete!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

# Set up the GUI
app = tk.Tk()
app.title("YouTube Video Downloader")
app.geometry("400x200")

# URL input field
tk.Label(app, text="Enter YouTube URL:").pack(pady=10)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

# Download button
download_button = tk.Button(app, text="Download", command=download_video)
download_button.pack(pady=20)

app.mainloop()
