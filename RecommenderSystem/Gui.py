import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

from PIL import Image,ImageTk
from Person import Person
from Admin import Admin
from Book import Book
from FileManager import ReadBooks,CheckLogin,write,delete,read
import DistanceManager

global Gusername
global Gpassw
Gusername=""
Gpassw=""


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo,PageThree,PageFour,PageFive,PageAdmin,PageAddBook,PageAddUser):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # image = Image.open("book.jpg")
        # photo = ImageTk.PhotoImage(image)
        # label = tk.Label(image=photo)
        # label.image = photo  # keep a reference!
        # label.place(x=0, y=0, relwidth=1, relheight=1)
        helv36 = tkfont.Font(self,family='Helvetica', size=17, weight='bold')




        label = tk.Label(self, text="Recommender System", font=helv36)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Sign In",
                            command=lambda: controller.show_frame("PageOne"),font=helv36)
        button2 = tk.Button(self, text="Sign Up",
                            command=lambda: controller.show_frame("PageTwo"),font=helv36)
        button1.config(height=1, width=7)
        button2.config(height=1, width=7)

        button1.pack()
        button2.pack()


class PageOne(tk.Frame):
    nameField=tk.Entry()
    PassField=tk.Entry()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        helv36 = tkfont.Font(self,family='Helvetica', size=17, weight='bold')

        label = tk.Label(self, text="Sign In", font=helv36)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"),font=helv36)
        button.place(x=10,y=10)
        button.config(height=1, width=7)
        nameLabel=tk.Label(self,text="Username: ",font=helv36)
        nameLabel.place(x=300,y=200)
        self.nameField= tk.Entry(self,text="Username")
        self.nameField.place(x=430, y=207)
        namePass=tk.Label(self,text="Password: ",font=helv36)
        namePass.place(x=300, y=250)
        self.PassField= tk.Entry(self,text="Password")
        self.PassField.place(x=430, y=257)


        submit = tk.Button(self, text="Sign In",
                           command=self.on_button, font=helv36)
        submit.place(x=380, y=300)
        submit.config(height=1, width=7)
        ##PageFour

    def on_button(self):

        Gusername=self.nameField.get()
        Gpassw=self.PassField.get()
        print Gusername+"here"
        if Gusername=="Admin" and Gpassw=="1111":
            self.controller.show_frame("PageAdmin")
        else:
             check=CheckLogin(Gusername,Gpassw)
             if check==True:
                write(Gusername,"logged.txt")
                self.controller.show_frame("PageFour")
             else:
                msg = tk.messagebox.showerror("Error", "Invalid Username or password")


class PageTwo(tk.Frame):
    nameField = tk.Entry()
    PassField = tk.Entry()
    unameField = tk.Entry()
    ageField = tk.Entry()
    salaryField = tk.Entry()
    v = tk.StringVar()
    v2 = tk.StringVar()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        helv36 = tkfont.Font(self,family='Helvetica', size=17, weight='bold')

        label = tk.Label(self, text="Sign Up", font=helv36)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"),font=helv36)
        button.place(x=10,y=10)
        button.config(height=1, width=7)

        unameLabel=tk.Label(self,text="Username:",font=helv36)
        unameLabel.place(x=300,y=100)
        self.unameField= tk.Entry(self,text="Username")
        self.unameField.place(x=430, y=107)

        namePass=tk.Label(self,text="Password: ",font=helv36)
        namePass.place(x=300, y=150)
        self.PassField= tk.Entry(self,text="Password")
        self.PassField.place(x=430, y=157)

        nameLabel=tk.Label(self,text="Name: ",font=helv36)
        nameLabel.place(x=300, y=200)
        self.nameField= tk.Entry(self,text="Name")
        self.nameField.place(x=430, y=207)

        ageLabel=tk.Label(self,text="Age: ",font=helv36)
        ageLabel.place(x=300, y=250)
        self.ageField= tk.Entry(self,text="Age")
        self.ageField.place(x=430, y=257)

        salaryLabel=tk.Label(self,text="Salary: ",font=helv36)
        salaryLabel.place(x=300, y=300)
        self.salaryField= tk.Entry(self,text="Salary")
        self.salaryField.place(x=430, y=307)

        self.v = tk.StringVar(self)

        GenderLabel=tk.Label(self,text="Gender: ",font=helv36)
        GenderLabel.place(x=300, y=350)

        rdMale=tk.Radiobutton(self,
                       text="Male",
                       padx=20,
                       variable=self.v,
                       value="M")
        rdMale.place(x=400,y=354)
        rdFemale=tk.Radiobutton(self,
                       text="Female",
                       padx=20,
                       variable=self.v,
                       value="F")
        rdFemale.place(x=480,y=354)

        CreditLabel=tk.Label(self,text="Do you have a credit card? ",font=helv36)
        CreditLabel.place(x=300, y=400)
        self.v2 = tk.StringVar(self)
        rdYes=tk.Radiobutton(self,
                       text="Yes",
                       padx=20,
                       variable=self.v2,
                       value="Y")
        rdYes.place(x=350,y=450)
        rdNo=tk.Radiobutton(self,
                       text="No",
                       padx=20,
                       variable=self.v2,
                       value="N")
        rdNo.place(x=430,y=450)

        submit = tk.Button(self, text="Sign Up",
                           command=self.on_button,font=helv36)
        submit.place(x=380,y=500)
        submit.config(height=1, width=7)

    def on_button(self):

                usernamee =self.unameField.get()
                password=self.PassField.get()
                name=self.nameField.get()
                age=self.ageField.get()
                salary=self.salaryField.get()
                gender=self.v.get()
                credit=self.v2.get()
                person = Person(usernamee, password, name, age, salary, gender, credit)
                person.Register(person)
                print(gender)



