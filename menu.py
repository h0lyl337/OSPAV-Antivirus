import __main__
from tkinter import *
import tkinter


def _databasemenu():
    global server_input
    global database_input
    global username_input
    global passwd_input
    global database_pop

    database_pop = Tk()
    server_text = Label(database_pop, text='Server IP:')
    server_input = Entry(database_pop)
    database_text = Label(database_pop, text='Database name:')
    database_input = Entry(database_pop)
    username_text = Label(database_pop, text='Username:')
    username_input = Entry(database_pop)
    passwd_text = Label(database_pop, text='Passwd:')
    passwd_input = Entry(database_pop)
    database_submit = Button(database_pop, text='OK')

    server_text.pack()
    server_input.pack()
    database_text.pack()
    database_input.pack()
    username_text.pack()
    username_input.pack()
    passwd_text.pack()
    passwd_input.pack()
    database_submit.pack()
    database_submit.bind('<Button-1>', database_pop_button)
    database_pop.title('database menu')
    server_text.config(bg='#424242', fg='white')
    username_text.config(bg='#424242', fg='white')
    passwd_text.config(bg='#424242', fg='white')
    database_text.config(bg='#424242', fg='white')
    database_pop.geometry('260x200')
    database_pop.config(bg='#424242')
    database_pop.mainloop()


def _selecthashmenu():
    window = Tk()
    hash_text = Label(window, text='Hash to search:')
    hash_input = Entry(window)
    ok_button = Button(window, text='OK')


    hash_text.pack()
    hash_input.pack()
    ok_button.pack()
    window.title('Hash Search')
    hash_text.config(bg='#424242', fg='white')
    window.config(bg='#424242')
    window.geometry('250x125')
    window.mainloop()


def database_pop_button(event):

    __main__._sql_server = server_input.get()
    __main__._sql_hashdb = database_input.get()
    __main__._sql_user = username_input.get()
    __main__._sql_pass = passwd_input.get()

    print(locals())

    database_pop.destroy()


def about_menu():
    window = Tk()
    con_label = Label(window, text='Contributors:')
    cons = Label(window, text='H0lyL337, Your name here')

    con_label.pack()
    cons.pack()
    window.title('About')
    window.mainloop()