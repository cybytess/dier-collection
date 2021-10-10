def load(file):
    content = open(file, encoding='utf-8', mode='r')
    content = content.readlines()
    return content


def read(file, mode):
    if mode == "title" or mode == "t":
        content = file[5].split('::')[1]
        return content
    if mode == "location" or mode == "l":
        content = file[4].split('::')[1]
        return content
    if mode == "start" or mode == "s":
        content = file[2].split('::')[1]
        return content
    if mode == "end" or mode == "e":
        content = file[3].split('::')[1]
        return content


#print(read(load("bookmarks001.SCA"), "l"))
