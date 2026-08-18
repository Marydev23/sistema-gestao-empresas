import tkinter as tk
from empresasDAO import EmpresasDAO
from tela import MinhaTela

if __name__ == '__main__':
    janela = tk.Tk()
     

    DAO = EmpresasDAO()
    minha_tela = MinhaTela(janela, DAO)
    janela.mainloop()




  


    