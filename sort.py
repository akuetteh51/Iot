# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 14:03:17 2021

@author: root
"""
import os 
from pathlib import Path

Subdirectories={
    "DOCUMENTS":['.pdf','.doc','.docx','.csv','.txt'],
    "AUDIO":['.m4b','.m4a','.mp3'],
    "VIDOES":['.mp4','.mov','.avi'],
    "IMAGES":['.jpg','.jpeg','.png'],
    "ZIP":['.iso','.zip','.7z'],
    "Pythonfiles":['.py']
    }


def pickDirectory(value):
    for category,suffixes in Subdirectories.items():
        for suffix in suffixes:
            if suffix==value:
                return category
            
print(pickDirectory(".py"))
def organize():
    for items in os.scandir():
        #return items
        print(items)
        filepath=Path(items)
        print(filepath)
        filetype=filepath.suffix.lower()
        print(filetype)
print(organize())