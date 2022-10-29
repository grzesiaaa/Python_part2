import urllib.request
import requests
import json
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont


def get_actual_rates():
    """
    Download actual currency exchange rates or if no internet connection open recently saved rates.
    :return: actual rates, names of currencies, a dictionary of rates and currencies
    """
    url = 'https://www.google.pl/'
    get_currencies = ["PLN"]
    get_rate = []
    try:
        urllib.request.urlopen(url)
        source = requests.get("http://api.nbp.pl/api/exchangerates/tables/c/").json()[0]
        currencies = source['rates']
        data_date = source["effectiveDate"]
        alls = [currencies, data_date]
    except:
        with open('actual_rates.txt') as file:
            alls = json.load(file)
    with open('actual_rates.txt', 'w') as file:
        json.dump(alls, file)
    for i in range(0, len(alls[0])):
        get_currencies.append(alls[0][i]['currency'])
    for i in range(0, len(alls[0])):
        get_rate.append(alls[0][i]['bid'])
    get_rates = dict(zip(get_currencies[1:], get_rate))
    return get_rates, get_currencies, alls


def graphic_converter():
    """
    Create a graphical currency converter.
    """
    rates = get_actual_rates()[0]
    currencies = get_actual_rates()[1]
    date_of_rates = get_actual_rates()[2][1]

    root = Tk()
    root.title("Currency converter")
    root.configure(background='#ffe8ec')
    root.geometry("600x300")
    root.resizable(0, 0)

    font1 = tkFont.Font(family="Calibri", size=9)
    font2 = tkFont.Font(family="Calibri", size=12, weight="bold")
    Label(root, text="CURRENCY CONVERTER", bg='#ffe8ec', font=font2).place(x=220, y=20)
    Label(root, text="Initial amount:", bg='#ffe8ec', font=font1).place(x=270, y=78)
    Label(root, text="From:", bg='#ffe8ec', font=font1).place(x=15, y=80)
    Label(root, text="To:", bg='#ffe8ec', font=font1).place(x=15, y=125)
    Label(root, text="Converted Amount:", bg='#ffe8ec', font=font1).place(x=270, y=125)
    date = Label(root, text='', bg='#ffe8ec')
    date.place(x=30,y=240)
    date['text'] = "Exchange rates data from:\n" + str(date_of_rates)

    choose_from = StringVar(root)
    choose_to = StringVar(root)
    choose_from.set("currency")
    choose_to.set("currency")

    initial_amount = Entry(root)
    converted_amount = Label(root, text='', bg='#ffe8ec')
    initial_amount.place(x=400, y=80)
    converted_amount.place(x=400, y=123)

    from_currency = OptionMenu(root, choose_from, *currencies)
    to_currency = OptionMenu(root, choose_to, *currencies)
    from_currency.place(x=70, y=75)
    to_currency.place(x=70, y=120)

    def clear():
        """
        Clear entered data.
        """
        initial_amount.delete(0, END)
        converted_amount['text'] = ''

    def convert():
        """
        Convert chosen currencies.
        """
        try:
            float(initial_amount.get())
            amount = float(initial_amount.get())
            if choose_from.get() == 'currency' or choose_to.get() == 'currency':
                messagebox.showinfo("Error", "Choose currencies.")
            elif choose_from.get() == choose_to.get():
                messagebox.showinfo("Typing error", "You can not convert the same currencies")
            elif amount <= 0:
                messagebox.showinfo("Typing error", "Amount shout be greater than 0")
            elif choose_from.get() == 'PLN':
                new_amount = round(amount / rates[choose_to.get()], 2)
                converted_amount['text'] = str(new_amount)
            elif choose_to.get() == 'PLN':
                new_amount = round(amount * rates[choose_from.get()], 2)
                converted_amount['text'] = str(new_amount)
            else:
                pln_amount = amount * rates[choose_from.get()]
                new_amount = round(pln_amount / rates[choose_to.get()], 2)
                converted_amount['text'] = str(new_amount)
        except ValueError:
            messagebox.showinfo("Typing error", "Typed amount should be a number")

    convert_button = Button(root, text="CONVERT", command=convert)
    convert_button.place(x=270, y=180)

    clear_button = Button(root, text="Clear", command=clear, font=font1)
    clear_button.place(x=560, y=40)

    exit_button = Button(root, text="Exit", command=quit)
    exit_button.place(x=560, y=10)
    root.mainloop()


"""if __name__=="__main__":
    graphic_converter()"""

graphic_converter()
