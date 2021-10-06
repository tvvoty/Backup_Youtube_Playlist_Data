# from pytube import YouTube
from pytube import Playlist
import re
import requests
new_line_character = "\n"  # f-string don't support back slashes so, yeah...
video_entry_html = ((f'<div class="thumbnail"><img src="{vid_obj.thumbnail_path}"></div><div class="title">'
                     f'<div class="title">{vid_obj.title}<br><br></div>'
                     f'<div class="url">{vid_obj.url}<br><br></div>'
                     f'<div class="author"><b>{vid_obj.author}</b><br><br></div>'
                     f'<div class="description">{re.sub(new_line_character, r"<br>", vid_obj.description)}<br><br></div>'))


class VideoObject:
    """Object for storing all videos in the playlist in a list"""

    def __init__(self, thumbnail_path, title, url, author, description):
        self.thumbnail_path = thumbnail_path
        self.title = title
        self.url = url
        self.author = author
        self.description = description


# the_playlist = Playlist('https://www.youtube.com/playlist?list=PL-nKcT3XDGcIuGnq4l92ZRLY2s7rUJENV')
the_playlist = Playlist('https://www.youtube.com/playlist?list=PL-nKcT3XDGcJT1v19mezBVRvyvDAx8oas')
video_obj_list = []
list_count = 0
for video in the_playlist.videos:
    video_obj_list.append(VideoObject(
        f"thumbnails/{video.title}.jpg", video.title, the_playlist.video_urls[list_count], video.author, video.description))
    img_data = requests.get(video.thumbnail_url).content
    with open(f'thumbnails/{video.title}.jpg', 'wb') as handler:
        handler.write(img_data)
    list_count += 1
    if list_count == 3:
        break


html_visual_list = "html_visual_list.html"
try:
    with open("html_template.html", mode='r', encoding='utf-8') as template:
        for line in template:
            html_from_template = template.readlines()
            #print(f'html lines are: {html_lines}')
    with open(html_visual_list, mode='w', encoding='utf-8') as f:
        for line in html_from_template[0:70]:
            # print(line)
            f.write(line)
        for vid_obj in video_obj_list:
            f.write(video_entry_html)
        for line in html_from_template[70:74]:
            f.write(line)
except Exception as e:
    print(f"Something wrong with your file or name: \n{e}\n Lets try again")

with open("videoslist.txt", mode='w', encoding='utf-8') as f:
    obj_count = 0
    f.write('ext_vid_obj_list = [')
    for obj in video_obj_list:
        f.write(
            f'obj{obj_count}({obj.thumbnail_path}, {obj.title}, {obj.url}, {obj.author}, {obj.description}),\n\n')
        obj_count += 1

# yt = YouTube('https://www.youtube.com/watch?v=qv3DQNchmHg&list=PL-nKcT3XDGcJT1v19mezBVRvyvDAx8oas')
