#include <stdio.h>
#include <stdlib.h>

void quick(int * arr, int initial, int end){
	int i = initial, j = end, pivot, aux;
	pivot = arr[(initial + end)/2];
	while(i<j){
		while(arr[i] < pivot) i++;
		while(arr[j] > pivot) j--;
		if(i <= j){
			aux = arr[i];
			arr[i++] = arr[j];
			arr[j--] = aux;
		}
	}
	if(j > initial) quick(arr, initial, j);
	if(i < end) quick(arr, i, end);

	return;
}

int main(int argc, char** argv){
	int size;
	scanf("%d", &size);
	int i;
	int * arr = (int*) malloc(size*sizeof(int));
	for(i = 0; i < size; i++) scanf("%d", &arr[i]);
	quick(arr,0, size-1);
	for(i = 0; i<size; i++) printf("%d\n", arr[i]);
	free(arr);
	return 0;
}