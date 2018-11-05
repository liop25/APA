#include <stdio.h>
#include <stdlib.h>

void merge(int *arr, int initial, int end) {
    int i, j, k, halfsize, *arrTemp;

    if(initial == end) return;

    halfsize = (initial + end ) / 2;
    merge(arr, initial, halfsize);
    merge(arr, halfsize + 1, end);

    i = initial;
    j = halfsize + 1;
    k = 0;
    arrTemp = (int *) malloc(sizeof(int) * (end - initial + 1));

    while(i < halfsize + 1 || j  < end + 1) {
        if (i == halfsize + 1 ) { 
            arrTemp[k] = arr[j];
            j++;
            k++;
        }
        else {
            if (j == end + 1) { 
                arrTemp[k] = arr[i];
                i++;
                k++;
            }
            else {
                if (arr[i] < arr[j]) {
                    arrTemp[k] = arr[i];
                    i++;
                    k++;
                }
                else {
                    arrTemp[k] = arr[j];
                    j++;
                    k++;
                }
            }
        }

    }

    for(i = initial; i <= end; i++) {
        arr[i] = arrTemp[i - initial];
    }
    free(arrTemp);

}

int main(int argc, char** argv){
	int size;
	scanf("%d", &size);
	int i;
	int * arr = (int*) malloc(size*sizeof(int));
	for(i = 0; i < size; i++) scanf("%d", &arr[i]);
	merge(arr,0, size-1);
	for(i = 0; i<size; i++) printf("%d\n", arr[i]);
	free(arr);
	return 0;
}

