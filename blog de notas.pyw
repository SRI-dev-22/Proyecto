from tkinter import Tk,Label,Button,Entry,Frame,messagebox, Radiobutton,Text,Scrollbar,IntVar

class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=900, height=900)
        self.master = master
        self.pack()
        self.widgets()
    def noexiste(self):
        pass
    def widgets(self):
        menu=Frame(self,width=900, height=30,bg="blue")
        menu.place(x=0,y=0)
        self.btnarchivo=Button(menu,text="Archivo",command=self.noexiste,fg="green")
        self.btnarchivo.place(x=10,y=0)
        

        p_aux = Frame(self)
        p_aux.place(x=30,y=30)

        scroll = Scrollbar(p_aux)
        scroll.pack(side='right', fill='y')

        self.txtRes=Text(p_aux, width=100, height=30, yscrollcommand=scroll.set)
        self.txtRes.pack(side="left")

        scroll.config(command= self.txtRes.yview)

      

    
root = Tk()
root.wm_title("Mi blog de Notas(Rewrite)")
app = MainFrame(root)
app.mainloop()