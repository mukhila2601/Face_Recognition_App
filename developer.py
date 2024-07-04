from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x790+0+0")
        self.root.title("face Recognition System")
        
        
        title_lbl=Label(self.root,text=" DEVELOPER ",font=("times new roman",38,"bold"),bg="green",fg="blue")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        img_top=Image.open(r"college_images\b3.jpg")
        img_top=img_top.resize((1300,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1300,height=720)
        
        # frame 
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=500,height=600)
        
        
        img_top1=Image.open(r"college_images\gl.jpeg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)
        
        
        #Developer info
          
        dev_label=Label(main_frame,text="My name is, HARI NARAYAN ",font=("times new roman",25,"bold"),bg="white",fg="brown")
        dev_label.place(x=0,y=5)
        
        dev_label=Label(main_frame,text="I am full stack developer",font=("times new roman",19,"bold"),bg="white")
        dev_label.place(x=0,y=50)
        
        dev_label=Label(main_frame,text="GL BAJAJ",font=("times new roman",40,"bold"),bg="white",fg="red")
        dev_label.place(x=0,y=150)
        
        #3rd
        img2=Image.open(r"college_images\a7.jpg")
        img2=img2.resize((500,390),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=205,width=500,height=390)
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()        