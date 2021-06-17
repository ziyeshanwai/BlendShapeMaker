#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import _tkinter
import tkinter as tk
# import imp
import os
import sys
APP_ROOT = os.path.dirname( os.path.abspath( __file__ ) )
sys.path.append(os.path.join(APP_ROOT,'lib'))
import Menu
import BMApp
def main():
    
    ''' Create Menu to load data '''
    # M = imp.load_source('Menu', APP_ROOT+'/lib/Menu.py')
    root = tk.Tk()
    root.title(u"BlendshapeMaker")
    menu_app = Menu.Menu(root)
    menu_app.mainloop()
    
    '''　If a data path has been selected:
        Create the main application and start the loop'''
    if (len(menu_app.filename) > 0):
        # A = imp.load_source('BMApp', APP_ROOT+'/lib/BMApp.py')
        root = tk.Tk()
        app = BMApp.BMApp(menu_app.filename, root)
        app.mainloop()
    
    return 0

if __name__ == '__main__':
    main()
    exit(0)