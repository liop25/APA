import sys

def insertion(arr):
	for i in range(1,len(arr)):
		x = arr[i]
		j = i-1
		while j >= 0 and x < arr[j]:
			arr[j+1] = arr[j]
			j-=1
		arr[j+1] = x



def main(fileName):
	print(fileName)
	f =  open(fileName[1], 'r+')
	arr = []
	for num in f.readlines():
		arr.append(int(num.rstrip('\n')))
	insertion(arr)
	name = '''result/insertion.%s'''%(fileName[1].replace("instancias/",""))
	open(name, 'w')
	f = open(name, 'w+')
	for i in arr:
		f.write("%d\n"%(i))

if __name__ == "__main__":
	main(sys.argv)

