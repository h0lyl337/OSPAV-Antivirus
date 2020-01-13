import __main__
import subprocess
import tkinter
import os


def startblockip():
    i = 0
    for ip in ipblocklist():
        print(i)
        subprocess.call(
            'netsh advfirewall firewall add rule name="ASS BLOCK" interface=any dir=in action=block remoteip="%s"'
            % ip.rstrip())
        subprocess.call(
            'netsh advfirewall firewall add rule name="ASS BLOCK" interface=any dir=out action=block remoteip="%s"'
            % ip.rstrip())
        i += 1


def ipblocklist():
    ip = []
    with open('{}\\ipblock'.format(os.getcwd()), 'r') as rx:
        for line in rx.readlines():
            ip.append(line)
            rx.close()
            yield line.rstrip()


def ipunblock(event):
    ipl = []
    __main__.nlistview.get(__main__.nlistview.curselection())
    with open('{}\\ipblock'.format(os.getcwd()), 'r') as rx:
        for ip in rx.readlines():
            if ip.rstrip() == __main__.nlistview.get(__main__.nlistview.curselection()):
                pass
            else:
                ipl.append(ip.rstrip())
    with open('{}\\ipblock'.format(os.getcwd()), 'w') as rx:
        for ip in ipl:
            rx.writelines(ip + '\n')
        rx.close()

    __main__.update_nlist_view()


def blockip(event):

    ipl = []
    print('Blocking ip')
    with open('{}\\ipblock'.format(os.getcwd(), 'r+')) as rx:
        for ip in rx.readlines():
            ipl.append(ip.rstrip())

    ipl.append(__main__.ipinput.get())
    with open('{}\\ipblock'.format(os.getcwd()), 'w') as rx:
        for ip in ipl:
            rx.writelines(ip + '\n')
        rx.close()

    subprocess.call(
        'netsh advfirewall firewall add rule name="ASS BLOCK" interface=any dir=in action=block remoteip=%s' % __main__.ipinput.get())
    subprocess.call(
        'netsh advfirewall firewall add rule name="ASS BLOCK" interface=any dir=out action=block remoteip=%s' % __main__.ipinput.get())
    __main__.update_nlist_view()
    __main__.ipinput.delete(0, tkinter.END )