import ttkthemes
import tkinter
import os
import queue
from tkinter import *
from tkinter import ttk
import threading
from datetime import datetime
import subprocess
import platform
import signal
import socket
import process_control
import network
import config
import filescan
import vtotal
import menu

maindir = []
scan_detected = []
downloads_comparison = []
startup_comparison = []
maindir.append(os.getcwd())
detaine_detected = []
auto_delete_detected = []

class App:
    def __init__(self, master):
        host = socket.gethostname()
        global ipaddress
        ipaddress = socket.gethostbyname(host)
        global textbox
        global checkbox_auto_scan_download
        global checkbox_auto_scan_process
        global checkbox_auto_vtotal
        global update_text
        global nlistview
        global ipinput
        global scan_detected_list
        global root
        global checkbox_auto_scan_download_var
        global checkbox_auto_scan_startup_var
        global checkbox_auto_scan_process_var
        global check_auto_vtotal_var
        global detected_list
        global _sql_server
        global _sql_hashdb
        global _sql_user
        global _sql_pass
        global q
        global menubar

        q = queue.Queue()
        checkbox_auto_scan_download_var = BooleanVar()
        checkbox_auto_scan_startup_var = BooleanVar()
        checkbox_auto_scan_process_var = BooleanVar()
        check_auto_vtotal_var = BooleanVar()
        detected_list = []

        _sql_server = ''
        _sql_hashdb = ''
        _sql_user = ''
        _sql_pass = ''

        menubar = Menu(root)
        menubar.config(background='black', activebackground='black')

        file = Menu(menubar)
        file.add_command(label='Get File Hash')
        file.add_command(label='Encrypt file')
        file.add_command(label='get file md5')

        database_menu = Menu(menubar)
        database_menu.add_command(label='Select database', command=menu._databasemenu)
        database_menu.add_command(label='search for hash', command=menu._selecthashmenu)
        database_menu.add_command(label='Add hash if not exist')

        account_menu = Menu(menubar)
        account_menu.add_command(label='Login')
        account_menu.add_command(label='Logoff')
        account_menu.add_command(label='Virus-Total API key')
        account_menu.add_command(label='Account settings')

        server_menu = Menu(menubar)
        server_menu.add_command(label='Enable Master mode')
        server_menu.add_command(label='Disable Master mode')

        about_menu = Menu(menubar)
        about_menu.add_command(label='Developers', command=menu.about_menu)

        menubar.add_cascade(label='File', menu=file)
        menubar.add_cascade(label='Database', menu=database_menu)
        menubar.add_cascade(label='Account', menu=account_menu)
        menubar.add_cascade(label='Server-Settings', menu=server_menu)
        menubar.add_cascade(label='About', menu=about_menu)

        tabocontrol = ttk.Notebook()
        tabocontrol.configure()
        tab1 = tkinter.Frame(tabocontrol)
        tab1.configure(bg='#424242')
        tab2 = ttk.Frame(tabocontrol)
        tab3 = ttk.Frame(tabocontrol)
        tab4 = ttk.Frame(tabocontrol)
        tabocontrol.add(tab1, text='Main')
        tabocontrol.add(tab2, text='Network')
        tabocontrol.add(tab3, text='Extensions')
        tabocontrol.add(tab4, text='System-Information')
        textbox = Text(tab1, height=5, width=200, font=("Helvetica", 10))
        textbox.configure(bg='grey', state=DISABLED)
        textbox.pack(side=BOTTOM)
        network_tab_control = ttk.Notebook(tab2)
        network_tab_control.pack(expand=1, fill="both")
        ntab1 = ttk.Frame(network_tab_control)
        ntab2 = ttk.Frame(network_tab_control)
        network_tab_control.add(ntab1, text='Firewall-Settings')
        network_tab_control.add(ntab2, text='Information')

        # MAIN TAB 1 #
        tabocontrol.pack(expand=1, fill="both")
        checkbox_auto_scan_download = Checkbutton(tab1, text='Auto-Scan Downloads', variable=checkbox_auto_scan_download_var, command=check_autoscan_download_box_status)
        checkbox_auto_scan_download.pack(anchor='ne')
        checkbox_auto_scan_download.configure(bg='#424242', fg='white', activebackground='#424242')
        checkbox_auto_scan_startup = Checkbutton(tab1, text='Auto-Scan Startup       ')
        checkbox_auto_scan_startup.pack(anchor='ne')
        checkbox_auto_scan_startup.configure(bg='#424242', fg='white', activebackground='#424242')
        checkbox_auto_scan_process = Checkbutton(tab1, text='Auto-Scan Process      ', variable=checkbox_auto_scan_process_var, command=check_autoscan_process_box_status)
        checkbox_auto_scan_process.pack(anchor='ne')
        checkbox_auto_scan_process.configure(bg='#424242', fg='white', activebackground='#424242')

        checkbox_auto_vtotal = Checkbutton(tab1, text='Virus-Total Scan     ', variable=check_auto_vtotal_var, command=check_auto_vtotal)
        checkbox_auto_vtotal.place(x=225, y=0)
        checkbox_auto_vtotal.configure(bg='#424242', fg='white', activebackground='#424242')

        network.startblockip()
        scan_detected_label = tkinter.Label(tab1, text='         Detected:')
        scan_detected_list = tkinter.Listbox(tab1)
        scan_detected_label.place(x=0, y=0)
        scan_detected_label.config(bg='#424242', fg='white')
        scan_detected_list.place(x=0, y=20)

        # NETWORK TAB 1 #
        ipa = Label(ntab1, text='IP:' + ipaddress)
        ipa.pack(anchor='ne')
        ipa.configure(bg='#424242', fg='white')
        style = ttkthemes.ThemedStyle(root)
        style.theme_use('black')
        nlistlistlabel = Label(ntab1, text="Blocked IP's")
        nlistlistlabel.place(x=0, y=0)
        nlistlistlabel.configure(bg='#424242', fg='red')
        nlistview = tkinter.Listbox(ntab1)
        nlistview.configure(bg='grey')
        for item in network.ipblocklist():
            nlistview.insert(END, item)
        nlistview.pack(anchor='nw')
        buttonunblockip = Button(ntab1, text='UnBlock  ')
        buttonunblockip.bind('<Button-1>', network.ipunblock)
        buttonunblockip.place(x=0, y=185)
        buttonblockip = Button(ntab1, text='Block        ')
        buttonblockip.bind('<Button-1>', network.blockip)
        buttonblockip.place(x=60, y=185)
        ipinput = Entry(ntab1)
        ipinput.place(x=0, y=210)

        # SYSTEM INFORMATION

        _syslabel = Label(tab4, text='System: {}'.format(platform.uname()[0]))
        _nodelabel = Label(tab4, text='Node: {}'.format(platform.uname()[1]))
        _releaselabel = Label(tab4, text='Release: {}'.format(platform.uname()[2]))
        _versionlabel = Label(tab4, text='Version: {}'.format(platform.uname()[3]))
        _machinelabel = Label(tab4, text='Machine: {}'.format(platform.uname()[4]))
        _proclabel = Label(tab4, text='Processor: {}'.format(platform.uname()[5]))

        _syslabel.pack(anchor='nw')
        _nodelabel.pack(anchor='nw')
        _releaselabel.pack(anchor='nw')
        _versionlabel.pack(anchor='nw')
        _machinelabel.pack(anchor='nw')
        _proclabel.pack(anchor='nw')



