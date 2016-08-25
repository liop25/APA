import sys

def merge(arr):
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge(lefthalf)
        merge(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1

def main(fileName):
    print(fileName)
    f =  open(fileName[1], 'r+')
    arr = []
    for num in f.readlines():
        arr.append(int(num.rstrip('\n')))
    merge(arr)
    name = '''result/merge.%s'''%(fileName[1].replace("instancias/",""))
    open(name, 'w')
    f = open(name, 'w+')
    for i in arr:
        f.write("%d\n"%(i))

if __name__ == "__main__":
    main(sys.argv)
