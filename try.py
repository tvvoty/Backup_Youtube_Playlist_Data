# from pytube import YouTube
from pytube import Playlist
import re
import requests


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


def create_video_obj_list():
    # the_playlist = Playlist('https://www.youtube.com/playlist?list=PL-nKcT3XDGcIuGnq4l92ZRLY2s7rUJENV')
    # the_playlist = Playlist('https://www.youtube.com/playlist?list=PL-nKcT3XDGcJT1v19mezBVRvyvDAx8oas')
    the_playlist = get_playlist_url_from_user()
    video_obj_list = []
    list_count = 0
    for video in the_playlist.videos:
        video_obj_list.append(VideoObject(
            f"thumbnails/{video.title}.jpg", video.title, the_playlist.video_urls[list_count], video.author, video.description))
        img_data = requests.get(video.thumbnail_url).content
        with open(f'{get_playlist_name_from_user}/thumbnails/{video.title}.jpg', 'wb') as handler:
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


def write_to_visual_list_html_file():
    try:
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


def create_playlist_data_backup():
    try:
        html_from_template = get_tamplate_html()
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
