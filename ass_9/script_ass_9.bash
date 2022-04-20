#!bin/bash
summation(){
    #array is not taking the sent prime array which should be in $1
    array=$1
    summation=0
    for i in ${array[@]}; 
    do
        let summation+=$i
    done
    echo $summation
}


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
    summation echo ${prime_Array[*]}

}



###################################################
#Q1
echo "
##### This Is Question 1 #####
"
array=()

for (( temp_Num=1; $temp_Num <= 20; temp_Num++ ))
do
    array[temp_Num]=$RANDOM
done


sorted_array=()
smallest=0
index=0
for (( temp_Num=0; $temp_Num < 20; temp_Num++ ))
do
    index=0
    smallest=${array[temp_Num]}
    
    for (( i=1; $i < ${#array[@]}; i++))
    do
        if [[ ${array[i]} -lt $smallest ]]
        then
            smallest=${array[i]}
            index=$i
        fi
    done
    sorted_array[temp_Num]=${array[index]}
    unset "array[index]"
done
echo "sorted       " ${sorted_array[*]}
echo "not sorted   " ${array[*]}

#Both 1 and 2 having same problem 
#it deletes the value then no longer adds and removes from respective arrays

######################################################
#Q2

echo "
##### This Is Question 2 #####
"
array=()

for (( temp_Num=1; $temp_Num <= 20; temp_Num++ ))
do
    array[temp_Num]=$RANDOM
done


sorted_array=()
largest=0
index=0
for (( temp_Num=0; $temp_Num < 20; temp_Num++ ))
do
    index=0
    largest=${array[temp_Num]}
    
    for (( i=1; $i < ${#array[@]}; i++))
    do
        if [[ ${array[i]} -lt $largest ]]
        then
            largest=${array[i]}
            index=$i
        fi
    done
    sorted_array[temp_Num]=${array[index]}
    unset "array[index]"
done
echo "sorted      " ${sorted_array[*]}
echo "not sorted  " ${array[*]}


#Both 1 and 2 having same problem 
#it deletes the value then no longer adds and removes from respective arrays

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
echo $summation

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
echo $summation



