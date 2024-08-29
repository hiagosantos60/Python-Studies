import PySimpleGUI as sg
from banco_de_dados import conectar, add_produto, remove_produto, encerra_conexao

layout = [
    [sg.Text('Nome do Produto')],
    [sg.Input(default_text='', key='-nome-', size=(50, 1))],
    [sg.Text('Código do Produto')],
    [sg.Input(default_text='', key='-lote-', size=(50, 1))],
    [sg.Text('Data de Saída')],
    [sg.Column([
        [sg.Input(key='-data-', size=(35, 1)), sg.CalendarButton('Escolher Data', target='-data-', format='%d-%m-%Y', key='-cal-')]
    ], pad=(0, 0))],
    [sg.Text('Descrição do Produto')],
    [sg.Multiline(default_text='', key='-descricao-', size=(50, 5))],
    [sg.Push(), sg.Button('Apagar'), sg.Button('Adicionar'), sg.Button('Remover'), sg.Push()]
]

window = sg.Window('Cadastro de Produtos', layout, resizable=True)

conn = conectar()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    
    elif event == 'Adicionar':
        produto_nome = values['-nome-']
        lote_codigo = values['-lote-']
        data_selecionada = values['-data-']
        descricao_produto = values['-descricao-']

        
        if conn:
            if produto_nome and lote_codigo:
                if data_selecionada: 
                    add_produto(conn, produto_nome, lote_codigo, data_selecionada, descricao_produto)
                else:
                    sg.popup_error("Por favor, preencha a data de saída.")
            else:
                sg.popup_error("Por favor, preencha o nome do produto e o código do produto.")
        else:
            sg.popup_error("Não foi possível conectar ao banco de dados.")
    
    elif event == 'Remover':
        lote_codigo = values['-lote-']

        if conn:
            if lote_codigo: 
                remove_produto(conn, lote_codigo)
            else:
                sg.popup_error("Por favor, preencha o código do produto.")
        else:
            sg.popup_error("Não foi possível conectar ao banco de dados.")

    elif event == 'Apagar':
        window['-nome-'].update('')
        window['-lote-'].update('')
        window['-data-'].update('')
        window['-descricao-'].update('')

encerra_conexao(conn)

window.close()
