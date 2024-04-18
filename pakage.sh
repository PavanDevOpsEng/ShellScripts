#!/bin/bash
USERID=$(id -u)
TIMESTAMP=$(date +%F-%H-%M-%S)

if [ $USERID -ne 0 ]
then 
echo "You are not a super user" 
exit 1
else 

echo "You are a super user.."

fi

dnf install mysql -y

if [ $? -ne 0 ]
then 
echo "Installation failed"
exit 1

else
echo "Installtion sucess"
fi 