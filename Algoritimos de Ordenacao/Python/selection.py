import sys

def selection(arr):
	for i in range(len(arr)):
		min = i
		for j in range(i+1, len(arr)):
			if arr[j]  < arr[min]:
				min = j;
		if i != min:		
			aux = arr[i]
			arr[i] = arr[min]
			arr[min] = aux


def main(fileName):
	print(fileName)
	f =  open(fileName[1], 'r+')
	arr = []
	for num in f.readlines():
		arr.append(int(num.rstrip('\n')))
	selection(arr)
	name = '''result/selection.%s'''%(fileName[1].replace("instancias/",""))
	f = open(name, 'w+')
	for i in arr:
		f.write("%d\n"%(i))

if __name__ == "__main__":

	main(sys.argv)

