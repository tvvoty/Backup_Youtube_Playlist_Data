from pytube import YouTube
from pytube import Playlist
yt = YouTube('https://www.youtube.com/watch?v=qv3DQNchmHg&list=PL-nKcT3XDGcJT1v19mezBVRvyvDAx8oas')

print(yt.description)
