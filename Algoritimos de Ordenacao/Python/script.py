import os
import time
from multiprocessing import	 Process

#pra rodar python script.py@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
fileNames = ['heap.py', 'insertion.py', 'merge.py', 'selection.py', 'quick.py']
entro = [10,50,90]
filesize = [100000, 500000,1000000]
open('time.txt','w').write("")

def exectu(fileName):
	os.system(fileName)		

def fun(name, fileName):
	begin = time.time()
	#muda o comando aqui VVVVVV
	execPy = "python %s %s"%(name,fileName)
	#^^^^^^^^^
	p = Process(target=exectu, name = "foo", args=(execPy,))
	p.start()
	begin = time.time()
	end = begin
	while p.is_alive():
		if (end - begin) > 5*60:
			p.terminate()
			p.join()
		end = time.time()
	open('time.txt', 'a').write('%s - %s: %.3f ms\n'%(name,fileName,(end-begin)*1000))

for x in entro:
	for i in range(1,6):
		for a in filesize:
			fileName = '''instancias/%d.%d.%d.in'''% (x,a,i) 
			print(fileName)	
			for name in fileNames:
				fun(name, fileName)
				



