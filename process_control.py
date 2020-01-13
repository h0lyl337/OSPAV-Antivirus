import psutil
import hashlib
import __main__
import hashdatabase
import threading
import filescan

check_proc = psutil.process_iter()
proc_list = ['consent.exe', ]
def mainn():
    __main__.update_text('scanning running processes')
    for proc in psutil.process_iter():
        proc_list.append(proc.name())
        __main__.root.update()
    while 1:
        for proc in psutil.process_iter():
            __main__.root.update()
            if proc.name() not in proc_list:
                __main__.root.update()
                __main__.update_text('New Process %s found.' % proc.name())
                opened_file = open(proc.exe(), 'rb')
                readfile = hashlib.md5(opened_file.read())
                hash = readfile.hexdigest()
                __main__.root.update()
                if hash not in filescan.return_download_hash_list():
                    threading.Thread(target=hashdatabase.find_hash, args=([hash]), daemon=True ).start()
                    while __main__.q.empty() == True:
                        __main__.root.update()
                    else:
                        pass
                        if __main__.q.get() == hash:
                            print('match found')
                            __main__.detected_list.append(proc.exe())
                            __main__.update_detected_list_view()
                            __main__.root.update()
                        else:
                            print('no match')
                            __main__.update_text("{} seems to be good!".format(proc.name()))
                            proc_list.append(proc.name())
                            filescan.add_clean_hash(hash)
                            __main__.root.update()
                else:
                    proc_list.append(proc.name())
                    __main__.update_text("{} was already scanned & seems to be good!".format(proc.name()))
        __main__.root.update()
