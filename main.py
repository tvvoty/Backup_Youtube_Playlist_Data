# from pytube import YouTube
from pytube import Playlist
import requests
import os
import re
import json

class VideoObject:
    """Object for storing all videos in the playlist in a list"""

    new_line_character = "\n"  # f-strings don't support back slashes so... yeah...

    def __init__(self, thumbnail_path, title, url, author, description):
        self.thumbnail_path = thumbnail_path
        self.title = title
        self.url = url
        self.author = author
        self.description = description

    def entry_html(vid_obj):
        html = ((f'<div class="thumbnail"><img src="{vid_obj.thumbnail_path}"></div><div class="title">'
                 f'<div class="title">{vid_obj.title}<br><br></div>'
                 f'<div class="url">{vid_obj.url}<br><br></div>'
                 f'<div class="author"><b>{vid_obj.author}</b><br><br></div>'
                 f'<div class="description">{re.sub(VideoObject.new_line_character, r"<br>", vid_obj.description)}<br><br></div>'))
        return html


def init_promt():
    while True:
        mode = input(('Enter "add" into the console to add a new playlist\n'
                      'Enter "check" to check a playlist:\n'))
        if mode == "add" or mode == "check":
            return mode
        print("Invalid input, lets try again.\n")


def get_playlist_url_from_user():
    playlist_url = input('Enter the playlist url:\n')
    return playlist_url


def get_playlist_name_from_user():
    playlist_url = input(
        'Enter the name for the folder the data for the playlist will be stored in:\n')
    return playlist_url


def check_and_create_playlist_dir(playlist_dir_name):
    if not os.path.isdir(f'./{playlist_dir_name}'):
        try:
            os.makedirs(f"./{playlist_dir_name}/thumbnails")
        except Exception as e:
            print(f"Something went wrong: {e}")


def create_video_obj_list(playlist_dir_name, the_playlist_url, write_thumbs):
    print(f"Agrs: {playlist_dir_name}, {the_playlist_url}, {write_thumbs}")
    # the_playlist = Playlist('https://www.youtube.com/playlist?list=PL-nKcT3XDGcIuGnq4l92ZRLY2s7rUJENV')
    # the_playlist = Playlist('https://www.youtube.com/playlist?list=PL-nKcT3XDGcJT1v19mezBVRvyvDAx8oas')
    # the_playlist = Playlist('https://www.youtube.com/playlist?list=PL-nKcT3XDGcJT1v19mezBVRvyvDAx8oas')
    the_playlist = Playlist(the_playlist_url)
    video_obj_list = []
    list_count = 0
    for video in the_playlist.videos:
        video_obj_list.append(VideoObject(
            f"thumbnails/{video.title}.jpg", video.title, the_playlist.video_urls[list_count], video.author, video.description))
        if write_thumbs:
            img_data = requests.get(video.thumbnail_url).content
            with open(f'{playlist_dir_name}/thumbnails/{video.title}.jpg', 'wb') as handler:
                handler.write(img_data)
        list_count += 1
        if list_count == 2:
            break
    print(video_obj_list)
    return video_obj_list


def get_tamplate_html():
    with open("html_template.html", mode='r', encoding='utf-8') as template:
        for line in template:
            html_from_template = template.readlines()
            #print(f'html lines are: {html_lines}')
        return html_from_template


def write_to_visual_list_html_file(video_obj_list, playlist_dir_name):
    html_from_template = get_tamplate_html()
    html_visual_list = f"{playlist_dir_name}/html_visual_list.html"
    try:
        with open(html_visual_list, mode='w', encoding='utf-8') as f:
            for line in html_from_template[0:70]:
                # print(line)
                f.write(line)
            for vid_obj in video_obj_list:
                f.write(VideoObject.entry_html(vid_obj))
            for line in html_from_template[70:74]:
                f.write(line)
    except Exception as e:
        print(f"Something wrong with your file or name: \n{e}\n Lets try again")


