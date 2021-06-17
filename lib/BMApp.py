#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from math import cos, sin, pi
from os import path
import imp
import time
from PIL import Image
from PIL import ImageTk
import cv2
import numpy as np
import _tkinter
import tkinter as tk
APP_ROOT = path.dirname( path.abspath( __file__ ) )
BMManager = imp.load_source('BMManager', APP_ROOT + '/BMManager.py')


class BMApp(tk.Frame):
    def __init__(self, path, master=None):
        self.path = path        #path for 3D Avatar
        self.root = master

        tk.Frame.__init__(self, master)

        self.pack()

        self.root.title(u"BlendshapeMaker")
        self.root.geometry("500x150+450+50")
        self.root.resizable(0, 0)

        self.Label = tk.Label(self.root, text=u"Make Blendshape models of\n\n%s\n" % self.path)
        self.Label.pack()

        self.Button = tk.Button(self.root, text=u'Start', padx=50, command=self.startapp)
        self.Button.pack()

        self.root.mainloop()

    def startapp(self):

        #disable Start Button
        self.Button.configure(state='disabled')

        self.Label2 = tk.Label(self.root, text=u"\nProcessing...")
        self.Label2.pack()
        self.root.after(50, self.routine)


    def routine(self):
        start_routine = time.time()
        self.root.destroy()
        #Load blendshapes
        print("******Load given Blendshape meshes******")
        self.BM = BMManager.BMMng('data/blendshapes/', self.path)
        self.BM.LoadBS()
        print(len(self.BM.BlendShapes), "Blendshapes are loaded")

        #Load Avatar
        print("******Load Avatar******")
        self.BM.LoadAvatar()

        #Rescale
        print("******Rescale Avatar******")
        self.BM.RescaleAvatar()

        #Triangle Correspondence
        print("******Triangle Correspondence******")
        self.BM.TriangleCorrespondence(0)

        #Deformation Transfer
        print("******Deformation transfer******")
        self.BM.DeformationTransfer()


        elapsed_time = time.time() - start_routine
        #End
        print("Complete. (Total : {:.2f} min)".format(elapsed_time/60))
