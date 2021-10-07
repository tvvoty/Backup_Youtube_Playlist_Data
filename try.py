import os

#
# os.mkdir("testfolder2/")
# with open("testfolder2/testfile.txt", mode='w', encoding='utf-8') as template:
#     template.write("hello")

playlist_dir_name = "testtryfolder123456"


def check_and_create_playlist_dir(playlist_dir_name):
    if not os.path.isdir(f'./{playlist_dir_name}'):
        try:
            # os.mkdir(playlist_dir_name)
            os.makedirs(f"./{playlist_dir_name}/thumbnails")
        except Exception as e:
            print(f"Something went wrong: {e}")
    else:
        print(f"{playlist_dir_name}")


check_and_create_playlist_dir(playlist_dir_name)
