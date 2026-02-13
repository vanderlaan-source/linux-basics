#!/bin/bash
echo "Qual é a tua idade?"
read "idade"
if [ $idade -ge 18 ]; then
echo "és maior de idade"
else
echo "és menor de idade"
fi