def write_vid_obj_list(video_obj_list, playlist_dir_name):
    pattern = re.compile(r'"')
    with open(f"{playlist_dir_name}/videoslist.json", mode='w', encoding='utf-8') as f:
        obj_count = 0
        f.write('{\n  "Video_objects": [\n')
        def s (line):
            return pattern.sub("''", line)
        for obj in video_obj_list:
            f.write (f'    {{\n      "title": "{s(obj.title)}",\n      "thumbnail_path": "{s(obj.thumbnail_path)}",\n      "url": "{s(obj.url)}",\n      "author": "{s(obj.author)}",\n      "description": "{obj.description}"\n    }},\n')

            if obj_count == 3:
                break
            obj_count += 1
    with open(f"{playlist_dir_name}/videoslist.json", 'rb+') as f:
        f.seek(-2, os.SEEK_END)
        f.truncate()
    with open(f"{playlist_dir_name}/videoslist.json", mode='a', encoding='utf-8') as f:
        f.write("\n  ]\n}")



def write_the_playlist_url(playlist_dir_name, the_playlist_url):
    with open(f"{playlist_dir_name}/the_playlist_url.txt", mode='w', encoding='utf-8') as f:
        f.write(f'{the_playlist_url}')


def create_playlist_data_backup():
    playlist_dir_name = input(
        'Enter the name for the folder the data for the playlist will be stored in:\n')
    the_playlist_url = input('Enter the playlist url:\n')
    check_and_create_playlist_dir(playlist_dir_name)
    vid_obj_list = create_video_obj_list(playlist_dir_name, the_playlist_url, True)
    write_to_visual_list_html_file(vid_obj_list, playlist_dir_name)
    write_vid_obj_list(vid_obj_list, playlist_dir_name)
    write_the_playlist_url(playlist_dir_name, the_playlist_url)


def get_playlist_url_from_file(playlist_dir_name):
    with open(f"{playlist_dir_name}/the_playlist_url.txt", mode='r', encoding='utf-8') as f:
        the_playlist_url = f.read()
    return the_playlist_url


def get_playlist_object_from_file(playlist_dir_name):
    old_vid_obj_list = []
    with open(f"{playlist_dir_name}/videoslist.json", mode='r', encoding='utf-8') as f:
        vid_objs  = json.load(f, strict=False)
        for obj in vid_objs['Video_objects']:
            old_vid_obj_list.append(VideoObject(
            f"thumbnails/{obj['thumbnail_path']}.jpg", obj['title'], obj['url'], obj['author'], obj['description']))
    return old_vid_obj_list


def check_playlist_integrity():
    playlist_dir_name = input(
        'Enter the name of playlist in:\n')
    the_playlist_url = get_playlist_url_from_file(playlist_dir_name)
    print(f"{the_playlist_url}")
    old_vid_obj_list = get_playlist_object_from_file(playlist_dir_name)
    #print(old_vid_obj_list)
    new_vid_obj_list = create_video_obj_list(playlist_dir_name, the_playlist_url, False)
    print(new_vid_obj_list)
    old_vid_obj_url_list = []
    #print(f"Old:\n\n")
    for obj in old_vid_obj_list[0:4]:
        old_vid_obj_url_list.append(obj.url)
        #print(f"{obj.url}\n")

    new_vid_obj_url_list = []
    print("New:\n\n")
    for obj in new_vid_obj_list:
        print(f"Objurl: {obj.url}")
        new_vid_obj_url_list.append(obj.url)
        print(f"{obj.url}\n")
    missing_videos = []
    for old_url in old_vid_obj_url_list:
        if old_url not in new_vid_obj_url_list:
            missing_videos.append(old_url)
    print(f'Missing: {missing_videos}')


# the_playlist = Playlist('https://www.youtube.com/playlist?list=PL-nKcT3XDGcIuGnq4l92ZRLY2s7rUJENV')
# the_playlist = Playlist('https://www.youtube.com/playlist?list=PL-nKcT3XDGcJT1v19mezBVRvyvDAx8oas')



mode = init_promt()
if mode == "add":
    create_playlist_data_backup()
elif mode == "check":
    check_playlist_integrity()
else:
    print("Something went wrong.")

