#include<iostream>
#include<cmath>
#include<fstream>
#include<vector>

typedef std::vector<double> vec; //nombre para vector

void EDO(vec & y, double x);
void EDO2(vec & y, double x);
template <class deriv> //Reciben como parametro la EDO a solucionar
void Euler(deriv edo, vec & y, double x, int stop, double dx);
template <class deriv>
void rk4(deriv edo, vec & y, double x, int stop, double dx);
template <class deriv>
void leapfrog(deriv edo,vec & y, double x, int stop, double dx);
	
const double k = 50.0;
const double m = 0.2;
const double b = 0.08;

int main(void){
	int iter = 10000;
	double h = 0.001;
	double Xin = 0.0;
	
	//Vector con componente de posicion, velocidad y aceleracion 
	vec Y(3, 0.0); 
		
	Euler(EDO2, Y, Xin, iter, h);
	rk4(EDO2, Y, Xin, iter, h);
	leapfrog(EDO2, Y, Xin, iter, h);

	return 0;
}

//EDO oscilador armonico
void EDO(vec & y, double x){
	y[2] = -(k/m)*y[0]; 
}
//EDO oscilador armonico amortiguado
void EDO2(vec & y, double x){
	y[2] = -(k/m)*y[0]-b*y[1]; 
}

//Metodo de euler segundo orden
template <class deriv>
void Euler(deriv edo, vec & y, double x, int stop, double dx){
	// Crear archivos:
	std::ofstream outfile;
	outfile.open("euler2.dat");

	//Condiciones iniciales
	y[0] = 0.1;
	y[1] = 0.0;
	int N = y.size()-1;
	for(int ii = 0; ii < stop; ii++){
		x += dx;
		//Escribir datos
		edo(y, x);
		for(int jj = 0; jj < N; jj++){
			y[jj] = y[jj] + dx*y[jj + 1];
		}
		outfile << x << "," << y[0] << "," << y[1] << "\n";
	}
	outfile.close();
}

//Metodo Runge-Kutta segundo orden 
template <class deriv>
void rk4(deriv edo, vec & y, double x, int stop, double dx){
	// Crear archivos:
	std::ofstream outfile;
	outfile.open("rk42.dat");
	//Condiciones iniciales
	y[0] = 0.1;
	y[1] = 0.0;
	int N = y.size()-1;
	vec k1(N), k2(N), k3(N), k4(N), yn(N);

	for(int ii = 0; ii < stop; ii++){
		x += dx;
		//k1
		edo(y, x);
		for(int jj = 0; jj < N; jj++){
			k1[jj] = dx*y[jj + 1];
		}

		//yn para k2
		for ( int jj = 0; jj < N; jj++){
			yn[jj] = y[jj] + k1[jj]/2;
		}
		
		//k2
		edo(yn, x);
		for(int jj = 0; jj < N; jj++){
			k2[jj] = dx*yn[jj + 1];
		}

		//yn para k3
		for ( int jj = 0; jj < N; jj++){
			yn[jj] = y[jj] + k2[jj]/2;
		}

		//k3
		edo(yn, x);
		for(int jj = 0; jj < N; jj++){
			k3[jj] = dx*yn[jj + 1];
		}

		//yn para k4
		for ( int jj = 0; jj < N; jj++){
			yn[jj] = y[jj] + k3[jj];
		}

		//k4
		edo(yn, x);
		for(int jj = 0; jj < N; jj++){
			k4[jj] = dx*yn[jj + 1];
		}

		//Escribir datos
		for(int jj = 0; jj < N; ++jj) {
      	y[jj] = y[jj] + (k1[jj] + 2*k2[jj] + 2*k3[jj] + k4[jj])/6.0;
    	}
		outfile << x << "," << y[0] << "," << y[1] << "\n";
	}	
	outfile.close();
}

//Metodo Leap-Frog
template <class deriv>
void leapfrog(deriv edo, vec & y, double x, int stop, double dx){
	// Crear archivos:
	std::ofstream outfile;
	outfile.open("leap_f.dat");
	//Condiciones iniciales
	y[0] = 0.1;
	y[1] = 0.0;
	int N = y.size()-1;

	edo(y, x);
	y[1] = y[1]+0.5*dx*y[2];
	for(int ii = 0; ii < stop; ii++){
		x += dx;
		//Escribir datos
		for(int jj = 0; jj < N; jj++){
			edo(y, x);
			y[jj] = y[jj] + dx*y[jj + 1];
		}
		outfile << x << "," << y[0] << "," << y[1] << "\n";
	}
	outfile.close();
}