#!/usr/bin/env python
"""
Written Edward Kan

This tools is help stupid Ryoko serach out of stock item from aliexpress
open multiple tabs for the serach result from browser 

sudo apt-get install python3-tk
sudo apt install python3
sudo apt install python3-pip
pip install -U PyYAML

Add trusted source for desktop shortcut
gio set /path/to/your/shortcut.desktop "metadata::trusted" yes

"""

import webbrowser
import argparse
import os
import yaml
import tkinter as tk
from os import path
from tkinter import simpledialog
from tkinter import messagebox

urls = {}
URLS_FILE = '/urls.yaml'
SEARCH = 'search?origin=y&SearchText='
keyword = ''


def main():
    """
    Initialize config
    """
    user_input()
    url_file = os.path.dirname(os.path.realpath(__file__)) + URLS_FILE
    load_config(url_file, urls)
    browse_urls()


def user_input():
    """
    search keyword input dialog 
    """
    global keyword
    root = tk.Tk()
    root.withdraw()

    keyword = simpledialog.askstring(title="JFigures",
            prompt="What's search keyword?:")


def load_config(file_path, urls):
    """
    Load yaml urls 
    """
    #messagebox.showinfo("realpath", file_path)
    with open(file_path, 'r') as file:
    	documents = yaml.full_load(file)

    for key, url in documents.items():
        urls.update({key:url})


def browse_urls():
    """
    Open tab per each keyword search from url
    """
    global urls

    chrome_path = '/usr/bin/google-chrome %s'
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
    
    #open new instance of chrome
    os.system(r'/usr/bin/google-chrome %s')
    
    for key, url in urls.items():
        webbrowser.get(chrome_path).open_new_tab(url+SEARCH+keyword)


if __name__ == "__main__":
    main()
