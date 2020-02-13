             ###################################################
             #                Joao Carlos Lopes                #
             #                   Num: 90732                    #
             #                   1º projeto                    #
             ###################################################

################################ Gramatica #####################################
def e_artigo_def(arg):
    grammar = ("A", "O")
    return arg in grammar

def e_vogal_palavra(arg):
    grammar = ("E",)
    return e_artigo_def(arg) or arg in grammar

def e_vogal(arg):
    grammar = ("I", "U")
    return arg in grammar or e_vogal_palavra(arg)

def e_ditongo_palavra(arg):
    grammar = ("AI", "AO", "EU", "OU")
    return arg in grammar

def e_ditongo(arg):
    grammar = ("AE", "AU", "EI", "OE", "OI", "IU")
    return arg in grammar or e_ditongo_palavra(arg)

def e_par_vogais(arg):
    grammar = ("IA", "IO")
    return e_ditongo(arg) or arg in grammar

def e_consoante_freq(arg):
    grammar = ("D", "L", "M", "N", "P", "R", "S", "T", "V")
    return arg in grammar

def e_consoante_terminal(arg):
    grammar = ("L", "M", "R", "S", "X", "Z")
    return arg in grammar

def e_consoante_final(arg):
    grammar = ("N", "P")
    return arg in grammar or e_consoante_terminal(arg)

def e_consoante(arg):
    grammar = ("B", "C", "D", "F", "G", "H", "J", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Z")
    return arg in grammar

def e_par_consoantes(arg):
    grammar = ("BR", "CR", "FR", "GR", "PR", "TR", "VR", "BL", "CL", "FL", "GL", "PL")
    return arg in grammar

def e_monossilabo_2(arg):
    grammar = ("AR", "IR", "EM", "UM")
    return arg in grammar or (e_vogal_palavra(arg[0]) and arg[1] == "S") or e_ditongo_palavra(arg) or (e_consoante_freq(arg[0]) and e_vogal(arg[1]))

def e_monossilabo_3(arg):
    return (e_consoante(arg[0]) and e_vogal(arg[1]) and e_consoante_terminal(arg[2])) or (e_consoante(arg[0]) and e_ditongo(arg[1:])) or (e_par_vogais(arg[:2]) and e_consoante_terminal(arg[2]))

def e_silaba_2(arg):
    return e_par_vogais(arg) or (e_consoante(arg[0]) and e_vogal(arg[1])) or (e_vogal(arg[0]) and e_consoante_final(arg[1]))

def e_silaba_3(arg):
    grammar = ("QUA", "QUI", "GUE", "GUI", "QUE")
    return arg in grammar or (e_vogal(arg[0]) and arg[1:] == "NS") or (e_consoante(arg[0]) and e_par_vogais(arg[1:])) or (e_consoante(arg[0]) and e_vogal(arg[1]) and e_consoante_final(arg[2])) or (e_par_vogais(arg[:2]) and e_consoante_final(arg[2])) or (e_par_consoantes(arg[:2]) and e_vogal(arg[2]))

def e_silaba_4(arg):
    return (e_par_vogais(arg[:2]) and arg[2:] == "NS") or (e_consoante(arg[0]) and e_vogal(arg[1]) and arg[2:] == "IS") or (e_consoante(arg[0]) and e_vogal(arg[1]) and arg[2:] == "NS") or (e_par_consoantes(arg[:2]) and e_par_vogais(arg[2:])) or (e_consoante(arg[0]) and e_par_vogais(arg[1:3]) and e_consoante_final(arg[3]))

def e_silaba_5(arg):
    return e_par_consoantes(arg[:2]) and e_vogal(arg[2]) and arg[3:] == "NS"

def e_silaba_final(arg):
    arg_len = len(arg)

    if arg_len == 2:
        return e_monossilabo_2(arg)
    elif arg_len == 3:
        return e_monossilabo_3(arg)
    elif arg_len == 4:
        return e_silaba_4(arg)
    else:
        return e_silaba_5(arg)

###############################e_monossilabo()##################################
def e_monossilabo(arg):
    if not isinstance(arg, str):
        raise ValueError("e_monossilabo:argumento invalido")
    arg_len = len(arg)

    if arg_len == 1:
        return e_vogal_palavra(arg)
    elif arg_len == 2:
        return e_monossilabo_2(arg)
    elif arg_len == 3:
        return e_monossilabo_3(arg)
    return False
###############################e_silaba()#######################################
def e_silaba(arg):
    if not isinstance(arg, str):
        raise ValueError("e_silaba:argumento invalido")
    arg_len = len(arg)

    if arg_len == 1:
        return e_vogal(arg)
    elif arg_len == 2:
        return e_silaba_2(arg)
    elif arg_len == 3:
        return e_silaba_3(arg)
    elif arg_len == 4:
        return e_silaba_4(arg)
    elif arg_len == 5:
        return e_silaba_5(arg)
    return False
###############################e_palavra()######################################
def e_palavra(arg):
    if not isinstance(arg, str):
        raise ValueError("e_palavra:argumento invalido")

    ###########################auxiliar_palavra()###############################
    def auxiliar_palavra(arg):
        if e_silaba_final(arg):
            return True
        for i in range(1, 6):  #So e necessario verificar se e silaba para strings com tamanhos menores que 6 e maiores que 0
            if e_silaba(arg[:i]):
                if auxiliar_palavra(arg[i:]):
                    return True
            elif i == 5:       #Se chegar ao maximo tamanho de uma silaba(5) sem encontrar uma, entao nao e palavra
                 return False

    return e_monossilabo(arg) or auxiliar_palavra(arg)
