import subprocess
import re

def read_metafile():
    proc = subprocess.check_output("exiftool porwaniekm.mov")
    data = proc.decode('utf-8')
    group = re.findall(r"(.+): (.+)", data)
    meta_list = []

    for data in group:
        mini = []
        mini.append(data[0].strip())
        mini.append(data[1].strip())
        meta_list.append(mini)
        
    return meta_list