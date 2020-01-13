import __main__
import os
import subprocess
import filescan
import process_control
import threading

def config_set_up():
    with open('{}\\config.cfg'.format(os.getcwd())) as config:
        read = config.readlines(0)
        auto_scan_download = read[0].strip()
        auto_scan_startup = read[1].strip()
        auto_scan_process = read[2].strip()
        extention = read[4].strip().strip()

        if auto_scan_download == '1':
            __main__.update_text('Auto Scan download is active')
            __main__.textbox.see('end')
            __main__.root.update()
            __main__.checkbox_auto_scan_download.toggle()

            __main__.checkbox_auto_scan_download.config(fg='green')
            __main__.root.update()
            threading.Thread(filescan.scan_downloads()).start()
        else:
            __main__.update_text('Auto Scan Downloads Disabled')

        if auto_scan_process == '1':
            __main__.update_text('Auto Scan Process is active')
            threading.Thread(target=process_control.mainn, args=([__main__.root]), daemon=True).start()
        else:
            __main__.update_text('Auto Scan Process is disabled')
            __main__.root.update()

        if extention == '1':
            __main__.update_text('Auto Extention Enabled')
            files = os.listdir('{}\\extensions'.format(os.getcwd()))
            for file in files:
                if '.py' in file:
                    global proc
                    proc = subprocess.Popen('python {}\\extensions\\{}'.format(os.getcwd(), file), creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        else:
            __main__.update_text('Auto Extention Disabled')
    config.close()
    __main__.root.update()