from pytube import Playlist
import requests
import os
import re
class VideoObject1:
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




ext_vid_obj_list = [VideoObject1("""thumbnails/Ironmouse on Connor's Hug Emote.jpg""", """Ironmouse on Connor's Hug Emote""", """https://www.youtube.com/watch?v=Y1Vn0tTn7Y8""", """RexxDroid [Vtuber Clips]""", """Like and subscribe for more vtuber content! (─‿‿─)
Check her out links below!

TWITCH
https://www.twitch.tv/ironmouse
TWITTER
https://twitter.com/ironmouse
YOUTUBE
https://www.youtube.com/ironmouseparty
STREAM
https://www.twitch.tv/videos/1164835840

CDawgVA emote- https://twitter.com/MAMETCHl/status/1444040729446203395/photo/1

---------------------------------------------------------------
My Twitter: https://twitter.com/RexxDroid
My Twitch: https://www.twitch.tv/rexxdroid

#ironmouse #vtuber #Vstreamer #vshojo 
#ENvtuber #Englishvtuber #VtuberEn #VtuberEnglish"""),

VideoObject1("""thumbnails/CDawgVA loses his mind and turns into memes (feat. IronMouse).jpg""", """CDawgVA loses his mind and turns into memes (feat. IronMouse)""", """https://www.youtube.com/watch?v=_nTJ7dNVD28""", """Alexa""", """CDawgVA and IronMouse were getting ready to play Golf It! during Connor's subathon... but Connor had to download it first (and IronMouse update it).

#CDawgVA #ironmouse #EnVtuber #Vshojo #vtuber

It took a while, so during that time, Connor decided to turn himself into memes. Clearly, as the subathon was reaching its conclusion, Connor was losing more and more of his sanity.



Also, please be nice to Mousey. She was medicated, so a bit loopy. It was very late for her too, and she was very kind to spend around 8 hours playing with Connor.

Video trimmed down and edited by me, taken from Connor's Twitch VOD: https://www.twitch.tv/videos/1159802063




Follow Connor's Twitch: https://www.twitch.tv/cdawgva
Connor's main YouTube: https://www.youtube.com/c/CDawgVA
Connor's second YouTube: https://www.youtube.com/channel/UCoil_VoKvJY4kdlBOZv974w


🐭 🐭 🐭
Follow IronMouse!
https://www.youtube.com/channel/UChgPVLjqugDQpRLWvC7zzig
https://www.twitch.tv/ironmouse
https://twitter.com/ironmouse
🐭 🐭 🐭

Twitter: https://twitter.com/CDawgVA
Facebook: https://www.facebook.com/CDawgVA/
Discord: https://discord.gg/cdawgva
Instagram: http://bit.ly/2g1IZWM"""),

VideoObject1("""thumbnails/CDawgVA told ironmouse why they are so good together.jpg""", """CDawgVA told ironmouse why they are so good together""", """https://www.youtube.com/watch?v=cKxO_MGPDAE""", """Rusian X {VTuber Enthusiast}""", """Watch me live in my https://www.twitch.tv/roosianx every 12 p.m/noon (GMT-4) I STREAM EVERYDAY!!??
If you guys found my stream entertaining why not try following my twitch and come back :))


Watch me everyday to never miss out on your favorite Vtuber clips! 

Follow CdawgVA in here:
Twitter: http://bit.ly/2fG2i5n​
Facebook: https://www.facebook.com/CDawgVA/​
Discord: https://discord.gg/cdawgva​
Twitch: https://www.twitch.tv/cdawgva​
Instagram: http://bit.ly/2g1IZWM​


Follow ironmouse in here:
- https://www.youtube.com/c/IronMouseParty/about
- https://www.twitch.tv/ironmouse​
- https://twitter.com/Iron_Mouse​





#CDawgVA #ironmouse #EnVtuber #Vshojo #vtuber





Thumbnail source:
https://twitter.com/cumdare_/status/1443650173649838081""")]

