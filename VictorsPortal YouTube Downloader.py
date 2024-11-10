# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:51:45 2024

@author: Victor-PhD
"""

import tkinter as tk  # Import tkinter for GUI components
from tkinter import messagebox, ttk  # Import messagebox for popup alerts and ttk for styled widgets
from yt_dlp import YoutubeDL  # Import yt_dlp for downloading YouTube videos

def download_video():
    """
    Downloads the video or audio from YouTube based on the selected format.
    Displays a success message if the download is successful, otherwise an error message.
    """
    url = url_entry.get()  # Get the URL entered by the user
    format_option = format_var.get()  # Get the selected format from the dropdown menu

    # Validate that a URL was entered
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return

    # Configure download options based on selected format
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Sets filename format
        'ffmpeg_location': 'C:/ffmpeg/bin/ffmpeg.exe',  # Specify the path to ffmpeg executable
    }
    if format_option == 'MP4 (Video)':
        # Download best video and audio combined if video format is selected
        ydl_opts['format'] = 'bestvideo+bestaudio/best'  
    elif format_option == 'MP3 (Audio)':
        # Download only audio with mp3 conversion if audio format is selected
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Set codec to mp3
            'preferredquality': '192',  # Set quality to 192 kbps
        }]

    try:
        # Start downloading using yt-dlp with the specified options
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"Download complete in {format_option.split()[0]} format!")
    except Exception as e:
        # Show error message if download fails
        messagebox.showerror("Error", f"Failed to download video: {e}")

# Set up the main application window
app = tk.Tk()
app.title("Dr. Victor's YouTube Video Downloader")  # Set the title of the window
app.geometry("500x350")  # Set window size
app.configure(bg="#1e1e2f")  # Set a dark purple background color for a modern look

# Apply styles to improve the appearance of labels, buttons, and entry fields
style = ttk.Style()
style.theme_use('clam')  # Use the 'clam' theme for modern, flat appearance

# Configure label styles
style.configure("TLabel", background="#1e1e2f", foreground="#f2f2f2", font=("Arial", 12))

# Configure entry field styles
style.configure("TEntry", font=("Arial", 12), padding=5)

# Configure button styles with cool color effects
style.configure("TButton", font=("Arial", 10, "bold"), background="#5a5a8b", foreground="#f2f2f2", padding=10)
style.map("TButton", background=[("active", "#404063")], foreground=[("active", "#ffffff")])

# Title label to display the app name
title_label = ttk.Label(app, text="Dr. Victor's YouTube Video Downloader", font=("Arial", 16, "bold"))
title_label.pack(pady=20)  # Add padding around the title for spacing

# Label for URL input field
url_label = ttk.Label(app, text="Enter Valid YouTube URL:")
url_label.pack(pady=5)  # Small padding for consistent layout

# Entry field for URL input
url_entry = ttk.Entry(app, width=50, font=("Arial", 12))  # Increased font size for readability
url_entry.pack(pady=5)

# Label for format selection dropdown
format_label = ttk.Label(app, text="Select Format:")
format_label.pack(pady=10)

# Dropdown menu for format selection (MP4 or MP3)
format_var = tk.StringVar(value="MP4 (Video)")  # Default format is set to MP4
format_dropdown = ttk.Combobox(app, textvariable=format_var, state="readonly", font=("Arial", 10), width=20)
format_dropdown['values'] = ("MP4 (Video)", "MP3 (Audio)")  # Options for the dropdown
format_dropdown.pack(pady=5)

# Download button to trigger the download process
download_button = ttk.Button(app, text="Download Now...", command=download_video)
download_button.pack(pady=20)  # Padding for spacing between button and other widgets

# Run the application main loop
app.mainloop()
