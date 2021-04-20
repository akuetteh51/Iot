# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 14:03:17 2021

@author: root
"""

Subdirectories={
    "DOCUMENTS":['.pdf','.doc','.docx','.csv','.txt'],
    "AUDIO":['.m4b','.m4a','.mp3'],
    "VIDOES":['.mp4','.mov','.avi'],
    "IMAGES":['.jpg','.jpeg','.png'],
    "ZIP":['.iso','.zip','.7z']
    }


def pickDirectory(value):
    for category,suffixes in Subdirectories.items():
        for suffix in suffixes:
            if suffix==value:
                return category
            
print(pickDirectory(".m4a"))
