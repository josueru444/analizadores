
import os
import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk
from ply import *
import time


root = tk.Tk()
root.geometry("1000x700")
root.title('Negativo')
root.resizable(height=False, width=False)
style = ttk.Style(root)
root.tk.call('source', 'azure2/azure.tcl')
root.tk.call("set_theme", "light")

comp1 = tk.PhotoImage(file='images/comp1.png')
comp2 = tk.PhotoImage(file='images/comp2.png')
lim1 = tk.PhotoImage(file='images/limp1.png')
lim2 = tk.PhotoImage(file='images/limp2.png')


fameTexto=Frame(root,width=700,height=650,bg='white')
frameBotones=Frame(root,width=1000,height=50,bg='#304ffe')
frameError=Frame(root,width=1000,height=200,background='red')
frametabla=Frame(root,width=300,height=650,background='pink')
compilarbtn=Label(image=comp1,background='#304ffe' )
limpiarbtn=Label(image=lim1,background='#304ffe')
entry=Text(fameTexto,background='#eceff1',fg='black')
entryErrores=ScrolledText(frameError,background='#eceff1',fg='black')
entryErrores.place(x=0,y=0,width=1000,height=200)

limpiarbtn.bind('<Button-1>',lambda e:limpiar())
limpiarbtn.bind("<Enter>", lambda e:limpiarbtn.config(image=lim2))
limpiarbtn.bind("<Leave>", lambda e:limpiarbtn.config(image=lim1))

compilarbtn.bind('<Button-1>',lambda e:compilar())
compilarbtn.bind("<Enter>", lambda e:compilarbtn.config(image=comp2))
compilarbtn.bind("<Leave>", lambda e:compilarbtn.config(image=comp1))

fameTexto.place(x=0,y=50)
compilarbtn.place(x=400,y=7)
limpiarbtn.place(x=600,y=7)

frameBotones.place(x=0,y=0)
frametabla.place(x=700,y=50)
entry.place(x=0,y=0,width=700,height=650)
# resultado del analisis

#tabla
columns = ('ID', 'TIPO','VALOR')
tabla=ttk.Treeview(frametabla,columns=columns, show='headings')

tabla.column('ID', width=10)
tabla.column('TIPO', width=10)
tabla.column('VALOR', width=10)

tabla.heading('ID', text='ID')
tabla.heading('TIPO', text='Tipo')
tabla.heading('VALOR', text='Valor')


tabla.place(x=0,y=0,width=300,height=650)
identificadores=[]

def normal():
    frameError.place_forget()
    entry.place_forget()
    fameTexto.config(height=650)
    entry.place(x=0,y=0,width=700,height=650)
    frametabla.config(height=650)
    tabla.place(x=0,y=0,width=300,height=650)



def compilar():
    identificadores.clear()
    a=time.strftime("%H-%M-%S")
    tex=entry.get('0.0',END).split('\n')
    tabla.delete(*tabla.get_children())
    resultado_lexema2.clear()
    file = open(("archivos/archivo.txt"), "w")

    for w in tex:
        prueba(w)
        if len(resultado_lexema2)>0:
            errores()
        else:
            normal()


            # add data to the treeview
    for tip in identificadores:

        tabla.insert('', tk.END, values=tip)

    for lexs in lexema:
        file.write(lexs+"\n")
        print(lexs)
    text= "".join(tex)
    prueba_sintatico(text)
    
    file.close()
    tipo.clear()


def errores():
    entryErrores.delete('0.0',END)
    entryErrores.insert(END,'---------------ERRORES:----------------------------------------------------------\n')
    for i in (resultado_lexema2):
        entryErrores.insert(END,(i+'\n'))
    entry.place_forget()
    fameTexto.config(height=450)
    entry.place(x=0,y=0,width=700,height=450)
    frametabla.config(height=450)
    frameError.place(x=0,y=500)

def limpiar():
    entry.delete('0.0',END)
    entryErrores.delete('0.0',END)
    identificadores.clear()
'''------------------------------------------------------------------LEXICO------------------------------------------------------------------'''
resultado_lexema = []
resultado_lexema2 = []
tipo=[]
lexema=[]
reservada = (
    # Palabras Reservadas
    'START',
    'END',
    'INTEGER',
    'DECIMAL',
    'READ',
    'PRINT',
    'ADD',
    'SUB',
    'MUL',
    'DIV',
)
tokens = reservada + (
    'IDENTIFICADOR',
    'IDENTIFICADORREAL',
    'IDENTIFICADORENTERO',
    'LLAVEINICIO',
    'LLAVEFIN',
    'PARENTESISINICIO',
    'PARENTESISFIN',
    'PUNTOCOMA',
    'COMA',
    'IGUAL'
)

