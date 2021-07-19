import os
from tkinter import Label, Tk

janela = Tk()
janela.title('Teste de Ping')
janela.geometry('600x400')

rt = Label(janela, font =("Arial", 15))
rt.grid(column = 0, row = 0)

with open("c:\\teste_ping\\lista_ip.txt") as file:
    dump = file.read()
    dump = dump.splitlines()
    print(dump)

for ip in dump:
    res = os.popen(f'ping {ip}').read()
    if ("Esgotado o tempo limite do pedido.") in res:

        f = open("c:\\teste_ping\\saida_teste.txt", "a")
        f.write(str(ip) + ' - Desativado ' + "\n")
        f.close()
    else:

        f = open("c:\\teste_ping\\saida_teste.txt", "a")
        f.write(str(ip) + ' - Funcionando ' + "\n")
        f.close()

with open("c:\\teste_ping\\saida_teste.txt") as file:
    saida = file.read()


rt.configure(text=saida)

with open("c:\\teste_ping\\saida_teste.txt", "w") as file:
    pass

janela.mainloop()