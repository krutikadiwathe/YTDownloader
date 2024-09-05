import tkinter
import customtkinter
import yt_dlp


def progress_hook(d):
    if d['status'] == 'downloading':
        # Try to use 'total_bytes', fallback to 'total_bytes_estimate'
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate', 1)
        downloaded_bytes = d.get('downloaded_bytes', 0)

        # Calculate percentage of completion
        percent_complete = downloaded_bytes / total_bytes * 100
        speed = d.get('_speed_str', '0 B/s')
        eta = d.get('_eta_str', 'N/A')

        # Update progress label and progress bar
        progressLabel.configure(text=f"Progress: {percent_complete:.2f}%, Speed: {speed}, ETA: {eta}")
        progressBar.set(percent_complete / 100)  # Progress bar expects a value between 0 and 1

        # Force the UI to refresh
        app.update_idletasks()

    elif d['status'] == 'finished':
        progressLabel.configure(text="Processed")
        app.update_idletasks()

    elif d['status'] == 'error':
        progressLabel.configure(text="Download failed")
        app.update_idletasks()

def startDownload():

    ytLink = link.get().strip()
    print(f"Link retrieved: {ytLink}")

    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
    }

    try:

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
           ydl.download([ytLink])


        print("Download Complete")
        finishLabel.configure(text="Downloaded!", text_color="green")

    except Exception as e:
        print(f"Error: {e}")
        finishLabel.configure(text="Download failed", text_color="red")





#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Progress Label
progressLabel = customtkinter.CTkLabel(app, text="Progress: 0%")
progressLabel.pack(pady=10)

# Progress Bar
progressBar = tkinter.DoubleVar()
progressbar_widget = customtkinter.CTkProgressBar(app, variable=progressBar, width=400)
progressbar_widget.pack(pady=10)
progressbar_widget.set(0)  # Initialize to 0%


#Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text=" ")
finishLabel.pack()

"""#progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)"""

#Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#Run app
app.mainloop()