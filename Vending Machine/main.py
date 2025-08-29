from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class VendingMachine:
    def __init__(self, display_label):
        self.state = 0
        self.display_label = display_label

    def insert_coin(self, coin):
        if coin not in [5, 10, 25]:
            self.display_label.config(text="Moeda inválida! Use 5, 10 ou 25 centavos.")
            return

        previous_state = self.state
        self.state += coin
        self.display_label.config(
            text=f"Transição: {previous_state}c → {self.state}c (inserido {coin}c)"
        )

        if self.state >= 30:
            self.display_label.config(text=f"Produto liberado com {self.state}c! Obrigado!")
            self.state = 0  # Reinicia para novo cliente

from tkinter import Tk, Label
from tkinter import ttk
from PIL import Image, ImageTk  # Certifique-se de ter pillow instalado

# Criando a interface
root = Tk()
root.title("Vending Machine")
root.geometry("708x1050")  # Ajuste o tamanho conforme a imagem

# Carregar e configurar imagem de fundo
imagem_fundo = Image.open("./images/maquina_vendas.png")
imagem_fundo = imagem_fundo.resize((708, 1050))  
bg = ImageTk.PhotoImage(imagem_fundo)

# Criar label para imagem de fundo
fundo_label = Label(root, image=bg)
fundo_label.place(x=0, y=0, relwidth=1, relheight=1)  # Preencher a janela inteira

# Criar Frame sobre a imagem de fundo
frm = ttk.Frame(root, padding=20)
frm.place(x=530, y=300)  # Centralizado

# Label para mostrar mensagens
message_label = ttk.Label(frm, text="Insira uma moeda:", font=("Arial", 12))
message_label.grid(column=0, row=0, columnspan=3, pady=10)

# Criar instância da máquina
vm = VendingMachine(message_label)

# Botões para as moedas
btn_5 = ttk.Button(frm, text="Inserir 5 centavos", command=lambda: vm.insert_coin(5))
btn_10 = ttk.Button(frm, text="Inserir 10 centavos", command=lambda: vm.insert_coin(10))
btn_25 = ttk.Button(frm, text="Inserir 25 centavos", command=lambda: vm.insert_coin(25))

btn_5.grid(column=0, row=1, padx=5, pady=5)
btn_10.grid(column=0, row=2, padx=5, pady=5)
btn_25.grid(column=0, row=3, padx=5, pady=5)

# Botão para sair
exit_button = ttk.Button(frm, text="Sair", command=root.destroy)
exit_button.grid(column=0, row=4, pady=5)

root.mainloop()
