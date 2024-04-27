import tkinter as tk
import webbrowser

class SitesAgregados:
    def __init__(self, root):
        self.root = root
        self.root.title('Sites Agregados')
        self.root.configure(bg='#f0f0f0')  # Cor de fundo suave

        # Criar os botões para cada site
        sites = [
            ('Google', 'https://www.google.com/', '#4CAF50'),  # Verde
            ('YouTube', 'https://www.youtube.com/', '#FF5722'),  # Laranja
            ('Facebook', 'https://www.facebook.com/', '#3B5998'),  # Azul
            ('WhatsApp', 'https://web.whatsapp.com/', '#009688'),  # Verde água
            ('Instagram', 'https://www.instagram.com/', '#C13584'),  # Rosa
            ('Globo', 'https://www.globo.com/', '#333333'),  # Cinza escuro
            ('Mercado Livre', 'https://www.mercadolivre.com.br/', '#F79F1F'),  # Amarelo
            ('UOL', 'https://www.uol.com.br/', '#551A8B'),  # Roxo
            ('Netflix', 'https://www.netflix.com/', '#E50914'),  # Vermelho
            ('Banco do Brasil', 'https://www.bb.com.br/', '#00154F'),  # Azul escuro
            ('Caixa', 'https://www.caixa.gov.br/', '#0099CC'),  # Azul claro
            ('Bradesco', 'https://www.bradesco.com.br/', '#F04D22')  # Laranja escuro
        ]

        for i, (nome, url, cor) in enumerate(sites):
            button = tk.Button(self.root, text=nome, command=lambda u=url: self.open_site(u), bg=cor, fg='white', font=('Arial', 12, 'bold'), width=20, height=2, cursor='hand2')
            button.grid(row=i//4, column=i%4, padx=10, pady=5, sticky='nsew')

    def open_site(self, url):
        webbrowser.open(url)

# Criar a janela principal
root = tk.Tk()
app = SitesAgregados(root)
root.mainloop()
