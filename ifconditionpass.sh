#!/bin/bash

######

######

echo "Enter the user name"

read username

echo "Enter the password"

read -s password

if [ $[password]="password" ]

then 

echo "password matched and you are good to go"

else 

echo "please type the correct password"

fi