class PageThree(tk.Frame):
    v = tk.IntVar()
    variable = tk.StringVar()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        helv36 = tkfont.Font(self,family='Helvetica', size=17, weight='bold')
        label = tk.Label(self, text="", font=helv36)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("PageFour"),font=helv36)
        button.place(x=10,y=10)
        button.config(height=1, width=7)
        bookLabel = tk.Label(self, text="Book", font=helv36)
        bookLabel.place(x=200, y=100)




        books=ReadBooks()
        OPTIONS=[]
        for x in books:
            OPTIONS.append(str(x))




        self.variable = tk.StringVar(self)
        self.variable.set(OPTIONS[0])  # default value

        w = apply(tk.OptionMenu, (self, self.variable) +tuple(OPTIONS))
        w.place(x=300,y=100)
        self.v=tk.IntVar(self)
        rd0= tk.Radiobutton(self,
                                text="0",
                                padx=20,
                                variable=self.v,
                                value=0)
        rd0.place(x=400, y=104)


        rd1 = tk.Radiobutton(self,
                                text="1",
                                padx=20,
                                variable=self.v,
                                value=1)
        rd1.place(x=480, y=104)

        rd2 = tk.Radiobutton(self,
                                  text="2",
                                  padx=20,
                                  variable=self.v,
                                  value=2)
        rd2.place(x=560, y=104)

        rd3 = tk.Radiobutton(self,
                                  text="3",
                                  padx=20,
                                  variable=self.v,
                                  value=3)
        rd3.place(x=630, y=104)

        rd4 = tk.Radiobutton(self,
                                  text="4",
                                  padx=20,
                                  variable=self.v,
                                  value=4)
        rd4.place(x=710, y=104)

        rd5 = tk.Radiobutton(self,
                                  text="5",
                                  padx=20,
                                  variable=self.v,
                                  value=5)
        rd5.place(x=790, y=104)

        ratebutton = tk.Button(self, text="Rate",
                           command=self.on_button,font=helv36)
        ratebutton.place(x=635,y=150)
        ratebutton.config(height=1, width=7)

    def on_button(self):
        title=str(self.variable.get())
        rate=self.v.get()
        book=Book(title,rate)
        name=read("logged.txt")
        value=str(name[0])
        person=Person("","",value,0,0,' ',' ')
        person.RateBook(book,rate)



class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # image = Image.open("book.jpg")
        # photo = ImageTk.PhotoImage(image)
        # label = tk.Label(image=photo)
        # label.image = photo  # keep a reference!
        # label.place(x=0, y=0, relwidth=1, relheight=1)
        helv36 = tkfont.Font(self,family='Helvetica', size=17, weight='bold')
        button = tk.Button(self, text="Logout",
                           command=self.logout,font=helv36)
        button.place(x=890,y=10)
        button.config(height=1, width=7)

        # name=read("logged.txt")




        label = tk.Label(self, text="Welcome", font=controller.title_font)
        label.pack(side="top", pady=10)

        button1 = tk.Button(self, text="Rate Book",
                            command=lambda: controller.show_frame("PageThree"),font=helv36)
        button2 = tk.Button(self, text="Find Nearest",
                            command=lambda: controller.show_frame("PageFive"),font=helv36)
        button1.config(height=1, width=10)
        button2.config(height=1, width=10)

        button1.pack()
        button2.pack()
    def logout(self):
        delete("logged.txt")
        self.controller.show_frame("StartPage")



