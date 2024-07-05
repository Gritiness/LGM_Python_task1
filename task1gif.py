from moviepy.editor import *

video_clip = VideoFileClip("video task1.mp4")
video_clip = video_clip.subclip(0,10)
video_clip.write_gif("Task_01.gif",fps = 20)
gif_video_clip = VideoFileClip("Task_01.gif")
gif_video_clip.ipython_display()
