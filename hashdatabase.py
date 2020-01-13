import __main__
import mysql.connector


def find_hash(hash):
    print('starting hash search')

    db = mysql.connector.connect(user='{}'.format(__main__._sql_user),
                                 password='{}'.format(__main__._sql_pass),
                                 host='{}'.format(__main__._sql_server),
                                 database='{}'.format(__main__._sql_hashdb))
    c = db.cursor()
    c.execute('''
    SELECT hash FROM sig WHERE hash='%s'
    '''%(hash))
    try:
        __main__.q.put(c.fetchone()[0])
        print('done')
    except:
        __main__.q.put('None')



def insert_new_hash(hash):
    if find_hash(hash) == hash:
        print('hash already in db.')

    else:
        print('this hash is new, adding now')


def get_count_hash():
    db = mysql.connector.connect(user='{}'.format(__main__._sql_user),
                                 password='{}'.format(__main__._sql_hashdb),
                                 host='{}'.format(__main__._sql_server),
                                 database='{}'.format(__main__._sql_hashdb))
    c = db.cursor()
    c.execute('''
    SELECT COUNT(*) FROM sig
    ''')
    print('ended')

    return c.fetchone()[0]


def remove_hash(hash):
    db = mysql.connector.connect(user='{}'.format(__main__._sql_hashdb),
                                 password='{}'.format(__main__._sql_hashdb),
                                 host='{}'.format(__main__._sql_server),
                                 database='{}'.format(__main__._sql_hashdb))
    c = db.cursor()
    c.execute('''
    DELETE FROM sig WHERE hash="{}"
    '''.format(hash))
    db.commit()


def update():
    print('asdf')
