#!/usr/bin/env python
"""
Written Edward Kan

This tools is help stupid Ryoko serach out of stock item from aliexpress
open multiple tabs for the serach result from browser 

sudo apt install python3
sudo apt install python3-pip
pip install -U PyYAML
"""

import webbrowser
import argparse
import yaml
import os
import tkinter as tk
from tkinter import simpledialog
from os import path

urls = {}
URLS_FILE = '/urls.yaml'
SEARCH = 'search?origin=y&SearchText='


def get_args():
    """
    Argurments parser
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--words',
            required=True,
            action='store',
            help='enter the search keyword')

    args = parser.parse_args()
    return args


def main():
    """
    Initialize config
    """
    url_file = os.getcwd() + URLS_FILE
    load_config(url_file, urls)
    browse_urls()
    

def browse_urls():
    """
    Open tab per each keyword search from url
    """
    args = get_args()
    chrome_path = '/usr/bin/google-chrome %s'
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)

    #open new instance of chrome
    os.system(r'/usr/bin/google-chrome %s')

    for key, url in urls.items():
        webbrowser.get(chrome_path).open_new_tab(url+SEARCH+args.words) 


def load_config(file_path, urls):
    """
    Load yaml urls 
    """
    if path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                documents = yaml.full_load(file)
                for key, value in documents.items():
                    urls.update({key:value})
            except:
                print("Could not read config file")
                exit(1)


if __name__ == "__main__":
    main()
