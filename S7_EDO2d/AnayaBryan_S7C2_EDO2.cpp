#include<iostream>
#include<cmath>
#include<fstream>
#include<vector>

using namespace std;
typedef vector<double> vec; //nombre para vector
// initialization vec(size, value);

void EDO(vec & y, vec & dy, double x);
void Euler(vec & y, vec & dy, double x, int stop, double dx);
template <class deriv>
void rk4(deriv edo, vec & y, double x, int stop, double dx);
	
const double k = 50.0;
const double m = 0.2;

int main(void){
	int iter = 10000;
	double h = 0.001;
	double Xin = 0.0;
	vec Y(2, 0.0);
	vec V(2, 0.0);
		
	Euler(Y, V, Xin, iter, h);
	
	return 0;
}

void EDO(vec & y, vec & dy, double x){
	dy[0] = y[1];
	dy[1] = -(k/m)*y[0]; 
}

void Euler(vec & y, vec & dy, double x, int stop, double dx){
	// Crear archivos:
	ofstream outfile;
	outfile.open("euler2d.dat");

	//Condiciones iniciales
	y[0] = 0.1;
	y[1] = 0.0;
	int N = y.size();
	for(int i = 0; i < stop; i++){
		x += dx;
		EDO(y, dy, x);
		for(int j = 0; j < N; j++){
			y[j] = y[j] + dx*dy[j];
		}
		outfile << x << "," << y[0] << "," << y[1] << endl;
	}
	outfile.close();
}

/*
Runge kuta 4
*/
template <class deriv>
void rk4(deriv edo, vec & y, double x, int stop, double dx){
	// Crear archivos:
	ofstream outfile;
	outfile.open("rk42.dat");
	//Condiciones iniciales
	y[0] = 0.1;
	y[1] = 0.0;
	int N = y.size() - 1;
	vec k1(N), k2(N), k3(N), k4(N), yn(N);

	for(int i = 0; i < stop; i++){
		x += dx;
		//k1
		edo(y, x);
		for(int j = 0; j < N; j++){
			k1[j] = dx*y[j + 1];
		}

		//yn para k2
		for ( int j = 0; j < N; j++){
			yn[j] = y[j] + k1[j]/2;
		}
		
		//k2
		edo(yn, x);
		for(int j = 0; j < N; j++){
			k2[j] = dx*yn[j + 1];
		}

		//yn para k3
		for ( int j = 0; j < N; j++){
			yn[j] = y[j] + k2[j]/2;
		}

		//k3
		edo(yn, x);
		for(int j = 0; j < N; j++){
			k3[j] = dx*yn[j + 1];
		}

		//yn para k4
		for ( int j = 0; j < N; j++){
			yn[j] = y[j] + k3[j];
		}

		//k4
		edo(yn, x);
		for(int j = 0; j < N; j++){
			k4[j] = dx*yn[j + 1];
		}

		//Escribir datos
		for(int j = 0; j < N; ++j) {
      	y[j] = y[j] + (k1[j] + 2*k2[j] + 2*k3[j] + k4[j])/6.0;
    	}
		outfile << x << "," << y[0] << "," << y[1] << endl;
	}	
	outfile.close();
}