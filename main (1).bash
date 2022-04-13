
#!/bin/bash

#Question 1: Print numbers from 1 to 15 using while, until, for. 

temp_Num=1
echo "While Loop"
while [ $temp_Num -le 15 ]
do
    echo $temp_Num
    let temp_Num+=1
done

temp_Num=1
echo "Until Loop"
until [ $temp_Num -eq 16 ]
do
    echo $temp_Num
    let temp_Num+=1
done


echo "For Loop"
for (( temp_Num=1; $temp_Num <= 15; temp_Num++ ))
do
    echo $temp_Num
done

#Question 2: Find summation of numbers from 20 to 40 using while, until, for

temp_Num=20
temp_Sum=0
echo "While Loop"
while [ $temp_Num -le 40 ]
do
    let temp_Sum+=temp_Num++
done
echo $temp_Sum

temp_Num=20
temp_Sum=0
echo "Until Loop"
until [ $temp_Num -eq 41 ]
do
    let temp_Sum+=temp_Num++
done
echo $temp_Sum

temp_Sum=0
echo "For Loop"
for (( temp_Num=20; $temp_Num <= 40; temp_Num++ ))
do
    let temp_Sum+=temp_Num
done
echo $temp_Sum

#Question 3: Using while, until, for conditions print prime numbers less than 50
check_Num=1
echo 2
while [ $check_Num -le 50 ] #can be exchenged with- until [ $check_Num -gt 50 ]
do
    for (( temp_Num=2; temp_Num < check_Num; temp_Num++))
        do
            if [[ $(($check_Num%$temp_Num)) -eq 0 ]]
            then
                is_Prime=0
                break
            fi
            is_Prime=1
            
        done
        if [[ is_Prime -eq 1 ]]
            then
                echo $check_Num
            fi
    let check_Num+=1
done

<<com
Question 4: Take a input from users, 
if the user provides 
“corpus” print “Texas A&M University Corpus Christi”, 

if user provides 
“Kingsville” print “Texas A&M University Kingsville”, 

if user provides
“commerce” print “Texas A&M University Commerce”. 

If none of the above, then print 
“Texas A&M
University”
com

echo "enter A&M University"
read uni_Name

case $uni_Name in
    "corpus"|"Corpus")
        echo "Texas A&M University Corpus Christi"
        ;;
    "kingsville"|"Kingsvile")
        echo "Texas A&M University Kingsville"
        ;;
    "commerce"|"Commerce")
        echo "Texas A&M University Commerce"
        ;;
    *)
        echo "Texas A&M University"
        ;;
esac


#bonus fixed code

var_test=21

echo $var_test

if [[ $var_test -ge 1 && $var_test -le 10 ]]
then
    echo "between 1 to 10"
elif [[ $var_test -ge 11 && $var_test -le 20 ]]
then
    echo "between 11 to 20"
elif [[ $var_test -gt 20 ]]
then
    echo "Greater than 20"
else
    echo "less than 1"
fi



