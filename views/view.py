import tkinter as tk
from tkinter import ttk

class View:
    def __init__(self, root, controller):
        print("    11-view")
        self.janela = root
        self.controlador = controller
        self.janela.geometry("400x400")
        self.janela.title("Meu Programinha MVC")

        self.style = ttk.Style()
        self.style.configure('Cinza.TFrame', background='#4F4F4F')
        self.style.configure('BrancoTexto.TLabel', background='#4F4F4F', foreground='white')

        self._criar_frame_topo()
        self._criar_frame_meio()
        self._criar_frame_baixo()

    def _criar_frame_topo(self):
        print("    12-view")
        self.frame_topo = ttk.Frame(self.janela, height=50, style='Cinza.TFrame')
        self.frame_topo.pack(fill="x", padx=1, pady=1)
        self.frame_topo.pack_propagate(False)
        
        self.label_titulo = ttk.Label(
            self.frame_topo,
            text="Cadastro de Alunos", # Tirei o (Exemplo)
            font=("Helvetica", 16, "bold"),
            style='BrancoTexto.TLabel'
        )
        self.label_titulo.place(x=20, y=10)

    def _criar_frame_meio(self):
        print("    13-view")
        self.frame_meio = ttk.Frame(self.janela)
        self.frame_meio.pack(padx=1, pady=1, fill="both", expand=True)
        
        # --- Formulário de Cadastro ---
        
        # Campo Nome
        self.label_nome = ttk.Label(self.frame_meio, text="Nome:")
        self.label_nome.place(x=20, y=20)
        self.caixa_nome = ttk.Entry(self.frame_meio, width=40)
        self.caixa_nome.place(x=150, y=20)

        # Campo Data de Nascimento
        self.label_data = ttk.Label(self.frame_meio, text="Data Nascimento:")
        self.label_data.place(x=20, y=60)
        self.caixa_data = ttk.Entry(self.frame_meio, width=40)
        self.caixa_data.place(x=150, y=60)

        # Campo RA
        self.label_ra = ttk.Label(self.frame_meio, text="RA:")
        self.label_ra.place(x=20, y=100)
        self.caixa_ra = ttk.Entry(self.frame_meio, width=40)
        self.caixa_ra.place(x=150, y=100)

        # Campo Curso
        self.label_curso = ttk.Label(self.frame_meio, text="Curso:")
        self.label_curso.place(x=20, y=140)
        self.caixa_curso = ttk.Entry(self.frame_meio, width=40)
        self.caixa_curso.place(x=150, y=140)
        
        # Botão Entrar
        self.botao_entrar = ttk.Button(
            self.frame_meio, 
            text="Entrar", 
            command=self.controlador.handle_salvar_aluno # Liga no controller
        )
        self.botao_entrar.place(x=150, y=180)

        # Label de Mensagem
        self.label_mensagem = ttk.Label(self.frame_meio, text="...aguardando ação...")
        self.label_mensagem.place(x=20, y=230)

    def _criar_frame_baixo(self):
        print("    14-view")
        self.frame_baixo = ttk.Frame(self.janela, height=50, style='Cinza.TFrame')
        self.frame_baixo.pack(fill="x", padx=1, pady=1, side="bottom")
        self.frame_baixo.pack_propagate(False)
      
        self.botao_salvar_exemplo = ttk.Button(
            self.frame_baixo, 
            text="Salvar (Exemplo)", 
            command=self.controlador.acao_botao_1
        ) 
        self.botao_salvar_exemplo.place(x=20, y=10)
        
        self.botao_buscar_exemplo = ttk.Button(
            self.frame_baixo, 
            text="Buscar (Exemplo)", 
            command=self.controlador.acao_botao_2
        ) 
        self.botao_buscar_exemplo.place(x=150, y=10)
