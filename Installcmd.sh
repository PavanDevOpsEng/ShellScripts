#!/bin/bash
USERID=$(id -u)
TIMESTAMP=$(date +%F-%H-%M-%S)

VALIDATE ()
{
    if [ $1 -ne 0 ]

    then 
    ehco "$2..Failure"
    exit 1 

    else 
    echo "$2..Success"

    fi
}


if [ $USERID -ne 0 ]
then 
echo "You are not a super user" 
exit 1
else 

echo "You are a super user.."

fi

for i in $@
do 

dnf install $i -y

VALIDATE $? "Installing $i"

done