class PageFive(tk.Frame):
    v=tk.IntVar()
    variable=tk.StringVar()
    kField=tk.Entry()
    resultData=tk.Label()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # image = Image.open("book.jpg")
        # photo = ImageTk.PhotoImage(image)
        # label = tk.Label(image=photo)
        # label.image = photo  # keep a reference!
        # label.place(x=0, y=0, relwidth=1, relheight=1)
        helv36 = tkfont.Font(self,family='Helvetica', size=17, weight='bold')
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("PageFour"),font=helv36)
        button.place(x=10,y=10)
        button.config(height=1, width=7)


        label = tk.Label(self, text="Find Nearest", font=controller.title_font)
        label.pack(side="top", pady=10)

        crLabel = tk.Label(self, text="Criteria", font=helv36)
        crLabel.place(x=230, y=100)

        self.v = tk.IntVar(self)

        rd1 = tk.Radiobutton(self,
                             text="Personal Information",
                             padx=20,
                             variable=self.v,
                             value=1)
        rd1.place(x=360, y=104)

        rd2 = tk.Radiobutton(self,
                             text="Book",
                             padx=20,
                             variable=self.v,
                             value=2)
        rd2.place(x=520, y=104)

        methodLabel = tk.Label(self, text="Method", font=helv36)
        methodLabel.place(x=230, y=150)

        self.variable = tk.StringVar(self)
        self.variable.set("Manhatten")


        w = tk.OptionMenu(self, self.variable, "Manhatten", "Ecludian", "Cosin similarity")
        w.place(x=380,y=150)

        kLabel = tk.Label(self, text="K value", font=helv36)
        kLabel.place(x=230, y=200)
        self.kField= tk.Entry(self,text="k")
        self.kField.place(x=380, y=207)

        button = tk.Button(self, text="Find",
                           command=self.on_button,font=helv36)
        button.place(x=635,y=150)
        button.config(height=1, width=7)

        resultLabel = tk.Label(self, text="Result", font=helv36)
        resultLabel.place(x=230, y=250)



        self.resultData = tk.Label(self, text="", font=helv36)
        self.resultData.place(x=230, y=300)
        self.resultData.config(height=10, width=50)

    def on_button(self):
        result=""
        cr=int(self.v.get())
        method=self.variable.get()
        k=int(self.kField.get())
        if cr==1:

            if method=="Manhatten":
                rresult=DistanceManager.Calculate_ManhattanDistance(k,cr)

                for x in range(len(rresult)):
                    result+="Name: "+str(rresult[x][0])+"  "+"Distance: "+str(rresult[x][1]+"\n")

            if method == "Ecludian":
                rresult=DistanceManager.Calculate_EcludienDistance(k,cr)

                for x in range(len(rresult)):
                    result+="Name: "+str(rresult[x][0])+"  "+"Distance: "+str(rresult[x][1]+"\n")
            if method == "Cosin similarity":
                rresult=DistanceManager.Calculate_CousineDistance(k,cr)

                for x in range(len(rresult)):
                     result+="Name: "+str(rresult[x][0])+"  "+"Distance: "+str(rresult[x][1]+"\n")
            self.resultData.configure(text=result)


        if cr==2:

            if method=="Manhatten":
                rresult=DistanceManager.Calculate_ManhattanDistance(k,cr)
                result="Rate: "+" "+str(rresult[0])+" "+str(rresult[1])

            if method == "Ecludian":
                rresult=DistanceManager.Calculate_EcludienDistance(k,cr)
                result="Rate: "+" "+str(rresult[0])+" "+str(rresult[1])
            if method == "Cosin similarity":
                rresult=DistanceManager.Calculate_CousineDistance(k,cr)
                result="Rate: "+" "+str(rresult[0])+" "+str(rresult[1])
            self.resultData.configure(text=result)








class PageAdmin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # image = Image.open("book.jpg")
        # photo = ImageTk.PhotoImage(image)
        # label = tk.Label(image=photo)
        # label.image = photo  # keep a reference!
        # label.place(x=0, y=0, relwidth=1, relheight=1)
        helv36 = tkfont.Font(self,family='Helvetica', size=17, weight='bold')
        button = tk.Button(self, text="Logout",
                           command=lambda: controller.show_frame("StartPage"),font=helv36)
        button.place(x=890,y=10)
        button.config(height=1, width=7)




        label = tk.Label(self, text="Welcome Admin", font=controller.title_font)
        label.pack(side="top", pady=10)

        button1 = tk.Button(self, text="Add Book",
                            command=lambda: controller.show_frame("PageAddBook"),font=helv36)
        button2 = tk.Button(self, text="Add User",
                            command=lambda: controller.show_frame("PageAddUser"),font=helv36)
        button1.config(height=1, width=10)
        button2.config(height=1, width=10)

        button1.pack()
        button2.pack()