> Javier:
# Reglas de Expresiones Regualres para token de Contexto simple

t_PUNTOCOMA = '\;'
t_COMA = r'\,'
t_PARENTESISINICIO = r'\('
t_PARENTESISFIN = r'\)'
t_LLAVEINICIO = r'{'
t_LLAVEFIN = r'}'
t_IGUAL = r'\='


def t_START(t):
    r'START+(\d|\w)*'
    if len(t.value) == 5:
        return t
    else:
        t_error(t)


def t_END(t):
    r'END+(\d|\w)*'
    if len(t.value) == 3:
        return t
    else:
        t_error(t)


def t_INTEGER(t):
    r'INTEGER+(\d|\w)*'
    if len(t.value)==7:return t
    else:t_error(t)


def t_DECIMAL(t):
    r'DECIMAL+(\d|\w)*'
    if len(t.value) == 7:
        return t
    else:
        t_error(t)


def t_READ(t):
    r'READ+(\d|\w)*'
    if len(t.value) == 4:
        return t
    else:
        t_error(t)


def t_PRINT(t):
    r'PRINT+(\d|\w)*'
    if len(t.value) == 5:
        return t
    else:
        t_error(t)


def t_ADD(t):
    r'ADD+(\d|\w)*'
    if len(t.value) == 3:
        return t
    else:
        t_error(t)

def t_MUL(t):
    r'MUL+(\d|\w)*'
    if len(t.value) == 3:
        return t
    else:
        t_error(t)


def t_DIV(t):
    r'DIV+(\d|\w)*'
    if len(t.value) == 3:
        return t
    else:
        t_error(t)

def t_SUB(t):
    r'SUB+(\d|\w)*'
    if len(t.value) == 3:
        return t
    else:
        t_error(t)

def t_IDENTIFICADORREAL(t):
    r'(\d*\.+\d+\.*)+'
    if t.value.count(".")>1:t_error(t)
    else:
        b = str(t.value)
        for i in range(len(b)):
            j = i - 1
            if b[j] == ".":
                c = b[i:]
                break
        if len(c) <= 2:
            print("tamaño", len(c))
            d = b[:-(len(c) + 1)]
            if len(d) <= 5:
                return t
            else:
                t_error(t)
        else:
            t_error(t)

def t_IDENTIFICADORENTERO(t):
    r'\.*\d+'
    if t.value.count(".") > 0: t_error(t)
    else:
        t.value = int(t.value)
        a = str(t.value)
        a = list(str(a))
        if len(a)<=5:return t
        else:t_error(t)

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    b = t.value.replace("0", "")
    for n in range(9):
        m = str(n + 1)
        b = b.replace(m, "")
        #print(b+"\n"+m+"\n")
    if len(b) == 1:
        text = b
        s = re.sub("[A-Za-z]", '', text)
        if len(s) == 0:
            con = []
            for i in range(10):
                q = str(i)
                v = 0
                v = (t.value.count(q))
                if v == 1:
                    con.append(i)
                elif v > 1:
                    for k in range(v):
                        con.append(i)
                else:
                    pass
            if len(con) < 4 and len(con)>0:return t
            else:t_error(t)
        else:t_error(t)
    else:t_error(t)




def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    print(t.lexer.lineno)
    return t.lexer.lineno


def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")
    return t.lexer.lineno


