import tkinter as tk
import pytube
from pytube import YouTube
from pytube import exceptions
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

# WORKING:     https://www.youtube.com/watch?v=tXOIvjbNhts
# NOT WORKING: https://www.youtube.com/watch?v=CTc-iYL_rrU

HEIGHT = 400
WIDTH = 750

def get_video_information(video_URL):
    label['text'] = format(video_URL)
    try:
        yt = pytube.YouTube(video_URL)
        first_stream = yt.streams.filter(file_extension='mp4').first()
        print(first_stream)
        first_stream.download()
        label['text'] = "Download Complete!"
    except pytube.exceptions.VideoUnavailable:
        label['text'] = "Video Unavailable. Please check network connection and try again."
        print("Video Unavailable. Please check network connection and try again.")
    except KeyError:
        label['text'] = "There was an error downloading the video"
        print("There was an error downloading the video")
    

def format(video_URL):
    final_string = "You entered %s" % video_URL
    return final_string


# Set Canvas
root = tk.Tk()
root.title('YouTube Downloader')
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


# Set Upper Frame
upper_frame = tk.Frame(root, bg = '#ff9999', bd = 5)
upper_frame.place(relx = .5, rely = .1, relwidth = .75, relheight = .1, anchor = 'n')

# Set Text Box
entry = tk.Entry(upper_frame, font = 40)
entry.place(relwidth = .65, relheight = 1)

# Set Button
button = tk.Button(upper_frame, text = "Download Video", command = lambda: get_video_information(entry.get()))
button.place(relx = 0.7, relheight = 1, relwidth = .3)

# Set Response Frame
middle_frame = tk.Frame(root, bg = '#ff9999', bd = 10)
middle_frame.place(relx = .5, rely = .25, relwidth = .75, relheight = .6, anchor = 'n')

# Set Response Label
label = tk.Label(middle_frame, text = "", bg = 'white', font = 20)
label.place(relwidth = 1, relheight = 1)


# Exit Button
exit_button = tk.Button(root, text = "Exit", font = 20, command = root.destroy).place(relx = .5, rely = .9)

root.mainloop()