class PageAddBook(tk.Frame):
    titleField=tk.Entry();

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # image = Image.open("book.jpg")
        # photo = ImageTk.PhotoImage(image)
        # label = tk.Label(image=photo)
        # label.image = photo  # keep a reference!
        # label.place(x=0, y=0, relwidth=1, relheight=1)
        helv36 = tkfont.Font(self,family='Helvetica', size=17, weight='bold')
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("PageAdmin"),font=helv36)
        button.place(x=10,y=10)
        button.config(height=1, width=7)




        label = tk.Label(self, text="New Book", font=controller.title_font)
        label.pack(side="top", pady=10)

        titlelabel = tk.Label(self, text="Book Title", font=controller.title_font)
        titlelabel.place(x=230,y=100)

        self.titleField= tk.Entry(self,text="Title")
        self.titleField.place(x=360, y=107)

        button1 = tk.Button(self, text="Add",
                            command=self.on_button,font=helv36)

        button1.config(height=1, width=10)


        button1.place(x=420,y=180)

    def on_button(self):
        title=self.titleField.get()
        admin=Admin("Admin","11111")
        book=Book(title,0)
        admin.AddBook(book)

class PageAddUser(tk.Frame):
    nameField = tk.Entry()
    PassField = tk.Entry()
    unameField = tk.Entry()
    ageField = tk.Entry()
    salaryField = tk.Entry()
    v = tk.StringVar()
    v2 = tk.StringVar()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        helv36 = tkfont.Font(self,family='Helvetica', size=17, weight='bold')

        label = tk.Label(self, text="Sign Up", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("PageAdmin"),font=helv36)
        button.place(x=10,y=10)
        button.config(height=1, width=7)

        unameLabel=tk.Label(self,text="Username:",font=helv36)
        unameLabel.place(x=300,y=100)
        self.unameField= tk.Entry(self,text="Username")
        self.unameField.place(x=430, y=107)

        namePass=tk.Label(self,text="Password: ",font=helv36)
        namePass.place(x=300, y=150)
        self.PassField= tk.Entry(self,text="Password")
        self.PassField.place(x=430, y=157)

        nameLabel=tk.Label(self,text="Name: ",font=helv36)
        nameLabel.place(x=300, y=200)
        self.nameField= tk.Entry(self,text="Name")
        self.nameField.place(x=430, y=207)

        ageLabel=tk.Label(self,text="Age: ",font=helv36)
        ageLabel.place(x=300, y=250)
        self.ageField= tk.Entry(self,text="Age")
        self.ageField.place(x=430, y=257)

        salaryLabel=tk.Label(self,text="Salary: ",font=helv36)
        salaryLabel.place(x=300, y=300)
        self.salaryField= tk.Entry(self,text="Salary")
        self.salaryField.place(x=430, y=307)

        self.v = tk.StringVar()

        GenderLabel=tk.Label(self,text="Gender: ",font=helv36)
        GenderLabel.place(x=300, y=350)

        rdMale=tk.Radiobutton(self,
                       text="Male",
                       padx=20,
                       variable=self.v,
                       value='M')
        rdMale.place(x=400,y=354)
        rdFemale=tk.Radiobutton(self,
                       text="Female",
                       padx=20,
                       variable=self.v,
                       value='F')
        rdFemale.place(x=480,y=354)

        CreditLabel=tk.Label(self,text="Do you have a credit card? ",font=helv36)
        CreditLabel.place(x=300, y=400)
        self.v2 = tk.StringVar()
        rdYes=tk.Radiobutton(self,
                       text="Yes",
                       padx=20,
                       variable=self.v2,
                       value='Y')
        rdYes.place(x=350,y=450)
        rdNo=tk.Radiobutton(self,
                       text="No",
                       padx=20,
                       variable=self.v2,
                       value='N')
        rdNo.place(x=430,y=450)

        submit = tk.Button(self, text="Add",
                           command=self.on_button,font=helv36)
        submit.place(x=380,y=500)
        submit.config(height=1, width=7)

    def on_button(self):

                usernamee =self.unameField.get()
                password=self.PassField.get()
                name=self.nameField.get()
                age=self.ageField.get()
                salary=self.salaryField.get()
                gender=self.v.get()
                credit=self.v2.get()
                person = Person(usernamee, password, name, age, salary, gender, credit)
                person.Register(person)
                print(gender)


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("1000x600")
    app.configure(background='red')
    app.mainloop()