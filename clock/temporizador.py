import tkinter as tk
from tkinter import *
from time import time, sleep

# Definição das variáveis globais
tempo_anterior = time()
tempo_total = 50 * 60  # Tempo total em segundos (50 minutos)
tempo_restante = tempo_total
rodando = False
milissegundos = 0
texto_tempo = None  # Inicializa a variável global texto_tempo

# Cores
cor1 = "#0a0a0a"  # Preto
cor2 = "#fafcff"  # Branco
cor4 = "#eb463b"  # Vermelho


def atualizar_temporizador():
    global tempo_restante, rodando, milissegundos, tempo_anterior, texto_tempo

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
            texto_tempo.set(
                f"{tempo_restante // 60:02d}:{tempo_restante % 60:02d}:{milissegundos:02d}"
            )

            # Condição para tempo esgotado
            if tempo_restante <= 0:
                rodando = False
                texto_tempo.set("Perdeu")

        # Atualização da tela a cada 10 milissegundos
        janela.after(10, atualizar_temporizador)


def iniciar_temporizador():
    global rodando
    rodando = True
    atualizar_temporizador()


def parar_temporizador():
    global rodando
    rodando = False


def reiniciar_temporizador():
    global tempo_restante, texto_tempo
    tempo_restante = tempo_total
    texto_tempo.set(
        f"{tempo_total // 60:02d}:{tempo_total % 60:02d}:{tempo_total % 60:02d}"
    )


def relogio():
    global texto_tempo, janela
    janela = Tk()
    janela.title("Temporizador")
    janela.geometry("1920x1820")
    janela.configure(bg=cor1)
    janela.resizable(width=False, height=False)

    texto_tempo = tk.StringVar()  # Agora estamos modificando a variável global
    texto_tempo.set(
        f"{tempo_total // 60:02d}:{tempo_total % 60:02d}:{tempo_total % 60:02d}"
    )

    # iniciar_temporizador()

    label_tempo = tk.Label(
        janela,
        textvariable=texto_tempo,
        font=("Times 50 bold"),
        bg=cor1,
        fg=cor4,
    )
    label_tempo.pack()

    botao_iniciar = tk.Button(
        janela,
        text="Iniciar",
        command=iniciar_temporizador,
        width=10,
        height=2,
        bg=cor1,
        fg=cor2,
        font=("Ivy 8 bold"),
        relief="raised",
        overrelief="ridge",
    )
    botao_iniciar.place(x=820, y=90)

    botao_parar = tk.Button(
        janela,
        text="Parar",
        command=parar_temporizador,
        width=10,
        height=2,
        bg=cor1,
        fg=cor2,
        font=("Ivy 8 bold"),
        relief="raised",
        overrelief="ridge",
    )
    botao_parar.place(x=910, y=90)

    botao_reiniciar = tk.Button(
        janela,
        text="Reiniciar",
        command=reiniciar_temporizador,
        width=10,
        height=2,
        bg=cor1,
        fg=cor2,
        font=("Ivy 8 bold"),
        relief="raised",
        overrelief="ridge",
    )

    botao_reiniciar.place(x=1000, y=90)

    janela.mainloop()


relogio()
