import FileManager
import tkinter as tk
from tkinter import messagebox

class Admin:

    Username = ""
    Password = ""

    def __init__(self, username, password):
        self.Username = username
        self.Password = password

    def AddPerson(self,person):
        FileManager.WriteData(person.Name + " " + person.Age + " " + person.Salary + " " + person.Gender + " " + person.HasCreditCard, 1)
        print("Person added successfully")


    def AddBook(self, book):
        FileManager.AddBook(book.Title)
        print("Book Added Successfully")
        msg=tk.messagebox.showinfo(" Success","Book Added Successfully")

