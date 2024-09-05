YouTube Downloader with Progress Bar 🎬⬇️
Welcome to this simple yet powerful YouTube Downloader! This tool allows you to easily download videos from YouTube directly to your computer, while showing you a live progress bar and status updates. It's built using Python, with a clean and modern user interface thanks to tkinter and customtkinter, and it uses the super-reliable yt_dlp for downloading the videos.

✨ Features
Easy-to-use interface: Just paste a YouTube link and click download. It’s that simple!
Real-time progress tracking: Watch the download progress with a live percentage, speed, and estimated time remaining.
Error handling: Get immediate feedback if something goes wrong, so you're always in the know.
Lightweight and fast: No bloat, just what you need to download your favorite videos quickly and efficiently.

🛠️ Installation & Setup
Prerequisites
Make sure you have Python installed on your system. You’ll also need a couple of additional packages for the app to work. Here's how to set it up:

Install Python packages: Open your terminal or command prompt and run:

pip install customtkinter yt-dlp

Running the Application
Download or clone this repository.
Navigate to the folder where the files are located.
Run the application by typing:

python main.py
That’s it! The YouTube downloader app will open, and you can start downloading videos right away.

🎮 How to Use
Step 1: Copy the YouTube link of the video you want to download.
Step 2: Paste the link into the input box in the app.
Step 3: Click the Download button.
Watch the progress: As the download happens, the progress bar will update, showing you how far along the download is, your download speed, and an estimate of how long it will take to finish.
Completion: Once the video is downloaded, the app will tell you with a nice “Downloaded!” message. If anything goes wrong, it will let you know as well.


📂 Project Structure
main.py: This is the main script where all the magic happens. It contains the code for the user interface and the download logic.
README.md: You’re reading this file right now! It explains what the project does and how to use it.

Example Screenshot 📸
![image](https://github.com/user-attachments/assets/6b08283e-4aaa-448b-8396-fc9ba6f586d4)


💡 Things to Know
The progress bar might jump quickly from 0% to completion for small videos or if the download happens super fast.
Some videos might not show an accurate file size, but the app will still download them without a problem!


🚀 Why Did I Build This?
I built this app as part of my journey to learn Python. It was a fun and practical project that helped me understand how to interact with APIs, create user interfaces, and handle real-time feedback. This project is great for anyone who, like me, is looking to explore Python in a hands-on way while creating something useful.


⚠️ License
Feel free to use, modify, or share this project!
