from Book import Book
import FileManager
import tkinter as tk
from tkinter import messagebox

class Person:

    Username=""
    Password=""
    Name = ""
    Age = 0
    Salary = 0
    Gender = ''
    HasCreditCard = ''
    Books = []

    def __init__(self,username,password,name, age, salary, gender, hasCreditCard):
        self.Username = username
        self.Password = password
        self.Name = name
        self.Age = age
        self.Salary = salary
        self.Gender = gender
        self.HasCreditCard = hasCreditCard
        self.Books = []

    def RateBook(self, Book, rate):
        Book.Rate = rate
        self.Books.append(Book)
        print("pr", self.Name)
        FileManager.AddRating(self.Name +" "+ Book.Title +" "+ str(rate))
        msg = tk.messagebox.showinfo("Success","Rated Successfully")

    def Register(self, person):
        FileManager.WriteData(person.Username +" "+ person.Password +" "+ person.Name +" "+ person.Age+ " "+ person.Salary +" "+ person.Gender +" "+ person.HasCreditCard, 1)
        FileManager.NormalizeData()
        msg = tk.messagebox.showinfo("Success","Registered Successfully")
