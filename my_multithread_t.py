import multiprocessing
import time
import sys

def worker(num):
    p = multiprocessing.current_process()
    print ('Starting:' + p.name + ":" + str(p.pid))
    print(str(num))
    sys.stdout.flush()
    print ('Exiting :' + p.name + ":" + str(p.pid))
    sys.stdout.flush()

def daemon():
    p = multiprocessing.current_process()
    print ('Starting:' + p.name + ":" + str(p.pid))
    sys.stdout.flush()
    time.sleep(10)
    print ('Exiting :' + p.name + ":" + str(p.pid))
    sys.stdout.flush()
    
def non_daemon():
    p = multiprocessing.current_process()
    print ('Starting:' + p.name + ":" + str(p.pid))
    sys.stdout.flush()
    time.sleep(20)
    print ('Exiting :' + p.name + ":" + str(p.pid))
    sys.stdout.flush()
    
if __name__ == '__main__':
    w = multiprocessing.Process(name='worker', target=worker, args=(100,))
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True
    nd = multiprocessing.Process(name='non-daemon', target=non_daemon)
    w.start()
    d.start()
    nd.start()
    
    print("the number of CPU is " + str(multiprocessing.cpu_count()))
    print("All children processes:")
    for p in multiprocessing.active_children():
        print("child:" + p.name + ":" + str(p.pid))
    print()
    
    w.join()
    d.join()