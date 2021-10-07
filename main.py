# from pytube import YouTube
from pytube import Playlist
import requests
import os
import re


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
    playlist_url = input('Enter the playlist url')
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


def create_video_obj_list(playlist_dir_name):
    # the_playlist = Playlist('https://www.youtube.com/playlist?list=PL-nKcT3XDGcIuGnq4l92ZRLY2s7rUJENV')
    # the_playlist = Playlist('https://www.youtube.com/playlist?list=PL-nKcT3XDGcJT1v19mezBVRvyvDAx8oas')
    # the_playlist = Playlist('https://www.youtube.com/playlist?list=PL-nKcT3XDGcJT1v19mezBVRvyvDAx8oas')
    the_playlist_url = get_playlist_url_from_user()
    the_playlist = Playlist(the_playlist_url)
    video_obj_list = []
    list_count = 0
    for video in the_playlist.videos:
        video_obj_list.append(VideoObject(
            f"thumbnails/{video.title}.jpg", video.title, the_playlist.video_urls[list_count], video.author, video.description))
        img_data = requests.get(video.thumbnail_url).content
        with open(f'{playlist_dir_name}/thumbnails/{video.title}.jpg', 'wb') as handler:
            handler.write(img_data)
        list_count += 1
        if list_count == 3:
            break
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
    with open("videoslist.txt", mode='w', encoding='utf-8') as f:
        obj_count = 0
        f.write('ext_vid_obj_list = [')
        for obj in video_obj_list:
            f.write(
                f'obj{obj_count}({obj.thumbnail_path}, {obj.title}, {obj.url}, {obj.author}, {obj.description}),\n\n')
            obj_count += 1


def create_playlist_data_backup():
    playlist_dir_name = get_playlist_name_from_user()
    check_and_create_playlist_dir(playlist_dir_name)
    vid_obj_list = create_video_obj_list(playlist_dir_name)
    write_to_visual_list_html_file(vid_obj_list, playlist_dir_name)
    write_vid_obj_list(vid_obj_list, playlist_dir_name)


# the_playlist = Playlist('https://www.youtube.com/playlist?list=PL-nKcT3XDGcIuGnq4l92ZRLY2s7rUJENV')
# the_playlist = Playlist('https://www.youtube.com/playlist?list=PL-nKcT3XDGcJT1v19mezBVRvyvDAx8oas')


if init_promt() == "add":
    create_playlist_data_backup()
