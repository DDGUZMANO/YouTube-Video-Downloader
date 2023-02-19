# librerías Tkinter, moviepy, pytube y shutil.
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import VideoFileClip
import shutil

ventana = Tk()
ventana.title('YouTube Downloader')

# Funciones

def ruta_descarga():
    ruta = filedialog.askdirectory()
    label_ruta.config(text=ruta,fg='#626462')
    
def descargar():
    obtener_link = entrada.get()
    ruta_usuario = label_ruta.cget('text')
    video_mp4 = YouTube(obtener_link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(video_mp4)
    video_clip.close()
    shutil.move(video_mp4 , ruta_usuario)
    # alert.config(text='Descarga finalizada', fg='#138113')
    

logo = PhotoImage(file='yt.png')
new_logo = logo.subsample(9,9)
label_logo = Label(ventana,image=new_logo)

label_encabezado = Label(ventana, text='Descargue sus videos', font=('Roboto',15))
label_ingrese = Label(ventana, text='Ingrese el link de Youtube',font=('Roboto',10))

entrada = Entry(ventana, width=45,highlightcolor='red',highlightthickness=2,font=('Roboto',11))

label_ruta = Label(ventana, text='Seleccione la ruta de la carpeta de descarga', font=('Roboto',11))

boton_ruta = Button(ventana,text='Ruta de descarga',bg='#5E646B',padx=5,pady=5,font=('Roboto',10), command=ruta_descarga)

boton_descarga = Button(ventana,text='Descargar',bg='#386B41',padx=5,pady=5,font=('Roboto',10), command=descargar)




label_encabezado.pack()

label_logo.pack()
label_ingrese.pack()
entrada.pack()
label_ruta.pack(pady=5)
boton_ruta.pack()
boton_descarga.pack(pady=5)

ventana.mainloop()