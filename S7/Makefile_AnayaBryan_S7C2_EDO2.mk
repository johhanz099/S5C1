all: Euler2.png Runge2.png

Euler2.png : AnayaBryan_S7C2_EDO2.py euler2.dat
	python AnayaBryan_S7C2_EDO2.py
    
Runge2.png : AnayaBryan_S7C2_EDO2.py rk42.dat
	python AnayaBryan_S7C2_EDO2.py

euler2.dat : ./a.out
	./a.out

rk42.dat : ./a.out
	./a.out

leap_f.dat : ./a.out
	./a.out

./a.out : AnayaBryan_S7C2_EDO2.cpp
	g++ AnayaBryan_S7C2_EDO2.cpp