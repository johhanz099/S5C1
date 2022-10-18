#include<iostream>
#include<fstream>
#include<vector>

using namespace std;
typedef vector<double> vec;

/*
Inicializar ecuación de difusión
*/
//void eqDifusion(float L, float nu);

/*
Inicializar condición inicial
*/
//void condInicial(float L, float nu);


/*
Inicializar main
*/
int main(){
	int L = 10; // Largo y ancho de la placa
	float nu = 0.0001; // Coeficiente de difusión
	float dx = 1; // avance en x
	
    
    // Open data
    ofstream outfile;
    outfile.open("data2d_Difusion.dat");
    

	// Arrays 2d Condición inicial
	float arrInic[L][L];
	
	//* Condición inicial
	for (int i=0; i<L; i++){
		for (int j=0; j<L; j++){
            if ((i >= 2 && i <=4) && (j >= 4 && j <= 6)){
                arrInic[i][j] = 100;
                outfile << arrInic[i][j] << ",";
            }
			else{
                arrInic[i][j] = 50;
                outfile << arrInic[i][j] << ",";
                
            }
		}
	}
    // Los datos completos de la temperatura se guardan en una sola fila
    outfile << endl;
    
    // /*
    
    // Arr present
    float arrPres[L][L];
    float t_max = 0; // habrían 2500 filas de datos
    float dt = 1; //dt = 1 sg
    int LFrontera = L-1; // Para no cambiar valores en la frontera
    for (int t = 1; t<=t_max; t += dt){ 
        
        for (int i = 1; i<LFrontera; i++){
            for (int k = 1; k<LFrontera; k++){
                float p2 = nu*dt/(dx*dx)*(arrInic[i+1][k] - 2*arrInic[i][k] + arrInic[i-1][k]);
                float p3 = nu*dt/(dx*dx)*(arrInic[i][k+1] - 2*arrInic[i][k] + arrInic[i][k-1]);
                arrPres[i][k] = arrInic[i][k] + p2 + p3;
                outfile << arrPres[i][k] << ",";
            }
        }
        outfile << endl;
        
        // Cambiar presente con pasado
        // Sin cambiar valores en la frontera
        // Tuve que hacerlo así ya que no es posible <<arrInic = arrPres>>
        for (int i=1; i<LFrontera; i++){
            for (int j=1; j<LFrontera; j++){
                arrInic[i][j] = arrPres[i][j];
            }
        }
    }
    
     // */

    // Close data
    outfile.close();
    // Los datos quedaron en t_max filas. Cada fila correspone a:
    // t = 0 s
    // t = 1 s
    // ...
    // t = t_,max s
    // Cada columna separada por espacios
	return 0;
	
}

