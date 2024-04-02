from tkinter import *
from tkinter import messagebox


#! Gabarito | 5 | 7 | 3 | 4 | 7 | 2 |
# Criar a janela principal com fundo preto
root = Tk()
root.configure(bg="black")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
# Variáveis para armazenar as perguntas e respostas
questions = [
    "Charada 1:\nEu sou um número inteiro.\nSe você me dividir por 2, o meu quociente é um número inteiro e o meu resto é nulo.\n\nAlém disso, se você olhar para Pi, eu estarei lá.\nQue número eu sou?",
    "Charada 2:\nSou um número primo menor que 10.\nSe me elevar ao quadrado, subtraírem 6 e multiplicarem por 3, obterás 81. Qual é o meu número?",
    "Charada 3:\nUm corpo acelerando em direção ao rosto do seu amigo a 10 m/s²\ntem massa similar a de uma xícara de 300 g,\nqual a força mínima que você tem que aplicar para que ele não se machuque?",
    "Charada 4:\nEu sou um número inteiro positivo.\nQuando dividido por 2, resulto em um quociente inteiro e resto zero.\nAlém disso, minha origem está na soma dos cinco primeiros números primos consecutivos,\ndividida por um primo distinto de 2.\nVocê sabe quem sou eu?",
    "Charada 5:\nSou um número primo menor que 10.\nSe me multiplicarem por 4, subtraírem 10 e depois dividirem por 2, obterão 9.\nQual é o meu número??",
    "Charada 6:\nUm corpo acelerando em direção ao rosto do seu amigo a 10 m/s²\ntem massa similar a de uma xícara de 200 g,\nqual a força mínima que você tem que aplicar para que ele não se machuque.",
    "Parabéns, você concluiu a PRIMEIRA etapa :) 🎆🎆\nAgora seu desafio será muito maior,o que teremos a seguir nesse angar de naves ??? hehe\nBoa sorte!\n\nEm um hangar de naves,\nEncontrei um tesouro perdido,\nCom ele, posso montar um código,\nQue, em um mundo digital,\nMe levará a um novo caminho.\n\n",
    "Meu Deus, você não desiste hein, vamos dificultar um pouquinho agora 👿\n\nAgora vamos pegar você espertinho🔪😡\n\n**Em uma espaçonave,\nDois mistérios estão escondidos,\nUm deles é uma cifra,\nO outro é uma chave.\nJuntos, eles formam um mistério,\nMas qual é esse mistério?**\n\n",
    #!lembre-se, aqui será o código onde vamos dificultar, vai executar uma charada com um certo tempo de partida.
]

answers = [
    "1",  # 5
    "1",  # 7
    "1",  # 3
    "1",  # 4
    "1",  # 7
    "1",  # 2
    "onepieto",  #! Dica : O tesouro perdido são as peças do ábaco, que representam os dígitos de um número na tabela ASCII.
    "1",
]

# Índice da pergunta atual
question_index = 0

# Adicionar um rótulo com a pergunta e texto branco
question = Label(
    root, text=questions[question_index], fg="white", bg="black", font=("Helvetica", 30)
)
question.pack()

# Adicionar uma entrada de texto com texto branco e fundo preto
answer_entry = Entry(root, width=50, fg="white", bg="black", font=("Helvetica", 30))
answer_entry.pack(pady=20)
answer_entry.focus_set()  # Faz o cursor aparecer na caixa de entrada

# Variável para armazenar o tempo restante
time_left = 2400  # 40 minutos


# Função para atualizar o temporizador
def update_timer():
    global time_left
    # Se ainda houver tempo restante, diminuir o tempo e atualizar o rótulo do temporizador
    if time_left > 0:
        time_left -= 1
        minutes = time_left // 60
        seconds = time_left % 60
        timer_label.config(
            text=f"Tempo restante: {minutes} minutos e {seconds} segundos"
        )
        # Agendar a próxima atualização para daqui a 1 segundo (1000 milissegundos)
        root.after(1000, update_timer)
    # Se o tempo restante for 2399 segundos, mostrar a charada surpresa
    elif time_left == 2399:
        question.config(
            text="Charada surpresa: ..."
        )  # Substitua "..." pela charada surpresa
    else:
        messagebox.showinfo("Tempo esgotado", "O tempo acabou!")


# Adicionar um rótulo para o temporizador
timer_label = Label(
    root,
    text=f"Tempo restante: {time_left} segundos",
    fg="red",
    bg="black",
    font=("Helvetica", 59),
)
timer_label.pack()


# Variável para rastrear se a charada surpresa já foi respondida
surprise_question_answered = False


# Função para verificar a resposta
def check_answer():
    global question_index, time_left, surprise_question_answered
    # Pegar o valor da entrada de texto
    answer = answer_entry.get()
    # Verificar se a resposta é para a charada surpresa
    if (
        time_left == 2399 and not surprise_question_answered and answer == "resposta"
    ):  # Substitua "resposta" pela resposta correta para a charada surpresa
        # Marcar a charada surpresa como respondida
        surprise_question_answered = True
        # Mostrar uma mensagem de sucesso
        messagebox.showinfo(
            "Sucesso", "Você respondeu corretamente à charada surpresa!"
        )
        # Limpar a entrada de texto
        answer_entry.delete(0, "end")
    # Verificar se a resposta está correta
    elif answer == answers[question_index]:
        # Avançar para a próxima pergunta
        question_index += 1
        # Se ainda houver perguntas, mostrar a próxima pergunta
        if question_index < len(questions):
            question.config(text=questions[question_index])
            # Limpar a entrada de texto
            answer_entry.delete(0, "end")
        else:
            messagebox.showinfo("Fim", "Parabéns, você respondeu todas as perguntas!")
    else:
        # Diminuir o tempo restante em 15 segundos
        time_left -= 15
        messagebox.showinfo("Falha", "Resposta incorreta!")


# Adicionar um botão que chama a função check_answer quando clicado
check_button = Button(
    root,
    text="Verificar resposta",
    command=check_answer,
    fg="white",
    bg="black",
    font=("Helvetica", 30),
)
check_button.pack()

# Iniciar o temporizador
update_timer()

# Iniciar o loop principal
root.mainloop()
