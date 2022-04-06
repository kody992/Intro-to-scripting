#!/bin/bash
<<com
    Problem:2
    prints name and courses variables
com

var_Name="kody Crane"
Var_C1="DBMS"
Var_C2="CYBER"
Var_C3="STATS"
Var_C4="SCRIPTING"

echo -e "Name: $var_Name \nCourses: \n$Var_C1, $Var_C2, $Var_C3, $Var_C4"

<<com
    Problem:3
    prints all passed variables (Name and courses)
com

echo $@

<<com
    Problem:4
    prints pid
    prints all passed variables
com

echo process ID = $$
echo to print all passed  use \$* $*
echo to print all with [] use \$@ $@

<<com
    Problem:5
    create a random # between 0 and 100 and display grade based on number
com

let "stu_Grade=0 " "stu_Grade=$RANDOM % 101"

if [ $stu_Grade -ge 90 ]
then
echo Grade is $stu_Grade = A
elif [[ $stu_Grade -lt 90 && $stu_Grade -ge 80 ]]
then
echo Grade is $stu_Grade = B
elif [[ $stu_Grade -lt 80 && $stu_Grade -ge 70 ]]
then
echo Grade is $stu_Grade = C
elif [[ $stu_Grade -lt 70 && $stu_Grade -ge 60 ]]
then
echo Grade is $stu_Grade = D
else
echo Grade is $stu_Grade = fail
fi

<<com
    Problem:6
    mathematical opperations
com

num_1=7
num_2=3
num_3=4
num_4=14
num_5=121

let "sum=0" "sum=$num_1 + $num_2"
echo $num_1 + $num_2 \= $sum

let "difference=0" "difference=$num_3 - $num_2"
echo $num_3 - $num_2 \= $difference

echo $num_4 now incrimented to $((++num_4))

let "product=0" "product=$num_4 * $num_2"
echo $num_4 \* $num_2 = $product

echo $((num_5--)) now decremented to $num_5

let "dividend=0" "dividend=$num_5 / $num_4"
echo $num_5 \/ $num_4 = $dividend


<<com
    Problem:7
    read input and change 2 variables based on input and calculate gross salary
com

echo Enter your Basic Salary: 
read emp_Basic_Salary



if [ $emp_Basic_Salary -le 10000 ]
then
    echo less than or equal to 10000
    HRA_Percent=20
    DA_Percent=80
    echo HRA\% = $HRA_Percent
    echo DA\% = $DA_Percent
    
elif [[ $emp_Basic_Salary -ge 10001 && $emp_Basic_Salary -le 20000 ]]
then
    echo between 10001 and 20000
    HRA_Percent=25
    DA_Percent=90
    echo HRA\% = $HRA_Percent
    echo DA\% = $DA_Percent
    
elif [ $emp_Basic_Salary -ge 20001 ]
then
    echo greater than 20000
    HRA_Percent=30
    DA_Percent=95
    echo HRA\% = $HRA_Percent
    echo DA\% = $DA_Percent
fi


