import sys

def heap(arr):
	n = len(arr)
	i = len(arr)//2
	while True:
		if i>0:
			i-=1
			t = arr[i]
		else:
			n-=1
			if n == 0:
				return
			t = arr[n]
			arr[n] = arr[0]
		parent = i
		child = i*2 +1;
		while child < n:
			if child +1 < n and arr[child + 1] > arr[child]:
				child += 1
			if(arr[child] > t):
				arr[parent] = arr[child]
				parent = child
				child = parent*2 + 1
			else:
				break
		arr[parent] = t


def main(fileName):
	print(fileName)
	f =  open(fileName[1], 'r+')
	arr = []
	for num in f.readlines():
		arr.append(int(num.rstrip('\n')))
	heap(arr)
	name = '''result/selection.%s'''%(fileName[1].replace("instancias/",""))
	open(name, 'w')
	f = open(name, 'w+')
	for i in arr:
		f.write("%d\n"%(i))
if __name__ == "__main__":
	main(sys.argv)
