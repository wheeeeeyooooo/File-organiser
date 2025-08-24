import os
import shutil
folder=input("enter the folder location where you want to organise your files")
file=os.listdir(folder)

images=os.path.join(folder,"images")
documents=os.path.join(folder,"documents")
audios=os.path.join(folder,"audios")
videos=os.path.join(folder,"videos")
others=os.path.join(folder,"others")
os.makedirs(images,exist_ok=True)
os.makedirs(documents,exist_ok=True)
os.makedirs(audios,exist_ok=True)
os.makedirs(videos,exist_ok=True)
os.makedirs(others,exist_ok=True)

a=['.jpg','.jpeg','.png','.gif','.bmp','.tiff','.tif','.webp']
b=['.pdf','.doc','.docx','.ppt','.pptx','.xls','.xlsx','.txt','.csv']
c=['.mp3','.wav','.aac','.flac','.ogg','.wma','.mpeg']
d=['.mp4','.mov','.avi','.mkv','.wmv','.flv']

for i in file:
    name,ext=os.path.splitext(i)
    source=os.path.join(folder,i)
    if ext.lower() in a:
        shutil.move(source,images)
    elif ext.lower() in b:
        shutil.move(source,documents)
    elif ext.lower() in c:
        shutil.move(source,audios)
    elif ext.lower()in d:
        shutil.move(source,videos)
    else:
        shutil.move(source,others)
print("files organised successfully")