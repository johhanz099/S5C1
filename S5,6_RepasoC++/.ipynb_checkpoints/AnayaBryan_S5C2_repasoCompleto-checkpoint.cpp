#include <iostream>
#include <cstdlib>
#include <cmath>
#include <fstream>
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
Función potenciación
*/
double funcPot(float mivarflotante, int mivarentera);

/*
Funcion crear arreglo enteros aleatorios
int arrAleat(int n, int min, int max);
*/

/*
Funcion buscar minimo de un arreglo
*/
int minArr(int arr[], int n, int max);

int main(){
	// Open file
	ofstream outfile;
	outfile.open("arrAleat.dat");
	

	cout << "La primera variable tiene un valor de " << varInt << " y la segunda variable tiene un valor de " << varDoub << "\n";
	cout << "El resultado de dividir la segunda entre la primera es: " << funcDiv(varInt,varDoub) << "\n";
    
	// Arreglo numeros aleatorios [0,900]
	int n = 300;
    int arrRand[n] = {};
    for (int i = 0; i < n; i++){
        arrRand[i] = rand() % 901;
        }
    cout << "El arreglo es: ";
    for (int i = 0; i < n; i++){
        cout << arrRand[i] << ' ';
		outfile << arrRand[i] << '\n';
    }
	// Close data 1
	outfile.close();
		

	// Arreglo con impares menos que 800
	ofstream outfile;
	outfile.open("arrImp.dat");
	int umbral = 800; 
	outfile << 1 << '\n';
	for (int i = 0; i < n; i++){
		if (arrRand[i] < umbral && arrRand[i]%2 == 0){
			outfile << arrRand[i] << '\n';
		}
	}

	// Close
	outfile.close();
	


	

	cout << '\n';
    cout << "El quinto elemento del arreglo de números aleatorios es: " << arrRand[5-1] << '\n';
    cout << "La longitud del arreglo es: " << sizeof(arrRand)/sizeof(int) << '\n';
    cout << "17.5 elevado a 5 da como resultado: " << funcPot(17.5,5) << '\n';
    cout << "El mínimo del arreglo anteriormente creado es: " << minArr(arrRand,n,900) << '\n';
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

int *arrAleat(int n, int min, int max){
	int arr[n] = {};
	for (int i = 0; i < n; i++){
		arr[i] = i;
	}
	return arr;
}
*/

/*
Método potenciación
*/
double funcPot(float mivarflotante, int mivarentera){
    return pow(mivarflotante, mivarentera);
}

/*
Método para encontrar el mínimo de un arreglo de enteros
*/
int minArr(int arr[],int n, int max){
    //int n = sizeof(arr)/sizeof(int);
    int ctr = max;
    for (int i=0; i<n; i++){
        if (arr[i] < ctr){
            ctr = arr[i];
        }
    }
    return ctr;
}





 



























