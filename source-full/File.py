from tkinter import *
import tkinter_file

def function():
    req_url = 'http://someurl.com/{}'.format(tkinter_file.input)
    print(req_url)