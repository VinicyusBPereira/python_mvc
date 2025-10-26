from views.view import View
from models.model import Model

class Controller:
    def __init__(self, root):    
        print(" 8-controller")
        self.view = View(root, self)
        self.model = Model(self)

    # CORRETO: Agora é um método da classe Controller
    def handle_salvar_aluno(self):
        print(" (controller) Botão 'Entrar' clicado. Coletando dados...")

        # 1. Pega os dados das caixas de texto da View
        nome = self.view.caixa_nome.get()
        data = self.view.caixa_data.get()
        ra = self.view.caixa_ra.get()
        curso = self.view.caixa_curso.get()
        
        # 2. Envia os dados para o Model salvar
        mensagem_retorno = self.model.salvar_aluno(nome, data, ra, curso)
        
        # 3. Atualiza o label na View com a resposta do Model
        self.view.label_mensagem.config(text=mensagem_retorno)
        
        # 4. (Opcional) Limpa os campos após salvar
        self.view.caixa_nome.delete(0, 'end')
        self.view.caixa_data.delete(0, 'end')
        self.view.caixa_ra.delete(0, 'end')
        self.view.caixa_curso.delete(0, 'end')
        print(" (controller) Dados enviados, label atualizado e campos limpos.")

    # CORRETO: Método alinhado com __init__
    def acao_botao_1(self):    
        print(" 9-controlller")     
        x = self.model.acessar_bd("Botão 1 acionado")
        self.view.label_mensagem.config(text=x) 

    # CORRETO: Método alinhado com __init__
    def acao_botao_2(self):    
        print(" 10-controller")     
        self.view.label_mensagem.config(text=self.model.acessar_bd("Botão 2 acionado"))