def check_autoscan_download_box_status():
    if checkbox_auto_scan_download_var.get() == TRUE:
        checkbox_auto_scan_download.configure(fg='green')
        t1 = threading.Thread(target=filescan.scan_downloads)
        t1.setDaemon(TRUE)
        t1.start()
        root.after(10000, check_autoscan_download_box_status)
    if checkbox_auto_scan_download_var.get() == FALSE:
        checkbox_auto_scan_download.configure(fg='white')


def check_autoscan_startup_box_status():
    if checkbox_auto_scan_download_var.get() == TRUE:
        checkbox_auto_scan_download.configure(fg='green')
        t1 = threading.Thread(target=filescan.scan_downloads)
        t1.setDaemon(TRUE)
        t1.start()
        root.after(10000, check_autoscan_download_box_status)
    if checkbox_auto_scan_download_var.get() == FALSE:
        checkbox_auto_scan_download.configure(fg='white')


def check_autoscan_process_box_status():
    if checkbox_auto_scan_process_var.get() == TRUE:
        checkbox_auto_scan_process.configure(fg='green', state=DISABLED)
        t1 = threading.Thread(target=process_control.mainn())
        t1.setDaemon(TRUE)
        t1.start()
    if checkbox_auto_scan_process_var.get() == FALSE:
        checkbox_auto_scan_process.configure(fg='white')


def check_auto_vtotal():
    if check_auto_vtotal_var.get() == TRUE:
        checkbox_auto_vtotal.config(fg="green")
        root.update()

    if check_auto_vtotal_var.get() == FALSE:
        checkbox_auto_vtotal.configure(fg='white')


def update_text(text):
    textbox.config(state='normal')
    times = datetime.now().strftime('%H:%M:%S')
    textbox.insert(INSERT, '%s %s \n' %(times, text))
    textbox.see('end')
    textbox.config(state=DISABLED)
    root.update()


def update_detected_list_view():
    scan_detected_list.delete(0, END)
    for file in detected_list:
        scan_detected_list.insert(END, file)
    root.update()


def update_nlist_view():
    nlistview.delete(0, END)
    for file in network.ipblocklist():
        nlistview.insert(END, file)
    root.update()


def on_exit():
    global proc
    subprocess.call('netsh advfirewall firewall delete rule name="ASS BLOCK"')
    root.destroy()
    try:
        proc.send_signal(signal.CTRL_BREAK_EVENT)
        proc.kill()
    except:
        pass
        exit()


if __name__ == '__main__':
        root = tkinter.Tk()
        App(root)
        root.config(menu=menubar)
        title = Label(root, text='AssAV v1.01')
        root.geometry('500x300')
        root.resizable(False, False)
        root.title('ASS(Advance Security Software) v1.01 by H0lyL337')
        config.config_set_up()
        root.protocol("WM_DELETE_WINDOW", on_exit)
        root.mainloop()

