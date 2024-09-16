#!/bin/bash

ageinput=$1
if [ $ageinput -lt 13 ]
then
	echo "child"
elif [ $ageinput -lt 20 ]
then
	echo "teen"
elif [ $ageinput -lt 65 ]
then
	echo "adult"
elif [ $ageinput -gt 65 ]
then
	echo "elderly"
fi
