P=float(input('Posimni kiriting P='))
M=float(input('Mollyar massani kiriting M='))
T=float(input('Temperaturani kiriting T='))
r=float(input('Molekula radiusini kiriting r='))
a=float(input('a tuzatmani kiriting a='))
b=float(input('b tuzatmani kiriting b='))
i=float(input('Erkinlik darajasini kiriting i='))
R=8.31
ka=1.38*10**(-23)
z=3.14
ro=(P*M)/(R*T)
l=(0.057*ka*T)/(r**2*P)
D=(l/3)*((8*R*T)/(z*M))**(1/2)
chi=(i*R*D*ro)/(2*M)
eta=D*ro
gamma=(i+2)/i
V_k=3*b
p_k=a/(27*b**2)
t_k=(8*a)/(27*R*b)

from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 45, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=420, y=40)# javob chiqadigan raqam parametri

        btns = [
            "ZICHLIGI", "ERKIN YUGURISH YOLI", "DIFFUZIYA KOEFFITSIENTI", "ISSIQLIK O'TKAZUVCHANLIGI",
            "QOUSHOQLIK KOEFFITSIENTI", "VAN-DER-VAALS TUZATMASI(a)", "VAN-DER-VAALS TUZATMASI(b)", "POLEOTROPIYA KO'RSATGICHI",
            "PUASSON KOEFFITSIENTI", "KRITIK HAJM", "KRITIK BOSIM", "KRITIK TEMPERATURA",
            
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=400,
                                      height=79)
            x += 400
            if x > 1200:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "ZICHLIGI":
            self.formula = ro,"kg/m^3" 
        elif operation == "ERKIN YUGURISH YOLI":
            self.formula = l,"m"
        elif operation == "DIFFUZIYA KOEFFITSIENTI":
            self.formula = D
        elif operation == "ISSIQLIK O'TKAZUVCHANLIGI":
            self.formula = chi
        elif operation == "QOUSHOQLIK KOEFFITSIENTI":
            self.formula = eta
        elif operation == "VAN-DER-VAALS TUZATMASI(a)":
            self.formula = a
        elif operation == "VAN-DER-VAALS TUZATMASI(b)":
            self.formula = b
        elif operation == "POLEOTROPIYA KO'RSATGICHI":
            self.formula = "0,1,cheksiz",gamma
        elif operation == "PUASSON KOEFFITSIENTI":
            self.formula = gamma
        elif operation == "KRITIK HAJM":
            self.formula = V_k,"m^3"
        elif operation == "KRITIK BOSIM":
            self.formula = p_k,"Pa"
        elif operation == "KRITIK TEMPERATURA":
            self.formula = t_k,"K"
            
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("1200x500+200+200")
    root.title("Modda parametrlarini topuvchi dastur")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
