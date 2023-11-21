import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy

#Tải các model đã train để phân loại
from keras.models import load_model
model = load_model('my_model.h5')

#dictionary to label all traffic signs class.
classes = { 1:'Gioi han toc do 20km/h',
            2:'Gioi han toc do 30km/h',
            3:'Gioi han toc do 50km/h',
            4:'Gioi han toc do 60km/h',
            5:'Gioi han toc do 70km/h',
            6:'Gioi han toc do 80km/h',
            7:'Het gioi han toc do 80km/h',
            8:'Gioi han toc do 100km/h',
            9:'Gioi han toc do 120km/h',
            10:'Cam vuot qua',
            11:'Cam xe tren 3,5 tan vuot qua',
            12:'Quyen uu tien tai nga tu',
            13:'Duong uu tien',
            14:'Nhuong duong',
            15:'Dung lai',
            16:'Cam xe',
            17:'Cam xe tren 3,5 tan',
            18:'Cam vao',       
            19:'Nguy hiem khac',
            20:'Cho vong nguy hiem ben trai',
            21:'Cho vong nguy hiem ben phai',
            22:'Nhieu cho ngoat nguy hiem lien tiep',
            23:'Duong co o ga, loi lom',
            24:'Duong tron',
            25:'Duong hep ve phia phai',
            26:'Cong truong',
            27:'Giao nhau co tin hieu den',
            28:'Duong nguoi di bo cat ngang',  
            29:'Tre em',
            30:'Nguoi di xe dap cat ngang',
            31:'Tuyet lo nguy hiem',
            32:'Thu rung vuot qua duong',
            33:'Het han che toc do toi da',      
            34:'Phia truoc re phai',     
            35:'Phia truoc re trai',       
            36:'Di thang',      
            37:'Di thang hoac re phai',      
            38:'Di thang hoac re trai',      
            39:'Di sang phai',     
            40:'Di sang trai',      
            41:'Noi giao nhau voi vong xuyen',     
            42:'Het cam vuot',      
            43:'Het cam xe tren 3,5 tan'}
                 
#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Nhận dạng biển báo giao thông ')
top.configure(background='#ffffff')

label=Label(top,background='#ffffff', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)   
# predict classes
    pred_probabilities = model.predict(image)[0]
    pred = pred_probabilities.argmax(axis=-1)
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#011638', text="Biển báo: " +sign) 
  
def show_classify_button(file_path):
    classify_b=Button(top,text="Nhận dạng",command=lambda: classify(file_path),padx=10, pady=5, bg='#0077cc', fg='white', font=('arial', 10, 'bold'), bd=2, relief=tk.GROOVE)
    classify_b.configure(background='#97b6d2', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


upload=Button(top, text="Chọn hình ảnh", command=upload_image, padx=10, pady=5, bg='#0077cc', fg='white', font=('arial', 10, 'bold'), bd=2, relief=tk.GROOVE)
upload.configure(background='#97b6d2', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Nhận dạng biển báo giao thông",pady=10, font=('arial',10,'bold'))
heading.configure(background='#ffffff',foreground='#ea4335')

heading.pack()

top.mainloop()
