from tkinter import *
from tkinter import ttk

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

# Criando a interface
root = Tk()
root.title("Vending Machine")

frm = ttk.Frame(root, padding=20)
frm.grid()

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
btn_10.grid(column=1, row=1, padx=5, pady=5)
btn_25.grid(column=2, row=1, padx=5, pady=5)

# Botão para sair
exit_button = ttk.Button(frm, text="Sair", command=root.destroy)
exit_button.grid(column=1, row=2, pady=20)

root.mainloop()
