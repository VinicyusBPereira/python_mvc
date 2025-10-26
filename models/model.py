import sqlite3 # Importa a biblioteca do SQLite

class Model:
    def __init__(self, controller):
        self.controller = controller
        print("  6-model")
        
        # Conecta ao banco de dados (ou cria se não existir)
        self.conexao = sqlite3.connect('alunos.db')
        
        # Chama a função para criar a tabela
        self._criar_tabela()

    def _criar_tabela(self):
        print("  7-model (verificando/criando tabela)")
        try:
            cursor = self.conexao.cursor()
            # SQL para criar a tabela, SÓ SE ELA NÃO EXISTIR
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                data_nascimento TEXT,
                ra TEXT,
                curso TEXT
            )
            """)
            self.conexao.commit()
            print("   Tabela 'alunos' pronta.")
        except sqlite3.Error as e:
            print(f"   Erro ao criar tabela: {e}")

    def salvar_aluno(self, nome, data, ra, curso):
        print("  (model) recebendo dados para salvar...")
        try:
            cursor = self.conexao.cursor()
            # SQL para inserir os dados
            cursor.execute("""
            INSERT INTO alunos (nome, data_nascimento, ra, curso) 
            VALUES (?, ?, ?, ?)
            """, (nome, data, ra, curso))
            
            self.conexao.commit()
            print("   Aluno salvo no banco de dados!")
            return "Aluno salvo com sucesso!" # Mensagem de sucesso
            
        except sqlite3.Error as e:
            print(f"   Erro ao inserir aluno: {e}")
            return f"Erro ao salvar: {e}" # Mensagem de erro

    # Função antiga (só para o botão 2 não dar erro)
    def acessar_bd(self, acao: str):
        print("  (model) 'acessar_bd' de exemplo chamado")
        return "Consultei o BD! vindo de '"+acao+"'"    