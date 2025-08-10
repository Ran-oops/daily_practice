from multiprocessing import Process, Manager

def modify(shared_dict, shared_list):
    shared_dict['key'] = 'new_value'
    shared_list.append(99)

if __name__ == '__main__':
    with Manager() as manager:
        shared_dict = manager.dict()
        shared_list = manager.list()
        p = Process(target=modify, args=(shared_dict, shared_list))
        p.start()
        p.join()
        print(shared_dict)

        print(shared_list)