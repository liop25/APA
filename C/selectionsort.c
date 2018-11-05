#include <stdio.h>
#include <stdlib.h>

int * selection(int *arr, int size){
	int i,j,y, min, aux;
	for(i = 0; i<size-1; i++){
		min = i;
		for(j = i+1; j<size; j++){
			if(arr[min] > arr[j]) min = j;
		}
		aux = arr[min];
		arr[min] = arr[i];
		arr[i] = aux;
}

}

int main(int argc, char** argv){
	int size;
	scanf("%d", &size);
	int i;
	int * arr = (int*) malloc(size*sizeof(int));
	for(i = 0; i < size; i++) scanf("%d", &arr[i]);
	selection(arr, size);
	for(i = 0; i<size; i++) printf("%d\n", arr[i]);
	free(arr);
	return 0;
}

