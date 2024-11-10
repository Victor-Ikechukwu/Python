
# Victor'sPortal YouTube Video Downloader

A simple and efficient YouTube video downloader with a graphical user interface (GUI) built using Python's `tkinter` library. This application allows users to download YouTube videos or audio in MP4 or MP3 format, using `yt-dlp` and `ffmpeg` for handling the downloads and conversions.

## Features

- **User-Friendly Interface**: A clean and attractive GUI for easy interaction.
- **Format Options**: Allows users to download videos in MP4 format or extract audio in MP3 format.
- **High-Quality Downloads**: Selects the best available quality for both video and audio.
- **Error Handling**: Informs users about any issues during the download process.

## Requirements

- Python 3.7+
- `yt-dlp` library
- `ffmpeg` (for converting videos to MP3)

## Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/YourUsername/Python.git
cd Python
```

### 2. Install Dependencies

Install the necessary Python libraries:

```bash
pip install yt-dlp
pip install tkinter
```

### 3. Install `ffmpeg`

- **Windows**: Download the Windows build from [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/), extract it, and add the `bin` directory to your system’s PATH.
- **Linux**: Install via package manager:
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```
- **macOS**: Use Homebrew:
  ```bash
  brew install ffmpeg
  ```

Verify the installation by running `ffmpeg -version` in your terminal. Make sure `ffmpeg` is accessible in your PATH.

## Usage

1. Run the script:

   ```bash
   python youtube.py
   ```

2. Enter the YouTube video URL in the input field.

3. Select the desired format from the dropdown menu:
   - **MP4 (Video)**: Downloads the video with the best available quality.
   - **MP3 (Audio)**: Extracts the audio and saves it as an MP3 file.

4. Click the **Download** button to start the download.

5. A success message will appear once the download is complete, or an error message if something went wrong.

## Code Explanation

The main parts of the script include:

- **GUI Setup**: Uses `tkinter` for creating a simple and intuitive interface.
- **Download Function**: Handles the download and conversion using `yt-dlp` and `ffmpeg`. The user’s selected format (MP4 or MP3) determines whether to download video or extract audio.
- **Error Handling**: Displays error messages for invalid URLs, network issues, or missing dependencies like `ffmpeg`.

### Sample Code Snippet

```python
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location': 'C:/ffmpeg/bin/ffmpeg.exe',  # Update with the correct path
}
```

The `ffmpeg_location` field specifies the path to the `ffmpeg` executable. Make sure this path is correct.

## Troubleshooting

### Common Issues

1. **`ffmpeg` Not Found**: 
   - Ensure `ffmpeg` is installed and the path is correctly set in the `ffmpeg_location` variable or added to your system’s PATH.

2. **Network Errors**:
   - Check your internet connection. If you are behind a firewall, ensure it allows access to GitHub and YouTube.

3. **Unable to Download Certain Videos**:
   - Some YouTube videos may be restricted or have DRM protections that prevent downloads.

4. **SSL/TLS Errors**:
   - Update Python and `yt-dlp` to the latest versions, as SSL/TLS protocols are updated frequently.

## Contributing

We welcome contributions! If you'd like to enhance this YouTube downloader, follow these steps:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix.
   ```bash
   git checkout -b feature-name
   ```
3. **Make your changes** and commit them.
4. **Push to your fork** and submit a Pull Request.

Please make sure to include a description of your changes in the Pull Request.

## License

This project is open-source and available under the MIT License.

## Acknowledgements

- **yt-dlp**: A powerful tool for downloading videos from various sources, including YouTube.
- **ffmpeg**: Used for video and audio processing.
```

