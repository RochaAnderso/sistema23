import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk
import pyttsx3
import speech_recognition as sr
rec = sr.Recognizer()
def falar():
    falar = pyttsx3.init()
    falar.say('''Maketa Martelão''')
    falar.runAndWait()

# Criação da janela principal
janela = tk.Tk()

# Define as dimensões da janela
largura = 1366
altura = 768
janela.geometry(f"{largura}x{altura}")

# Carregamento e exibição da imagem em tela cheia
imagem_principal = Image.open("magens/iparan.png")
imagem_principal = imagem_principal.resize((largura, altura))
imagem_principal_tk = ImageTk.PhotoImage(imagem_principal)

label_imagem_principal = tk.Label(janela, image=imagem_principal_tk)
label_imagem_principal.pack()


botaosaibamais=ctk.CTkButton(master=label_imagem_principal,width=12,text='SAIBA MAIS')
botaosaibamais.place(x=100,y=100)
# 

# Inicialização do mecanismo de fala
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Iniciar a fala após a janela estar aberta
janela.after(0, falar)

# Execução da janela principal
janela.mainloop()
