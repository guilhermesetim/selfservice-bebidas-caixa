def tratamentoDadosbd(string):
    # retira o inicio
    string = string.replace("b'","")
    # retira o final
    tirar = string.find('\\')
    string = string[:tirar]
    # divide para separar na lista
    stringDividida = string.split('|')

    return stringDividida


