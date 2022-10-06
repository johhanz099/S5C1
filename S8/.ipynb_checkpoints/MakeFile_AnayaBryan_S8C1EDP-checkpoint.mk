all: Finicial.png

Finicial.png : AnayaBryan_S8C1EDP.py Finicial.dat
    python AnayaBryan_S8C1EDP.py
    
Finicial.dat : a.out
    ./a.out
    
a.out : AnayaBryan_S8C1EDP.cpp
    g++ AnayaBryan_S8C1EDP.cpp