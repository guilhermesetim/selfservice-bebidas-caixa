from tela import Tela
import PySimpleGUI as sg
from datetime import datetime


class Credito(Tela):
    def __init__(self, info, cursor, bancoDados):
        # atributos
        self.cod = info[0]
        self.id = info[1]
        self.nome = info[2]
        self.saldoAtual = info[3]
        self.cursor = cursor
        self.bancoDados = bancoDados

        # métodos
        self.telaInterativa()
        self.gravarBancoDados()
        

    
    def telaInterativa(self):
        # layout
        figma = [
            [sg.Text('Valor do copo', size=(15,0)), sg.Text('R$ 4,50')],
            [sg.Text('Id:', size=(15,0)), sg.Text(self.id)],
            [sg.Text('Nome:', size=(15,0)), sg.Text(self.nome)],
            [sg.Text('Quant canecas:', size=(15,0)), sg.Text(self.saldoAtual)],
            [sg.Text('Add canecas:', size=(15,0)), sg.Input(size=(5,0), key='add')],
            [sg.Button('  Adicionar  ')]
        ]

        # janela
        self.janela = sg.Window("Compra de crédito").layout(figma)

        # extrair dados
        self.button, self.values = self.janela.Read()


    def atualizarCanecas(self):
        valor = int(self.values['add']) + int(self.saldoAtual)
        return int(valor)
    
    def calculoPagar(self):
        valor = float(self.values['add']) * 4.50
        return round(float(valor),2)
    
    def gravarBancoDados(self):
        self.cursor.execute(f"UPDATE clientes SET canecas = {self.atualizarCanecas()} WHERE cod = {self.cod} " )
        self.cursor.execute(f"INSERT INTO receita (cod_cliente, data_credito, valor) values ({self.cod}, '{datetime.now()}', {self.calculoPagar()})" )

        self.bancoDados.commit()
        self.sucesso()
        
    
    def sucesso(self):
        # layout
        figma = [ [sg.Text('\n\nCrédito adicionado com sucesso', size=(30,5) )] ]

        # janela        
        self.janelaCadastro = sg.Window("Cadastro do usuário").layout(figma)

        # extrair dados
        self.values = self.janelaCadastro.Read()
    
    