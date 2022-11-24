#include "declarations.h"

int main(){
    //Datos Sol
    double mS = 333000.0;
    //Datos Tierra
    double mt = 1.0;
    double rt = 1.0;
    double wt = sqrt(G*mS*pow(rt, -3));
    double vt = wt*rt; //Orbita circular w*r 
    //Datos Jupiter
    double mj = 317.81;
    double rj = 5.203;
    double wj = sqrt(G*mS*pow(rj, -3));
    double vj = wj*rj; //Orbita circular w*r 
    //Datos Sonda
    double ms = 4.225E-22;
    double rs = rt + pow(mS, -2/5);
    double v0s = sqrt((2*G*mS*rj)/(rs*(rs+rj))); //Velocidad de transicion
    
    // double rs = rt + 4.25875E-5;
    // double v0s = 0.783; //Velocidad de transicion
    //---(x0,y0,z0,Vx0,Vy0,Vz0,m)
    Cuerpo Sol(0,0,0,0,0,0,mS);
    Cuerpo Tierra(rt,0,0,0,vt,0,mt);
    Cuerpo Jupiter(1.31619,5.03377,0,-0.2219,0.058,0,mj);
    Cuerpo Sonda(rs,0,0,0,v0s,0, ms);
    cuerpos N = {Sonda, Tierra, Jupiter, Sol};
    //Fuerza inicial
    force(N);
    
    Jupiter.start_leap_frog(DT);
    Sonda.start_leap_frog(DT);
    trans_galileo(N);
    print(N,0.0);

    double time = 0.0;
    for(int ii = 0; ii < NSTEPS; ++ii){
        force(N);
        trans_galileo(N);
        print(N, DT*ii);
        time = DT*ii;
        //if(gassist(N, rj)){break;}
    }
    // double phi = acos(N[0].R.x/rj)-wj*time;
    // std::cout << phi;

    return 0;
}