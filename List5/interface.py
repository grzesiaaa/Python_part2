from tkinter import *
import requests
import sys


source = requests.get("http://api.nbp.pl/api/exchangerates/tables/c/").json()[0]
currencies = source['rates']
source_date = source['effectiveDate']


waluty = []
przelicznik = []

for i in range(0,len(currencies)):
    waluty.append(currencies[i]['currency'])

for i in range(0,len(currencies)):
    przelicznik.append(currencies[i]['bid'])

przeliczniki = dict(zip(waluty,przelicznik))
waluty.append("PLN")

root=Tk()

variable1 = StringVar(root)
variable2 = StringVar(root)

variable1.set("currency")
variable2.set("currency")

def clear_all() :
    initial_amount.delete(0, END)
    converted_amount.delete(0, END)

def quit():
    sys.exit()

def converter():
    amount1 = float(initial_amount.get())
    if variable1.get() == 'PLN':
        new_amount = round(amount1 / przeliczniki[variable2.get()], 2)
        converted_amount.insert(0, str(new_amount))
    elif variable2.get() == 'PLN':
        new_amount = round(amount1 * przeliczniki[variable1.get()],2)
        converted_amount.insert(0, str(new_amount))
    else:
        pln_amount = amount1 * przeliczniki[variable1.get()]
        new_amount = round(pln_amount / przeliczniki[variable2.get()], 2)
        converted_amount.insert(0, str(new_amount))


if __name__ == "__main__":
    root.title("Przelicznik walut")
    root.configure(background='#ffe8ec')
    root.geometry("600x300")

    Label(root, text="Currency converter").place(x=240,y=20)
    Label(root, text="Initial amount:").place(x=270,y=80)
    Label(root, text="From:").place(x=15, y = 80)
    Label(root, text="To:").place(x =15, y = 125)
    Label(root, text="Converted Amount:").place(x=270, y = 125)

    initial_amount = Entry(root)
    converted_amount = Entry(root)
    initial_amount.place(x=400, y=80)
    converted_amount.place(x=400, y=125)


    CurrencyCode_list = waluty

    from_currency = OptionMenu(root, variable1, *CurrencyCode_list)
    to_currency = OptionMenu(root, variable2, *CurrencyCode_list)

    from_currency.place(x=70,y =75)
    to_currency.place(x=70, y = 120)

    convert_button = Button(root, text="CONVERT", command=converter)
    convert_button.place(x=260,y=180)

    clear_button = Button(root, text="Clear", command=clear_all)
    clear_button.place(x=560,y=40)

    exit_button=Button(root, text="Exit", command = quit)
    exit_button.place(x=560,y=10)
    root.mainloop()