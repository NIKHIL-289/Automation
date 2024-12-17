import os
import shutil
from os.path import splitext, exists, join
from shutil import move
from time import sleep

import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".mkv", ".qt", ".flv", ".swf", ".avchd"]
audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]
document_extensions = [".doc", ".docx", ".odt", ".txt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".epub", ".pages", ".zip"]

source_dir = "/Users/nikhiltripathi/Downloads/"
dest_dir_music = "/Users/nikhiltripathi/Downloads/music"
dest_dir_video = "/Users/nikhiltripathi/Downloads/videos"
dest_dir_image = "/Users/nikhiltripathi/Downloads/images1"
dest_dir_documents = "/Users/nikhiltripathi/Downloads/documents"


    

def move_file(directory):
    files = os.scandir(source_dir)
    for file in files:
        if file.is_file(): 
            name = file.name
            file_path = os.path.join(directory, name)
            
            _, extension = splitext(name)
            extension = extension.lower() 

            if extension in image_extensions[::]:
                shutil.move(file_path, dest_dir_image)
                print(f"{name}, moved to destination_path {dest_dir_image}\n")
            elif extension in video_extensions[::]:
                shutil.move(file_path, dest_dir_video)
                print(f"{name}, moved to destination_path {dest_dir_video}\n")
            elif extension in audio_extensions[::]:
                shutil.move(file_path, dest_dir_music)
                print(f"{name}, moved to destination_path {dest_dir_music}\n")
            elif extension in document_extensions[::]:
                shutil.move(file_path, dest_dir_documents)
                print(f"{name}, moved to destination_path {dest_dir_documents}\n")
            else:
                continue
    
move_file(source_dir)

print("!!!!!!!DONE!!!!!!!")
























        
    
    
    
