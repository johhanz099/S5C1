#include<iostream>
#include<fstream>
#include<vector>

using namespace std;
typedef vector<double> vec; //nombre para vector
// initialization vec(size, value);

/*
Inicializar método ecuación de onda
*/
void eqOnda(float c, float L, float h, float N, vec & xInic, vec & yInic);


/*
Inicializar método Función de condición inicial
Crea el arreglo (vector) con los valores que representan la condición inicial
*/
void FcondInicial(float L, float h, float N, vec & xInic, vec & yInic);


/*
MAIN /////////////////////////7
*/
int main(void){
	float c = 300; // velocidad de propagación
    float h = 0.1; // altura inicial de la cuerda
	float L = 2; // longitud de la cuerda
    float N = 100; // Cantidad de divisiones discretas - N par
    float tf= 0.1; // tiempo final
    
    // Prueba implementar funcion condición inicial
    vec xInic(N,0);
    vec yInic(N,0);
    FcondInicial(L,h,N,xInic,yInic); //Funcionó correctamente
    
    //vec condInicialx = FcondInicial(L,h,N)[0];
    //vec condInicialy = FcondInicial(L,h,N)[1];
    
	return 0;
}

/*
Método ecuación de onda
*/
void eqOnda(float c, float L, float h, float N, vec & xInic, vec & yInic, float tf){
    float dx = L/N;
    float dt = 0.5*dx/c;
    float k  = c*c*dt*dt*dx*dx;
    vec t(N,0);
    vec upast = yInic;
    int ntmax = tf/dt;
    
    //Open data
    
    for (int j = 0; j <= ntmax; j++){
        t[j] = dt * j; // avance en t
        
        for (int i = 0, i <= N, i++){
            u[j] = 
            
    }
    
    
    
    
}


/*
Método Función de condición inicial
*/
void FcondInicial(float L, float h, float N, vec & xInic, vec & yInic){
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
    xInic = x;
    yInic = y;
}
    
    
