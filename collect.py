#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import fnmatch
import google as Google

def find_files_in_folder(PATH):
    for files in os.listdir(PATH):
        if fnmatch.fnmatch(files, ['*.avi', 'mkv', 'rmvb', 'nrg', 'wmv']):
            print files


def find_pic_for_file(filename, method):
    print filename
    if method == "Google":
        Goo = Google.Google()
        options = Google.ImageOptions()
        options.image_type = Google.ImageType.CLIPART
        options.larger_than = Google.LargerThan.VGA
        search_res = Goo.search_images(filename)
        if len(search_res) > 1:
            return search_res[0].link

            
    for dirs in os.walk(PATH):
        for files in dirs[2]:
            #print files
            fname, ftype = os.path.splitext(files)
            if ftype in ['.avi', '.mkv', '.rmvb', '.nrg', '.wmv']:
                #find_pic_for_file(fname, "Google")