def t_comments_ONELine(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 1
    print("Comentario de una linea")
    return t.lexer.lineno


t_ignore = ' \t'

def t_error(t):
    global resultado_lexema2
    global estado

    tex = entry.get('0.0', END).split('\n')
    for j in range(len(tex)):
        if t.value in tex[j]:
            error=(j + 1)
            break

    estado = "** Token no valido {:16} en la linea {:16}".format(str(t.value),str(error))

    resultado_lexema2.append(estado)
    lexema.append(estado)
    t.lexer.skip(1)


# Prueba de ingreso

def prueba(data):
    global resultado_lexema
    ids=[]
    analizador = lex.lex()
    analizador.input(data)

> Javier:
resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Token {:16} Lexema {:16}".format(str(tok.type),str(tok.value))
        if tok.type=="IDENTIFICADOR":
            if tok.value in identificadores:pass
            elif tok.value not in identificadores:identificadores.append((tok.value))
        tipo.append(("{:16}{:16}".format(str(tok.type),str(tok.value))))
        lexema.append(estado)
        print(estado)
    print(identificadores)
    return resultado_lexema


# instanciamos el analizador lexico
analizador = lex.lex()
'''------------------------------------------------------------------SINTACTICO------------------------------------------------------------------'''

resultado_gramatica = []

procedencia = (

    ('left','INTEGER','DECIMAL'),
    ('left','READ','PRINT'),
    ('left','ADD','SUB'),
    ('left','MUL','DIV'),
    ('right', 'END'),
    ('left', 'START')
)
nombres = {}

def p_Codigo(t):
    'codigo : Inicio Cuerpo Fin'
    t[0] = t[2]
    print("inicio")


def p_Inicio(t):
    'Inicio : START LLAVEINICIO'
    t[0] = t[1]

def p_Cuerpo(t):
    'Cuerpo : declaracion'
    t[0] = t[1]

def p_Cuerpo1(t): 
    'Cuerpo : declaracion operacion'
    t[0] = t[1]

def p_Cuerpo2(t):
    'Cuerpo : Cuerpo declaracion'
    t[0] = t[1]

def p_Cuerpo3(t):
    'Cuerpo : Cuerpo operacion'
    t[0] = t[1]

def p_Cuerpo4(t):
    'Cuerpo : ES'
    t[0] = t[1]

def p_Cuerpo5(t):
    'Cuerpo : Cuerpo ES'
    t[0] = t[1]

def p_Cuerpo6(t):
    'Cuerpo : declaracion ES'
    t[0] = t[1]

def p_Cuerpo7(t):    
    'Cuerpo : valor'
    t[0] = t[1]

def p_Cuerpo8(t):
    'Cuerpo : asignacion'
    t[0] = t[1]

def p_Cuerpo9(t):
    'Cuerpo : Cuerpo asignacion'
    t[0] = t[1]

def p_CuerpoEmpty(t):
    'Cuerpo : empty'
    #t[0] = Null()
    print("nulo")

def p_declaracion(t):
    'declaracion : tipo variables PUNTOCOMA'
    t[0] = t[2]

def p_declaracion1(t):
    'declaracion :  variables PUNTOCOMA'
    t[0] = t[2]

def p_Tipo(t):
    'tipo : INTEGER'
    t[0] = t[1]

def p_Tipo1(t):
    'tipo : DECIMAL'
    t[0] = t[1]

def p_Variables(t):
    'variables : IDENTIFICADOR'
    t[0] = t[1]

def p_Variables1(t):
    'variables : asignacion'
    t[0] = t[1]

def p_Variables2(t):
    'variables : variables COMA IDENTIFICADOR'
    t[0] = t[1]

def p_Variables3(t):
    'variables : variables COMA asignacion' 
    t[0] = t[2]

def p_Asignacion(t):
    'asignacion : IDENTIFICADOR IGUAL valor' 
    t[0] = t[3]

def p_Valor(t):
    'valor : IDENTIFICADORENTERO'
    t[0] = t[1]

def p_Valor1(t):
    'valor : IDENTIFICADORREAL'
    t[0] = t[1]

def p_Valor2(t):
    'valor : IDENTIFICADOR'
    t[0] = t[1]

def p_Valor3(t):
    'valor : operacion'
    t[0] = t[1]

def p_Operacion(t):
    'operacion : Operador PARENTESISINICIO valor COMA valor PARENTESISFIN'
    t[0] = t[1], t[3], t[5]
    print("operacion")

def p_Operacion1(t):
    'operacion : Operador PARENTESISINICIO valor COMA valor PARENTESISFIN PUNTOCOMA'
    t[0] = t[1], t[3], t[5]
    print("operacion")

def p_Operador(t):
    'Operador : ADD'
    t[0] = t[1]

def p_Operador1(t):
    'Operador : MUL'
    t[0] = t[1]

def p_Operador2(t):                
    'Operador : DIV'
    t[0] = t[1]

def p_Operador3(t):
    'Operador : SUB'
    t[0] = t[1]

def p_ES(t):
    'ES : Funcion PARENTESISINICIO variables PARENTESISFIN PUNTOCOMA'
    t[0] = t[1],t[3]


def p_Funcion(t):
    'Funcion : PRINT'
    t[0] = t[1]
    print("funcion print")

def p_Funcion1(t):
    'Funcion : READ'
    print("funcion read")

def p_Fin(t):
    'Fin : LLAVEFIN END'
    print("END")

def p_empty(t):
    'empty :'
    pass

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintatico de tipo {} en  el valor {} Linea {:4}".format(str(t.type), str(t.value),str(t.lineno))
        print(resultado)
    else:
        resultado = "Error sintatico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)
