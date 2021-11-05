def load(path):
    content = open(path, encoding='utf-8', mode='r').readlines()
    open(path, encoding='utf-8', mode='r').close()
    return content


def read(file, mode):
    if mode == "title" or mode == "t":
        content = file[5].split('::')[1]
        return content
    if mode == "path" or mode == "p":
        content = file[4].split('::')[1]
        return content
    if mode == "start" or mode == "s":
        content = file[2].split('::')[1]
        return content
    if mode == "end" or mode == "e":
        content = file[3].split('::')[1]
        return content
    if mode == "name" or mode == "n":
        content = file[4].split('\\')[len(file[4].split('\\')) - 1]
        return content


def save(file, path):
    f = open(path, encoding='utf-8', mode='w')
    for x in file:
        f.write(x)
    f.close()


def write(file, mode, content):
    if mode == "title" or mode == "t":
        file[5] = '[&L]::' + content + '\n'
    if mode == "path" or mode == "p":
        file[4] = '[&P]::' + content + '\n'
    if mode == "start" or mode == "s":
        file[2] = '[&A]::' + content + '\n'
    if mode == "end" or mode == "e":
        file[3] = '[&B]::' + content + '\n'
    return file
