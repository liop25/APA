#include <stdio.h>
#include <stdlib.h>

int * insertion(int *arr, int size){
	int i, j, key;
	for(int i = 1; i < size; i++){
		key = arr[i];
		for(j = i-1; j>=0 && key < arr[j];j--){
			arr[j+1] = arr[j];
		}
		arr[j+1] = key;
	}
}

int main(int argc, char** argv){
	int size;
	scanf("%d", &size);
	int i;
	int * arr = (int*) malloc(size*sizeof(int));
	for(i = 0; i < size; i++) scanf("%d", &arr[i]);
	insertion(arr,size);
	for(i = 0; i<size; i++) printf("%d\n", arr[i]);
	free(arr);
	return 0;
}
