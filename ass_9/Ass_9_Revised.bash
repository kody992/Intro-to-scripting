#!bin/bash

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
    summation=0
    for i in ${prime_Array[@]}; 
    do
        let summation+=$i
    done
    echo "this is the sum $summation"
}



###################################################
#Q1
echo "
##### This Is Question 1 #####
"
array=()

for (( temp_Num=1; $temp_Num < 20; temp_Num++ ))
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

######################################################
#Q2

echo "
##### This Is Question 2 #####
"
for (( temp_Num=1; $temp_Num <= 20; temp_Num++ ))
do
    let array[temp_Num]=$RANDOM%10
done


echo "Unsorted: "${array[*]}
 
for (( i = 0; i<20; i++ ))
do
    
    for(( j = 0; j<${#array[*]}-i; j++ ))
    do
    
        if [[ ${array[j]} -lt ${array[$((j+1))]} ]]
        then
            temp=${array[j]}
            array[$j]=${array[$((j+1))]}  
            array[$((j+1))]=$temp
        fi
    done
done
echo "sorted Array" ${array[*]}


###########################################################
#Q3


echo "
##### This Is Question 3 #####
"

array=()
for (( temp_Num=1; $temp_Num <= 50; temp_Num++ ))
do
    array[temp_Num]=$temp_Num
done

echo ${array[*]}


#############################################################
#Q4

echo "
##### This Is Question 4 #####
"

Prime_finder ${array[*]}
##########################################################
#Q5

echo "
##### This Is Question 5 #####
"

odd_array=()
for temp_Num in $(seq 1 2 50)
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

#################################################################

even_array=()
for temp_Num in $(seq 2 2 50)
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
