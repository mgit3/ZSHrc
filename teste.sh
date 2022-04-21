#!/usr/bin/env bash

echo Olá qual é seu primeiro nome?;
read a;
echo Bem-Vindo Sr./Sra. $a, Gostaria de dizer seu último nome?;
read b;
echo Obrigado Sr./Sra. $a $b por dizer seu nome;
sleep 3
echo
echo "*******************"
echo
echo 'Usando shell script podemos fazer somas sabia?'
echo
sleep 3
echo -e 'Por exemplo 243 mais 425 podem ser somados aqui e podemos ler o total da soma.\nQue seria?'
echo
sleep 3
N1=243
N2=425
TOTAL=$(($N1+$N2))
echo Seria: $TOTAL
sleep 3
echo
echo Mr./Mrs. $b, agora é hora de nos despedirmos, por enquanto.
echo
