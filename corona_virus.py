"""a Python Program to get corona virus details of india."""
from tkinter import Tk, Label, Entry, Button, BOTTOM, E, END, messagebox as msgbx, StringVar


# Initializing the root window
root = Tk()
root.title("Covid 19 Tracker by Paras4902")
root.geometry("600x500")
root.resizable(0, 0)


# Labels
Label(root, text="Covid 19 Tracker", font=("Times", 25, "bold underline"), fg="grey").pack()
Label(root, text="↓Country↓", font=("Helvetica", 15, "bold")).place(x=250, y=50)
Label(root, text="↓Confirmed↓", font=("Helvetica", 15, "bold")).place(x=70, y=150)
Label(root, text="↓Active↓", font=("Helvetica", 15, "bold")).place(x=400, y=150)
Label(root, text="↓Deaths↓", font=("Helvetica", 15, "bold")).place(x=85, y=250)
Label(root, text="↓Recovered↓", font=("Helvetica", 15, "bold")).place(x=380, y=250)
Label(root, text="@Paras4902", font=("Times", 25, "bold underline"), fg="grey").pack(side=BOTTOM, anchor=E)


# Entries
e1 = Entry(root, font=("Helvetica", 15, "bold"))
e2 = Entry(root, font=("Helvetica", 15, "bold"))
e3 = Entry(root, font=("Helvetica", 15, "bold"))
e4 = Entry(root, font=("Helvetica", 15, "bold"))
e5 = Entry(root, font=("Helvetica", 15, "bold"))


# Packing entries
e1.place(x=190, y=80)
e2.place(x=25, y=190)
e3.place(x=325, y=190)
e4.place(x=25, y=290)
e5.place(x=325, y=290)


# get_report_Function
def get_report():
    """function to get details about corona virus using covid module"""

    from covid import Covid  # pip install covid

    # deleting the text inside the entries
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

    # updating button's text and b1 widget
    txt.set("Getting Report....")
    b1.update()

    try:
        covid = Covid()
        cases = covid.get_status_by_country_name("India")

        # getting details
        c_name = cases['country']
        c_confirmed = cases['confirmed']
        c_active = cases['active']
        c_deaths = cases['deaths']
        c_recovered = cases['recovered']

        # inserting details
        e1.insert(END, c_name)
        e2.insert(END, c_confirmed)
        e3.insert(END, c_active)
        e4.insert(END, c_deaths)
        e5.insert(END, c_recovered)

    except Exception:
        msgbx.showerror("No Internet", "You're not connected to internet\nmake sure you are connected to internet")

    finally:
        txt.set("Get Report")


# Buttons
txt = StringVar()
txt.set("Get Report")
b1 = Button(root, textvariable=txt, font=("Times", 25, "bold"), bd=10, command=get_report, fg="cyan")
b1.place(x=200, y=350)


root.mainloop()
