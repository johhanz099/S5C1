#include <iostream>
#include <cstdlib>
using namespace std;

/*
Inicializar variables
*/
int varInt = 5;
double varDoub = 5.05;


// Declarar funciones

/*
Funcion dividir variables
*/
double funcDiv(int x, double y);

/*
Funcion crear arreglo enteros aleatorios
*/
int arrAleat(int n, int min, int max);


int main(){
	cout << "La primera tiene un valor de " << varInt << " y la segunda variable tiene un valor de " << varDoub << "\n";
	cout << "El resultado es " << funcDiv(varInt,varDoub) << "\n";
	cout << arrAleat(10,0,10);
	cout << "\n";
	return 0;
}


/*
Calcular division entre dos numeros
*/
double funcDiv(int x, double y){
	return y/x;
}

/*
Crear arreglo
int n = tamaño
int min = límite inferior
int max = límite superior
*/
int *arrAleat(int n, int min, int max){
	int *array[n] = {0};
	for (int i = 0; i < n; i++){
		array[i] = i;
	}
	return array;
}



 



























