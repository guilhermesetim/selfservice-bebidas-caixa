from tela import Tela
import PySimpleGUI as sg

class Cadastro(Tela):
    def __init__(self, id, cursor, bancoDados):      

        # atributos
        self.id = id
        self.cursor = cursor
        self.bancoDados = bancoDados

        # métodos
        self.telaInterativa()

        self.nome = self.values['nome']
        self.gravarBancoDados(self.nome)
        self.enviarArduino(self.nome)
        


    def telaInterativa(self):
        # layout
        figma = [
            [sg.Text('Id:', size=(7,0)), sg.Text(self.id)],
            [sg.Text('Nome:', size=(7,0)), sg.Input(size=(16,0), key='nome')],
            [sg.Button('  Cadastrar  ')]
        ]

        # janela        
        self.janelaCadastro = sg.Window("Cadastro do usuário").layout(figma)

        # extrair dados
        self.button, self.values = self.janelaCadastro.Read()


    def gravarBancoDados(self, nome):
        self.cursor.execute(f"INSERT INTO clientes (id, nome) values ('{self.id}', '{nome}')" )
        self.bancoDados.commit()
        self.sucesso()


    def enviarArduino(self, nome):
        print(nome)
    

    def sucesso(self):
        # layout
        figma = [ [sg.Text('\n\nCliente cadastrado com sucesso', size=(30,5) )] ]

        # janela        
        self.janelaCadastro = sg.Window("Cadastro do usuário").layout(figma)

        # extrair dados
        self.values = self.janelaCadastro.Read()

    def fechar(self):
        self.janelaCadastro.close()
