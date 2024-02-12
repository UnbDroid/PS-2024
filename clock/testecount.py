import tkinter as tk
from tkinter import *
import tkinter
from time import time, sleep



global tempo_anterior

# Definição das variáveis
tempo_total = 50 * 60  # Tempo total em segundos (50 minutos)
tempo_restante = tempo_total
rodando = False
milissegundos = 0

#? Cores
cor1 = "#0a0a0a"  # Preto
cor2 = "#fafcff"  # Branco
cor3 = "#21c25c"  # Verde
cor4 = "#eb463b"  # Vermelho
cor5 = "#dedcdc"  # Cinza
cor6 = "#3080f0"  # Azul

#* Função para atualizar o temporizador


tempo_anterior = time()

def atualizar_temporizador():
    global tempo_restante, rodando, milissegundos, tempo_anterior

    if rodando:
        tempo_atual = time()
        tempo_decorrido = tempo_atual - tempo_anterior

        if tempo_decorrido >= 0.01:  # 0.01 segundos, ajuste conforme necessário
            tempo_anterior = tempo_atual

            if milissegundos == 0:
                milissegundos = 99
                tempo_restante -= 1
            else:
                milissegundos -= 1

            # Atualização do texto do tempo
            texto_tempo.set(f"{tempo_restante // 60:02d}:{tempo_restante % 60:02d}:{milissegundos:02d}")

            # Condição para tempo esgotado
            if tempo_restante <= 0:
                rodando = False
                texto_tempo.set("Perdeu")

        # Atualização da tela a cada 10 milissegundos
        janela.after(10, atualizar_temporizador)


#* Função para diminuir o tempo
def diminuir_tempo():
    global tempo_restante
    tempo_restante -= 15
    atualizar_temporizador()

#* unções para os botões
def iniciar_temporizador():
    global rodando
    rodando = True
    atualizar_temporizador()


def parar_temporizador():
    global rodando
    rodando = False


def reiniciar_temporizador():
    global tempo_restante
    tempo_restante = tempo_total
    texto_tempo.set(f"{tempo_total // 60:02d}:{tempo_total % 60:02d}:{tempo_total % 60:02d}")


# Criação dos botões


#? Criação da janela principal
janela = Tk()
janela.title("Temporizador")
janela.geometry("300x140")
janela.configure(bg=cor1)
janela.resizable(width=False, height=False)

#?Criação do widget para mostrar o tempo
texto_tempo = tk.StringVar()
texto_tempo.set(f"{tempo_total // 60:02d}:{tempo_total % 60:02d}:{tempo_total % 60:02d}")

label_tempo = tk.Label(
    janela,
    textvariable=texto_tempo,
    font=("Times 50 bold"),
    bg=cor1,
    fg=cor4,
)
label_tempo.pack()



#? Criação de botões 

botao_iniciar = tk.Button(
    janela, text="Iniciar",
    command=iniciar_temporizador,
    width = 10, height = 2,
    bg = cor1,fg = cor2,
    fon = ("Ivy 8 bold"),
    relief='raised',
    overrelief = "ridge",
)
botao_iniciar.place(x=20,y=90)

botao_parar = tk.Button(
    janela, text="Parar",
    command=parar_temporizador,
    width = 10, height = 2,
    bg = cor1,fg = cor2,
    fon = ("Ivy 8 bold"),
    relief='raised',
    overrelief = "ridge",
)
botao_parar.place(x=110,y=90)

botao_reiniciar = tk.Button(
    janela, text="Reiniciar",
    command=reiniciar_temporizador,
    width = 10, height = 2,
    bg = cor1,fg = cor2,
    fon = ("Ivy 8 bold"),
    relief='raised',
    overrelief = "ridge",
)

botao_reiniciar.place(x=200,y=90)


# teste de botão :D
botao_diminuir = tk.Button(janela, text="Diminuir 15 Segundos", command=diminuir_tempo)
botao_diminuir.pack()

# Execução da interface gráfica
janela.mainloop()
