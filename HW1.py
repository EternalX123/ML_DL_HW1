import requests
import json
from bs4 import BeautifulSoup
from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np


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
root.geometry('500x300') 

url ='https://m.mugzone.net/index'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/55.0.2883.87 Safari/537.36'}
r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text)
j=0
imag=[]
for i in soup.find_all("div"):
    try:
        if i['class'][0]=='g_map':
            imag.append(download_img([i.find('a').find_all("div")[0].get('style')[22:-1],str(j)+".png"]))
            j+=1
    except:
        1
k=0
def hit_me():
    global k
    image_name = str(k)+'.png'
    imag = cv2.imread(image_name)
    b,g,r = cv2.split(imag)
    img = cv2.merge((r,g,b))
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im) 
    l.config(image = imgtk)
    l.image = imgtk
    k+=1
 

var = StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = Label(root, textvariable = var, font=('Arial', 12))

b = Button(root, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()
l.pack()
root.mainloop()
