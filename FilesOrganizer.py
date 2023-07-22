import os
import imghdr
import mimetypes
import shutil
def get_file_type(file_name):
    mime_type = mimetypes.guess_type(file_name)[0]
    if mime_type is None:
        return None

    return mime_type.split('/')[0]
def organize(path):
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(path+"/"+file):
            mime_type = get_file_type(file)
            if mime_type == "vedio":
                if os.path.isdir(path+"/Videos"):
                    shutil.move(path +"/" + file, path+"/Videos/"+file)
                else:
                    os.mkdir(path+ "/Videos")
                    shutil.move(path +"/" + file, path+"/Videos/"+file)
            elif mime_type == "audio":
                if os.path.isdir(path+"/Audio"):
                    shutil.move(path +"/" + file, path+"/Audio/"+file)
                else:
                    os.mkdir(path+ "/Audio")
                    shutil.move(path +"/" + file, path+"/Audio/"+file)
            elif mime_type == "image":
                if os.path.isdir(path+"/Images"):
                    shutil.move(path +"/" + file, path+"/Images/"+file)
                else:
                    os.mkdir(path+ "/Images")
                    shutil.move(path +"/" + file, path+"/Images/"+file)
            elif mime_type == "doc":
                if os.path.isdir(path+"/Documents"):
                    shutil.move(path +"/" + file, path+"/Documents/"+file)
                else:
                    os.mkdir(path+ "/Documents")
                    shutil.move(path +"/" + file, path+"/Documents/"+file)
            elif mime_type == "application":
                if os.path.isdir(path+"/Compressed"):
                    shutil.move(path +"/" + file, path+"/Compressed/"+file)
                else:
                    os.mkdir(path+ "/Compressed")
                    shutil.move(path +"/" + file, path+"/Compressed/"+file)
            else:
                if os.path.isdir(path+"/Misc"):
                    shutil.move(path +"/" + file, path+"/Misc/"+file)
                else:
                    os.mkdir(path+ "/Misc")
                    shutil.move(path +"/" + file, path+"/Misc/"+file)
path = r"</path/to/folder>"
organize(path)
