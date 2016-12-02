# -*- coding: utf-8 -*-

import time,threading
#假定这是银行存款

balance = 0
lock = threading.Lock()

def change_it(n):
	#先存后取 结果为0

	global balance

	balance = balance + n
	balance = balance - n

def run_thread(n):

	for i in range(100000):

		lock.acquire()
		try:
			# print n
			change_it(n)
		finally:
			lock.release()
		


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()

print balance