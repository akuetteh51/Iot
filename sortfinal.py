# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 15:02:13 2021

@author: root
"""

import os
from pathlib import Path as p
os.chdir('../../Desktop/')
Subdirectories={
    "DOCUMENTS":['.pdf','.doc','.docx','.csv','.txt'],
    "AUDIO":['.m4b','.m4a','.mp3'],
    "VIDOES":['.mp4','.mov','.avi'],
    "IMAGES":['.jpg','.jpeg','.png'],
    "ZIP":['.iso','.zip','.7z'],
    "Pythonfiles":['.py']
    }

def Search(value):
    for categories,suffixes in Subdirectories.items():
        for suffix in suffixes:
            if suffix == value:
                return categories
    return 'MISC'
#print(Search('.pdf'))
def organize():
    for items in os.scandir():
        if items.is_dir():
            continue
        filepath=p(items)
        #print(filepath)
        filetype=filepath.suffix.lower()
        #print(filetype)
        directory=Search(filetype)
        print(directory)
        directoryPath=p(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
            
        filepath.rename(directoryPath.joinpath(filepath))
        

organize()