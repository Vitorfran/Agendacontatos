import tkinter as tk
import customtkinter as ctk

# Configurações do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# funçao Add o contato
def add_contact():
    nome = nomeentry.get()  
    numero = numeroentry.get() 
    if nome and numero: 
        contato = f"{nome} - {numero}"
        lista_contatos.insert(tk.END, contato)  
        nomeentry.delete(0, tk.END)  
        numeroentry.delete(0, tk.END)  

# funçao de remover contato
def remove_contact():
    try:
        selected_index = lista_contatos.curselection() 
        if selected_index:
            lista_contatos.delete(selected_index)
    except:
        pass  # Caso não haja seleção, apenas ignora

def janela_ligar():
    janela2 = ctk.CTkToplevel(janela)
    janela2.title("Ligando..")
    janela2.geometry("500x900")
    janela2.mainloop()

# Crie a janela principal
janela = ctk.CTk()
janela.title("Agenda de Contatos")
janela.geometry("500x900")

# Adicione widgets
label = ctk.CTkLabel(janela, text="Bem Vindo(a) a Agenda de Contatos!")
label.pack(padx=10, pady=10)

textoadd = ctk.CTkLabel(janela, text="Adicione um novo contato:")
textoadd.pack(padx=10, pady=5)

# Adicione a lista de contatos usando o Listbox do Tkinter
nomeentry = ctk.CTkEntry(janela, placeholder_text="Digite o nome")
nomeentry.pack(padx=10, pady=5)

numeroentry = ctk.CTkEntry(janela, placeholder_text="Digite o número")
numeroentry.pack(padx=10, pady=5)

lista_contatos = tk.Listbox(janela)
lista_contatos.pack(padx=10, pady=10, fill='both', expand=True)

# Adicione o botão de adicionar contato
botao = ctk.CTkButton(janela, text='Adicionar', command=add_contact)
botao.pack(padx=10, pady=5)

# Adicione o botão de remover contato
botaorem = ctk.CTkButton(janela, text='Remover', command=remove_contact)
botaorem.pack(padx=10, pady=5)

# Adicione o botão de ligar
bntligar = ctk.CTkButton(janela, text='Ligar', command=janela_ligar)
bntligar.pack(padx=10, pady=5)


# Inicie o loop de eventos
janela.mainloop()

print("Obrigado por usar a Agenda de Contatos!")