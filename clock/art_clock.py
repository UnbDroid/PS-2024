from tkinter import *
import tkinter

#cores
cor1 = "#0a0a0a"  # black 
cor2 = "#fafcff"  # white 
cor3 = "#21c25c"  # green 
cor4 = "#eb463b"  # red 
cor5 = "#dedcdc"  # gray 
cor6 = "#3080f0"  # blue 

#? Janela

janela = Tk()
janela.title("")
janela.geometry('300x180')
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)
#! Definindo variaveis globais
global contador
global tempo
global rodar
global limitador

#? Tempo

tempo = "50:00:00"
rodar = False
contador = -5

#? Função iniciar

def iniciar():
    global contador
    global tempo
    global limitador
    if rodar :
        #Antes do cronometro começar
        if contador <= -1:
            inicio = 'Começando em ' + str(contador)
            label_tempo['text'] = inicio 
            label_tempo['fon'] = 'Arial 10'
        
        #Rodando o cronometro
        else:
            label_tempo['fon'] = 'Times 50 bold'
            
            temporaria = str(tempo)
            m,s,mm = map(int,temporaria.split(":"))
            
            m = int(m)
            s = int(s)
            mm = int(limitador)
            
            
            
            
            
            
        label_tempo.after(1000,iniciar)
        contador += 1
 
#? Dando inicio
           
def start():
    global rodar
    rodar = True
    iniciar()








#? labels

label_app = Label(janela, text="Cronômetro", fon = ("Arial 10"), bg = cor1, fg = cor2)
label_app.place(x=20,y=5)

label_tempo = Label(janela, text = tempo, fon = ("Times 50 bold"), bg = cor1, fg = cor4)
label_tempo.place(x=20,y=30)


#? Botons

botao_iniciar = Button(janela,command=start, text='Iniciar', width = 10, height = 2,bg = cor1,fg = cor2, fon = ("Ivy 8 bold"), relief='raised', overrelief = "ridge" )
botao_iniciar.place(x=108,y=130)



janela.mainloop()

