# -*- coding=utf-8 -*-


import threading

#创建全局TreadLocal对象：
local_school = threading.local()

def process_student():
	print 'Hello, %s (in %s)\n' %(local_school.student, threading.current_thread().name)

def process_thread(name):
	#绑定ThreadLocal的student
	local_school.student = name
	process_student()


t1 = threading.Thread(target= process_thread,args= ('Alice',), name='A')
t2 = threading.Thread(target= process_thread,args= ('Sum',),name= 'B')
t1.start()
t2.start()
t1.join()
t2.join()
