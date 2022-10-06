#include<iostream>
#include<fstream>
#include<vector>

using namespace std;
typedef vector<double> vec; //nombre para vector
// initialization vec(size, value);

/*
Inicializar método ecuación de onda
*/
void eqOnda(float c, float L, float h, float N);


/*
Inicializar método Función de condición inicial
Crea el arreglo (vector) con los valores que representan la condición inicial
*/
void FcondInicial(float L, float h, float N);


/*
MAIN /////////////////////////7
*/
int main(void){
	float c = 300; // velocidad de propagación
    float h = 0.1; // altura inicial de la cuerda
	float L = 2; // longitud de la cuerda
    float N = 100; // Cantidad de divisiones discretas - N par
    
    // Prueba implementar funcion condición inicial
    FcondInicial(L,h,N); //Funcionó correctamente
    
    //vec condInicialx = FcondInicial(L,h,N)[0];
    //vec condInicialy = FcondInicial(L,h,N)[1];
    
	return 0;
}

/*
Método ecuación de onda
*/
void eqOnda(float c, float L, float h, float N){
    // Crear la condición inicial
    float m = 2*h/L; // pendiente
    float dx = L/N; // avance discreto en x
    vec x_cond(N,0); // Inicializar vector en x
    vec y_cond(N,0); // --------------------- y
    float b = (2*h + m*L)/2; // punto de corte y_2
    
    for(int i = 0; i <= N; i++){
        x_cond[i] = dx * i; // avance en x
        if(x_cond[i] <= L/2){ // arreglo y_1
            y_cond[i] = x_cond[i] * m;
        }
        else if(x_cond[i] > L/2){ // arreglo y_2
            y_cond[i] = x_cond[i] * (-m) + b;
        }
    }
    
    
}


/*
Método Función de condición inicial
*/
void FcondInicial(float L, float h, float N){
    float m = 2*h/L; // pendiente
    float dx = L/N; // avance discreto en x
    vec x(N,0); // Inicializar vector en x
    vec y(N,0); // --------------------- y
    float b = (2*h + m*L)/2; // punto de corte y_2
    
    // Open data
    ofstream outfile;
    outfile.open("Finicial.dat");
    
    for(int i = 0; i <= N; i++){
        x[i] = dx * i; // avance en x
        if(x[i] <= L/2){ // arreglo y_1
            y[i] = x[i] * m;
            outfile << x[i] << "," << y[i] << endl;
        }
        else if(x[i] > L/2){ // arreglo y_2
            y[i] = x[i] * (-m) + b;
            outfile << x[i] << "," << y[i] << endl;
        }
    }
    // Close data
    outfile.close();
    //return x,y;
}
    
    
