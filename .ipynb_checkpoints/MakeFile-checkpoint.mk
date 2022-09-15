all: fig1_dataRand.png fig2_dataImp.png

fig1_dataRand.png: AnayaBryan_S5C2_repasoC.cpp AnayaBryan_S6C1_Graf.py arrAleat.dat
    g++ AnayaBryan_S5C2_repasoC.cpp
    python AnayaBryan_S6C1_Graf.py
    
fig2_dataImp.png: AnayaBryan_S5C2_repasoC.cpp AnayaBryan_S6C1_Graf.py arrImp.dat
    g++ AnayaBryan_S5C2_repasoC.cpp
    python AnayaBryan_S6C1_Graf.py    