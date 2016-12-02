# -*- coding: utf-8 -*-

from multiprocessing import Process
import os

#子进程执行
def run_proc(name):

	print 'Run child process %s (%s)...' %(name,os.getpid())
	while 1:
		pass
if __name__=='__main__':
	print 'Process (%s) start...' % os.getpid()
	p = Process(target=run_proc, args=('test',))
	print 'Process will start'
	p.start()
	while 1:
		pass
	p.join()
	print 'Process end.'





