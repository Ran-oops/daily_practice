from multiprocessing import Process, Pipe


def child(conn):
    conn.send([42, None, 'hello'])
    conn.close()



if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=child, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()