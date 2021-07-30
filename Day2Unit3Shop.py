import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title('Shopping')
canvas1 = tk.Canvas(root, width=400, height=350, relief='raised')
canvas1.pack()
class Item:
    def __init__(self, name: str, cost: float, quantity: int, itemtype):
        self.name = name
        self.cost = cost
        self.quantity = quantity
        self.itemtype = itemtype
    def in_stock(self) -> bool:
        return self.quantity > 0
    def __str__(self) -> str:
        return "OVERRIDE PER CHILD CLASS"
    def calculate_total(self) -> float:
        return 0.0
class Book(Item):
    def __str__(self):
        return f"You bought a {self.name}."
    def calculate_total(self):
        return self.cost * self.quantity * self.itemtype
class Electronic(Item):
    def __str__(self):
        return f"You bought a {self.name}."
    def calculate_total(self):
        return self.cost * self.quantity * self.itemtype
class Food(Item):
    def __str__(self):
        return f"You bought a {self.name}"
    def calculate_total(self):
        return self.cost * self.quantity * self.itemtype
class Tablet(Item):
    def __str__(self):
        return f"You bought an {self.name}"
    def calculate_total(self):
        return self.cost * self.quantity * self.itemtype


cart = []


shop_items = [
    Book("101 WAYS TO CODE", 5.99, 2, 1.1),
    Book("COOKING MASTERPIECES", 11.99, 3, 1.1),
    Electronic("MP3 PLAYER", 2.99, 10, 1.3),
    Electronic("USB DATA STICK", 9.99, 3, 1.3),
    Food("PACK OF APPLES", 2.99, 3, 0.7),
    Food("PINT OF MILK", 0.79, 20, 0.7),
    Tablet("ANDROID TABLET", 49.99, 1, 1.9),
    Tablet("APPLE TABLET", 209.99, 1, 1.9)
]
lower_shop_items = [
    Book("101 ways to code", 5.99, 2, 1.1),
    Book("Cooking Masterpieces", 11.99, 3, 1.1),
    Electronic("MP3 Player", 2.99, 10, 1.3),
    Electronic("USB data stick", 9.99, 3, 1.3),
    Food("Pack of apples", 2.99, 3, 0.7),
    Food("Pint of Milk", 0.79, 20, 0.7),
    Tablet("Android tablet", 49.99, 1, 1.9),
    Tablet("Apple tablet", 209.99, 1, 1.9)
]
label1 = tk.Label(root, text='Buy a product:')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)
entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)
names_list = []
lower_names_list = []
for i in shop_items:
    names_list.append(i.name)
for i in lower_shop_items:
    lower_names_list.append(i.name)
def AddToCart():
    got = entry1.get()
    if got.upper() in names_list:
        conf = messagebox.askyesno("Confirmation", f"Are you sure you want to add {got} to your cart?")
        if conf == True:
            cart.append(got)
    else:
        messagebox.showerror("Error", f"Not valid. These are some valid products:\n{lower_names_list}")
def ViewCart():
    messagebox.showinfo("Cart", cart)
def BuyCart():
    buy = messagebox.askyesnocancel("Buy Cart", f"Are you sure you want to buy your full cart? \n\n\nThis includes:\n\n\n{cart}")
    if buy == True:
        messagebox.showinfo("Yay!", "Your order is on it\'s way!")
button1 = tk.Button(text='Add to cart', command=AddToCart, bg="orange", fg="black", font=('Arial', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)
button2 = tk.Button(text='View Cart', command=ViewCart, bg="light blue", fg="white", font=('Arial', 9, 'bold'))
canvas1.create_window(200, 240, window=button2)
button3 = tk.Button(text='Buy Cart', command=BuyCart, bg="grey", fg="white", font=('Arial', 9, 'bold'))
canvas1.create_window(200, 300, window=button3)


root.mainloop()