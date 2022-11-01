/*
Ejercicio2
1) Genere un arreglo A con 6 números aleatorios entre 10 y 16. Genere un arreglo B con 6 numeros aleatorios entre 5 y 13. Imprima en consola y de manera clara ambos arreglos.\\  

Nota:  Para esto use srand() y rand(). 
Ejemplo: para generar un numero iRand entre 0 y 9:
srand(time(0))
int iRand = rand() % 10;
ver tambien: https://stackoverflow.com/questions/4621191/c-random-number-1-9

Su codigo debe:\\
2) Imprimir el mensaje "elijo A" si TODOS los elementos del arreglo A son mayores que TODOS los elementos del arreglo B.\\
3) Imprimir "elijo B" si al menos uno de los elementos de A es mayor o igual que alguno de los elementos de B y no se cumple la condición del punto 2).

*/

#include <fstream>
#include <iostream>
#include <math.h>
#include <stdio.h>
#include<time.h>
using namespace std;

int main(){
    // Generar arreglos según las instrucciones
    int n = 6;
    int A[n] = {};
    int B[n] = {};
    for (int i = 0; i < n; i++){
        A[i] = 10 + rand()%(16-10);
        B[i] = 5  + rand()%(13-5);
        }
    // Imprime arreglo A
    cout << "El arreglo A es: ";
    for (int i = 0; i < n; i++){
        cout << A[i] << ' ';
    }
    cout << '\n';
    // Imprime arreglo B
    cout << "El arreglo B es: ";
    for (int i = 0; i < n; i++){
        cout << B[i] << ' ';
    }
    cout << '\n';
    
    // Elegir entre ambos arreglos según las condiciones dadas
    
    // Primero
    // Encontrar máximo de B y mínimo de A para testear opcion 2
    int prueba = 0;
    int Amin = 20;
    int Bmax = 0;
    for(int i=0; i<n; i++){
        if(B[i] > Bmax){
            Bmax = B[i];
        }
        if(A[i] < Amin){
            Amin = A[i];
        }
    }
    
    if (Amin > Bmax){
        prueba = 1; // Cond(2) si y solo si todos los elementos de A son mayores a todos los elementos de B
    }
    
    
    // Testear opcion 3
    for(int i = 0; i<n; i++){
        for(int j = 0; j<n; j++){
            if(prueba == 0 && A[i] >= B[j]){ //si no se cumple Cond(2) y alguno de A es >= a alguno de B
                prueba = 2;
            }
        }
    }
    if (prueba == 1){
        cout << "Elijo A" << endl;
        }
    else if (prueba == 2){
        cout << "Elijo B" << endl;
        }
    else if(prueba == 0){
        cout << "No se pudo decidir" << endl;
    }
    
    
    return 0;
}