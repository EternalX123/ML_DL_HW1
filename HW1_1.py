import requests
import json
from bs4 import BeautifulSoup
from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
from HW1_2 import ResizeImage


def download_img(url_info):
    if url_info[1]:
        print("-----------downloading image %s"%(url_info[0]))
        try:
            url = url_info[0]
            response = requests.get(url)
            img = response.content
            
            # Save Path
            path='%s' % (url_info[1])
            with open(path, 'wb') as f:
                f.write(img)
            return (True, path)
            
        except Exception as ex:
            print("--------Error----")
            pass

root = Tk()  
root.geometry('1000x600') 

url ='https://m.mugzone.net/index'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/55.0.2883.87 Safari/537.36'}
r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text)

class GETPICTURE:
    def get_pic(self):
        j=0
        name=[]
        name1=[]
        for i in soup.find_all("div"):
            try:
                if i['class'][0]=='g_map':
                    download_img([i.find('a').find_all("div")[0].get('style')[22:-1],str(j)+".png"])
                    download_img(['https://m.mugzone.net/'+i.find('img').get('src'),'type'+str(j)+".png"])
                    name.append(i.find_all('p')[0].string)
                    name1.append(i.find_all('p')[1].string)
                    j+=1
            except:
                1
        return [name,name1]

names=GETPICTURE().get_pic()
name=names[0]
name1=names[1]

for k in range(len(name)):
    ResizeImage(k,400,filein = 'D:\\python_and_ML\\'+str(k)+'.png')
    ResizeImage(k,50,filein = 'D:\\python_and_ML\\'+'type'+str(k)+'.png')

k=0
def getmap():
    global k
    image_name = str(k)+'.png'
    image_name1 = 'type'+str(k)+'.png'
    imag = cv2.imread(image_name)
    imag1 = cv2.imread(image_name1)
    b,g,r = cv2.split(imag)
    img = cv2.merge((r,g,b))
    b,g,r = cv2.split(imag1)
    img1 = cv2.merge((r,g,b))
    im = Image.fromarray(img)
    im1 = Image.fromarray(img1)
    imgtk = ImageTk.PhotoImage(image=im) 
    imgtk1 = ImageTk.PhotoImage(image=im1) 
    l.config(image = imgtk)
    l.image = imgtk
    ptype.config(image = imgtk1)
    ptype.image = imgtk1
    m.config(text=name[k])
    n.config(text=name1[k])
    k+=1
 
def lastpage():
    global k
    k-=2
    image_name = str(k)+'.png'
    image_name1 = 'type'+str(k)+'.png'
    imag = cv2.imread(image_name)
    imag1 = cv2.imread(image_name1)
    b,g,r = cv2.split(imag)
    img = cv2.merge((r,g,b))
    b,g,r = cv2.split(imag1)
    img1 = cv2.merge((r,g,b))
    im = Image.fromarray(img)
    im1 = Image.fromarray(img1)
    imgtk = ImageTk.PhotoImage(image=im) 
    imgtk1 = ImageTk.PhotoImage(image=im1) 
    l.config(image = imgtk)
    l.image = imgtk
    ptype.config(image = imgtk1)
    ptype.image = imgtk1
    m.config(text=name[k])
    n.config(text=name1[k])
    k+=1

var = StringVar()    # ???label??????????????????????????????????????????var?????????hit_me?????????????????????????????????????????????
l = Label(root, textvariable = var, font=('Arial', 12))
ptype = Label(root)
m = Label(root) 
n=Label(root)
b = Button(root, text='????????????????????????', font=('Arial', 14), width=14, height=1, command=getmap)
b1=Button(root,text='?????????',font=('Arial', 14), width=14, height=1, command=lastpage)

b.grid(column=1, row=0)
b1.grid(column=0,row=0)
m.grid(column=1, row=1)
n.grid(column=1, row=2)
ptype.grid(column=1, row=3)
l.grid(column=1, row=4)

root.mainloop()
