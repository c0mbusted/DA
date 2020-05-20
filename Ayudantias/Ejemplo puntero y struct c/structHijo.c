#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Persona{
    int id;
    char nombre[10];
    char apellido[10];
};

int main() {
    struct Persona hijo; //objeto persona
    hijo.id= 001;
    strcpy(hijo.nombre, "Pepito");
    strcpy(hijo.apellido, "Gomez");

    printf("El detalle del hijo es: \n");
    printf("El id es: %d",hijo.id);
    printf("Nombre: %s",hijo.nombre);
    printf("Apellido: %s",hijo.apellido);
}
