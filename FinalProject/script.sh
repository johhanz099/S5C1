#!/bin/bash
g++ simul.cpp main.cpp
./a.out > data.dat
python graficas.py
echo Done!