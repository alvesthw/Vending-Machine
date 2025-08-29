from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class VendingMachine:
    def __init__(self, message_label, transition_label):
        self.state = 0
        self.message_label = message_label
        self.transition_label = transition_label

    def insert_coin(self, coin):
        if coin not in [5, 10, 25]:
            self.message_label.config(text="Moeda inválida! Use 5, 10 ou 25 centavos.")
            return

        previous_state = self.state
        self.state += coin

        # Atualiza apenas a label de transição
        self.transition_label.config(
            text=f"Transição: {previous_state}c → {self.state}c (inserido {coin}c)"
        )

        if self.state >= 30:
            self.message_label.config(
                text=f"Produto liberado com {self.state}c!"
            )
            self.state = 0
        else:
            self.message_label.config(text="Mais moedas, por favor.")

# Criando a interface
root = Tk()
root.title("Vending Machine")
root.geometry("500x660")  # Ajuste o tamanho conforme a imagem
root.resizable(False, False)  # Impede que a janela seja redimensionada

# Carregar e configurar imagem de fundo
imagem_fundo = Image.open("./images/maquina_vendas.png")

largura_original, altura_original = imagem_fundo.size

# Fator de escala desejado (ex: 0.5 = 50% do tamanho)
escala = 0.7

# Calcular nova largura e altura proporcional
nova_largura = int(largura_original * escala)
nova_altura = int(altura_original * escala)

# Redimensionar proporcionalmente
imagem_fundo = imagem_fundo.resize((nova_largura, nova_altura))
bg = ImageTk.PhotoImage(imagem_fundo)

# Criar label para imagem de fundo
fundo_label = Label(root, image=bg)
fundo_label.place(x=0, y=0, relwidth=1, relheight=1)  # Preencher a janela inteira

# Criar Frame sobre a imagem de fundo
frm = ttk.Frame(root, padding=5)
frm.place(x=380, y=200)  # Centralizado

# Label para mensagens principais
message_label = ttk.Label(frm, text="Insira uma moeda:", font=("Arial", 8), width=15)
message_label.grid(column=0, row=0, columnspan=3, pady=10)

# Label para mostrar transições
transition_label = ttk.Label(root, text="", font=("Arial", 10), foreground="gray", width=49, wraplength=200)
transition_label.place(x=33, y=36) 

# Criar instância da máquina com as duas labels
vm = VendingMachine(message_label, transition_label)

# Botões para as moedas
btn_5 = ttk.Button(frm, text="$0,05", command=lambda: vm.insert_coin(5))
btn_10 = ttk.Button(frm, text="$0,1", command=lambda: vm.insert_coin(10))
btn_25 = ttk.Button(frm, text="$0,25", command=lambda: vm.insert_coin(25))

btn_5.grid(column=0, row=2, padx=2, pady=5)
btn_10.grid(column=0, row=3, padx=5, pady=5)
btn_25.grid(column=0, row=4, padx=5, pady=5)

# Botão para sair
exit_button = ttk.Button(frm, text="Sair", command=root.destroy)
exit_button.grid(column=0, row=5, pady=5)

root.mainloop()
