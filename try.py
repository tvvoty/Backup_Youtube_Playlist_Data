from pytube import YouTube
from pytube import Playlist
# yt = YouTube('https://www.youtube.com/watch?v=qv3DQNchmHg&list=PL-nKcT3XDGcJT1v19mezBVRvyvDAx8oas')

# print(yt.description)


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


def create_playlist_data_backup:
    pass


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
        with open(f'thumbnails/{video.title}.jpg', 'wb') as handler:
            handler.write(img_data)
        list_count += 1
        if list_count == 3:
            break
    return video_obj_list
