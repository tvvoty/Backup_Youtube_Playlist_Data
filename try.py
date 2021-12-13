import os

#
# os.mkdir("testfolder2/")
# with open("testfolder2/testfile.txt", mode='w', encoding='utf-8') as template:
#     template.write("hello")

# with open(f"test.txt", mode='r', encoding='utf-8') as f:
#     for line in f:
#         the_playlist_url = f.readlines()
#
# print(the_playlist_url)


def get_url():
    with open("test.txt", mode='r', encoding='utf-8') as template:
        html_from_template = template.read()
        #print(f'html lines are: {html_lines}')
        return html_from_template


def get_tamplate_html():
    with open("html_template.html", mode='r', encoding='utf-8') as template:
        for line in template:
            print(line)
            html_from_template = template.readlines()
            #print(f'html lines are: {html_lines}')
        return html_from_template


# u = get_url()
# print(u[2])
# print(get_tamplate_html)

# g = get_tamplate_html()
#
# print(g)

t = ["""Hello""", """w'o"ld""", """!"""]
print(t)
