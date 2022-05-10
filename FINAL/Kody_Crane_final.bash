#!/bin/bash

Prime_finder(){
    prime_Array=()
    array=$1
    flag=1
    for i in ${array[@]};
    do
        flag=1
        if [[ $i -gt 1 ]]
        then
            for ((num=2; $num < $i; num++))
            do
                check=$i%$num
                if [[ $check -eq 0 ]]
                then
                    flag=0
                fi
            done
            if [[ flag -eq 1 ]]
            then
                prime_Array+=($i)
            fi
        fi
    done
    echo ${prime_Array[*]}
}

math_operations(){
    num1=$1
    num2=$2
    addition=0
    multiplication=0
    subtraction=0
    division=0
    exponent=0
    let addition=$num1+$num2
    let multiplication=$num1*$num2
    let subtraction=$num1-$num2
    let division=$num1/$num2
    let exponent=$num1**$num2
}

<<com
question 7
com
echo "--------Q7--------"
array=()
for (( temp_Num=0; $temp_Num <= 900; temp_Num++ ))
do
    let array[temp_Num]=($temp_Num+100)
done
Prime_finder ${array[*]}


<<com
question 8
com
echo "--------Q8--------"

odd_array=()
for temp_Num in $(seq 51 2 101)
do
    odd_array+=($temp_Num)
done

summation=0
for i in ${odd_array[@]}; 
do
  let summation+=$i
done

echo ${odd_array[*]}
echo "the sum of the odd array is: $summation"
######################################################
even_array=()
for temp_Num in $(seq 50 2 100)
do
    even_array+=($temp_Num)
done

summation=0
for i in ${even_array[@]}; 
do
  let summation+=$i
done

echo ${even_array[*]}
echo "the sum of the even array is: $summation"

<<com
question 9
com

echo "--------Q9--------"
array=()
for (( temp_Num=1; $temp_Num <= 20; temp_Num++ ))
do
    let array[temp_Num]=$RANDOM%10
done

echo "Unsorted: "${array[*]}
 
for (( i = 0; i<20; i++ ))
do
    for(( j = 0; j<${#array[*]}-i; j++ ))
    do
        if [[ ${array[j]} -gt ${array[$((j+1))]} ]]
        then
            temp=${array[j]}
            array[$j]=${array[$((j+1))]}  
            array[$((j+1))]=$temp
        fi
    done
done
echo "sorted Array" ${array[*]}


<<com
question 10
com

echo "--------Q10--------"
echo "enter 2 numbers"
read num1
read num2

while [ $num2 == 0 ]
do
    echo "enter non 0 for num 2"
    read num2
done
math_operations $num1 $num2
echo "addition " $addition
echo "multiplication " $multiplication
echo "subtraction " $subtraction
echo "division " $division
echo "exponent " $exponent
