import sys

def quick(arr, ini, end):
	i = ini
	j = end
	pivot = arr[(ini+end)//2]
	while i<j:
		while arr[i] < pivot:
			i+=1
		while arr[j] > pivot:
			j-=1
		if i<=j:	
			aux = arr[i]
			arr[i] = arr[j]
			arr[j] = aux
			i+=1
			j-=1
	if j> ini:
		quick(arr, ini, j)
	if i<end:
		quick(arr, i, end)


def main(fileName):
	print(fileName)
	f =  open(fileName[1], 'r+')
	arr = []
	for num in f.readlines():
		arr.append(int(num.rstrip('\n')))
	quick(arr,0,len(arr)-1)
	name = '''result/quick.%s'''%(fileName[1].replace("instancias/",""))
	open(name, 'w')
	f = open(name, 'w+')
	for i in arr:
		f.write("%d\n"%(i))

if __name__ == "__main__":
	main(sys.argv)

