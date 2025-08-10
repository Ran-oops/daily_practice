from multiprocessing import shared_memory, Process
import numpy as np

def worker(shm_name):
    # 连接到现有共享内存
    shm = shared_memory.SharedMemory(name=shm_name)
    arr = np.ndarray((3,), dtype=np.int64, buffer=shm.buf)
    arr[0] = 100  # 修改数据


if __name__ == '__main__':
    # 创建初始数据
    orig_arr = np.array([1, 2, 3], dtype=np.int64)
    # 创建共享内存并复制数据
    shm = shared_memory.SharedMemory(create=True, size=orig_arr.nbytes)
    shm_arr = np.ndarray(orig_arr.shape, dtype=orig_arr.dtype, buffer=shm.buf)
    shm_arr[:] = orig_arr[:]
    p = Process(target=worker, args=(shm.name,))
    p.start()
    p.join()
    print(shm_arr)
    shm.close()
    shm.unlink()  # 销毁共享内存