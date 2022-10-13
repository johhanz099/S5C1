#include<iostream>
#include<fstream>
#include<vector>

using namespace std;
typedef vector<double> vec;

/*
Inicializar ecuación de difusión
*/
void eqDifusion(float L, float nu);

/*
Inicializar condición inicial
*/
void condInicial();


/*
Inicializar main
*/
int main(void){
	float L = 100; // Largo y ancho de la placa
	float nu = 0.0001; // Coeficiente de difusión
	float dx = 1; // avance en x
	

	// Prueba arrays 2d
	float arr[2][2];
	
	//*	
	for (int i=0; i<2; i++){
		for (int j=0; j<2; j++){
			arr[i][j] = 0;
			cout << arr[i][j] << " ";	
		}
		cout << endl;
	}
	//*/
	cout << sizeof(arr) << endl;


	return 0;
	
}

