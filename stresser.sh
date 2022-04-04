#!/bin/bash

for ((i=1; i<=10; i++))
do
    python3 PortRat.py "$i" &
done

