import urllib.request
import requests
import json
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont


class CurrencyConverter:
    def __init__(self, master):
        url = "https://www.google.pl/"
        self.get_currencies = ["PLN"]
        self.get_rate = []
        try:
            urllib.request.urlopen(url)
            self.source = requests.get("http://api.nbp.pl/api/exchangerates/tables/c/").json()[0]
            self.currencies = self.source['rates']
            self.data_date = self.source["effectiveDate"]
            self.alls = [self.currencies, self.data_date]
        except:
            with open('actual_rates.txt') as file:
                self.alls = json.load(file)
        with open('actual_rates.txt', 'w') as file:
            json.dump(self.alls, file)
        for i in range(0, len(self.alls[0])):
            self.get_currencies.append(self.alls[0][i]['currency'])
        for i in range(0, len(self.alls[0])):
            self.get_rate.append(self.alls[0][i]['bid'])
        self.get_rates = dict(zip(self.get_currencies[1:], self.get_rate))

        self.choose_from = StringVar(root)
        self.choose_to = StringVar(root)
        self.choose_from.set("currency")
        self.choose_to.set("currency")

        font1 = tkFont.Font(family="Calibri", size=9)
        font2 = tkFont.Font(family="Calibri", size=12, weight="bold")
        Label(root, text="CURRENCY CONVERTER", bg='#ffe8ec', font=font2).place(x=220, y=20)
        Label(root, text="Initial amount:", bg='#ffe8ec', font=font1).place(x=270, y=78)
        Label(root, text="From:", bg='#ffe8ec', font=font1).place(x=15, y=80)
        Label(root, text="To:", bg='#ffe8ec', font=font1).place(x=15, y=125)
        Label(root, text="Converted Amount:", bg='#ffe8ec', font=font1).place(x=270, y=125)
        date = Label(root, text='', bg='#ffe8ec')
        date.place(x=30, y=240)
        date['text'] = "Exchange rates data from:\n" + str(self.alls[1])

        self.initial_amount = Entry(root)
        self.converted_amount = Label(root, text='', bg='#ffe8ec')
        self.initial_amount.place(x=400, y=80)
        self.converted_amount.place(x=400, y=125)

        self.from_currency = OptionMenu(root, self.choose_from, *self.get_currencies)
        self.to_currency = OptionMenu(root, self.choose_to, *self.get_currencies)

        self.from_currency.place(x=70, y=75)
        self.to_currency.place(x=70, y=120)

        self.convert_button = Button(root, text="CONVERT", command=self.convert)
        self.convert_button.place(x=260, y=180)

        self.clear_button = Button(root, text="Clear", command=self.clear_all)
        self.clear_button.place(x=560, y=40)

        self.exit_button = Button(root, text="Exit", command=quit)
        self.exit_button.place(x=560, y=10)

    def convert(self):
        try:
            float(self.initial_amount.get())
            amount1 = float(self.initial_amount.get())
            if self.choose_from.get() == 'currency' or self.choose_to.get() == 'currency':
                messagebox.showinfo("Error", "Choose currencies.")
            elif self.choose_from.get() == self.choose_to.get():
                messagebox.showinfo("Typing error", "You can not convert the same currencies")
            elif amount1 <= 0:
                messagebox.showinfo("Typing error", "Amount shout be greater than 0")
            elif self.choose_from.get() == 'PLN':
                new_amount = round(amount1 / self.get_rates[self.choose_to.get()], 2)
            elif self.choose_to.get() == 'PLN':
                new_amount = round(amount1 * self.get_currencies[self.choose_from.get()], 2)
            else:
                pln_amount = amount1 * self.get_currencies[self.choose_from.get()]
                new_amount = round(pln_amount / self.get_currencies[self.choose_to.get()], 2)
            self.converted_amount['text'] = str(new_amount)
        except ValueError:
            messagebox.showinfo("Typing error", "Typed amount should be a number")

    def clear_all(self):
        self.initial_amount.delete(0, END)
        self.converted_amount['text'] = ''


if __name__ == '__main__':
    root = Tk()
    root.title("Przelicznik walut")
    root.configure(background='#ffe8ec')
    root.geometry("600x300")
    root.resizable(0,0)
    CurrencyConverter(root)
    root.mainloop()