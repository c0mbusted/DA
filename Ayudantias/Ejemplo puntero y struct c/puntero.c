#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() 
    int edad=20;
    int *pedad;
    int nueva_edad;

    pedad= &edad;//el puntero es igual a la memoria de edad osea 56789 en el ej

    printf("el valor del puntero es : %d ",*pedad);
}