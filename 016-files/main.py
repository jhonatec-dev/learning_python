import os

file_dir = "c:/projects/portfolio-astro/frontend/.vercel/output/static"


def get_path_with_index(path, list=[]):
    entries = os.scandir(path)
    for entry in entries:
        if entry.is_dir():
            get_path_with_index(entry.path, list)
        elif entry.is_file() and entry.name.endswith("index.html"):
            path = entry.path.replace(file_dir, "")
            path = path.replace("index.html", "")
            path = path.replace("\\", "/")
            list.append(path)
