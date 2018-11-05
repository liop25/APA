#include <stdio.h>
#include <stdlib.h>

void heap(int a[], int n) {
   int i = n / 2, pai, filho, t;
   for (;;) {
      if (i > 0) {
          i--;
          t = a[i];
      } else {
          n--;
          if (n == 0) return;
          t = a[n];
          a[n] = a[0];
      }
      pai = i;
      filho = i * 2 + 1;
      while (filho < n) {
          if ((filho + 1 < n)  &&  (a[filho + 1] > a[filho]))
              filho++;
          if (a[filho] > t) {
             a[pai] = a[filho];
             pai = filho;
             filho = pai * 2 + 1;
          } else {
             break;
          }
      }
      a[pai] = t;
   }
}


int main(int argc, char** argv){
  int size;
  scanf("%d", &size);
  int i;
  int * arr = (int*) malloc(size*sizeof(int));
  for(i = 0; i < size; i++) scanf("%d", &arr[i]);
  heap(arr,size);
  for(i = 0; i<size; i++) printf("%d\n", arr[i]);
  free(arr);
  return 0;
}
