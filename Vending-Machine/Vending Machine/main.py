from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class VendingMachine:
    def __init__(self, message_label, canvas, state_circles, product_label, product_img):
        self.state = 0
        self.message_label = message_label
        self.canvas = canvas
        self.state_circles = state_circles
        self.product_label = product_label   # Label onde o produto vai aparecer
        self.product_img = product_img       # Imagem do produto

        self.highlight_state(0)  # Estado inicial

    def highlight_state(self, value):
        """Destaca o círculo do estado atual"""
        for v, circle in self.state_circles.items():
            self.canvas.itemconfig(circle, fill="white")
        if value in self.state_circles:
            self.canvas.itemconfig(self.state_circles[value], fill="lightgreen")
    
    def insert_coin(self, coin):
        if coin not in [5, 10, 25]:
            self.message_label.config(text="Moeda inválida! Use 5, 10 ou 25 centavos.")
            return

        self.state += coin

        if self.state >= 30:
            self.state = 30
            self.message_label.config(text=f"Produto liberado com {self.state}c!")

            start_x = 250
            start_y = 300
            end_y = 590
            step = 5

            self.product_label.config(image=self.product_img, bg=root["bg"])
            self.product_label.place(x=start_x, y=start_y)

            def animate(y=start_y):
                if y < end_y:
                    self.product_label.place(x=start_x, y=y)
                    self.product_label.after(20, lambda: animate(y + step))
                else:
                    self.product_label.after(500, lambda: self.product_label.config(image=""))

                    # Pergunta se o usuário quer pedir outro produto
                    resposta = messagebox.askyesno("Continuar?", "Deseja pedir outro produto?")
                    if resposta:
                        self.state = 0  # Zera o estado
                        self.highlight_state(self.state)
                        self.message_label.config(text="Insira uma moeda:")
                    else:
                        root.destroy()  # Fecha a aplicação

            animate()
        else:
            self.message_label.config(text="Mais moedas, por favor.")

        self.highlight_state(self.state)



# Criando a interface
root = Tk()
root.title("Vending Machine")
root.geometry("600x700")
root.resizable(False, False)

# Carregar imagem de fundo
imagem_fundo = Image.open("./images/maquina_vendas.png")
escala = 0.7
imagem_fundo = imagem_fundo.resize((int(imagem_fundo.width * escala), int(imagem_fundo.height * escala)))
bg = ImageTk.PhotoImage(imagem_fundo)

fundo_label = Label(root, image=bg)
fundo_label.place(x=-60, y=30, relwidth=1, relheight=1)

# Frame de controles
frm = ttk.Frame(root, padding=5)
frm.place(x=420, y=250)

message_label = ttk.Label(frm, text="Insira uma moeda:", font=("Arial", 8), width=50)
message_label.grid(column=0, row=0, columnspan=3, pady=10)

# Canvas de estados
canvas = Canvas(root, width=345, height=60, bg="white")
canvas.place(x=65, y=10)

altura = 30
states = [0, 5, 10, 15, 20, 25]
espacamento = canvas.winfo_reqwidth() // (len(states) + 1)

state_positions = {value: ((i+1) * espacamento, altura) for i, value in enumerate(states)}

state_circles = {}
for value, (x, y) in state_positions.items():
    circle = canvas.create_oval(x-15, y-15, x+15, y+15, fill="white", outline="black")
    canvas.create_text(x, y, text=f"{value}c")
    state_circles[value] = circle
    
# Carregar imagem do produto (ex.: refrigerante)
product_img = Image.open("./images/refri.png")
product_img = product_img.resize((40, 100))  # menor que antes

# Girar a imagem de lado (90 graus no sentido horário)
product_img = product_img.rotate(90, expand=True)

# Converter para Tkinter
product_img = ImageTk.PhotoImage(product_img)

product_label = Label(root, bg=root["bg"])


# Criar máquina de vendas
vm = VendingMachine(message_label, canvas, state_circles, product_label, product_img)

# Botões
btn_5 = ttk.Button(frm, text="5c", command=lambda: vm.insert_coin(5))
btn_10 = ttk.Button(frm, text="10c", command=lambda: vm.insert_coin(10))
btn_25 = ttk.Button(frm, text="25c", command=lambda: vm.insert_coin(25))

btn_5.grid(column=0, row=2, padx=2, pady=5)
btn_10.grid(column=0, row=3, padx=5, pady=5)
btn_25.grid(column=0, row=4, padx=5, pady=5)

exit_button = ttk.Button(frm, text="Sair", command=root.destroy)
exit_button.grid(column=0, row=5, pady=5)

root.mainloop()
