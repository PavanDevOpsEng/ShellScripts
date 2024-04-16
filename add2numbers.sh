#!/bin/bash

echo "Enter the number1 to add"

read number1

echo "Enter the number2 to add"

read number2

sum=$(($number1+$number2))

echo "The sum of 2 numbers are:: $sum"
