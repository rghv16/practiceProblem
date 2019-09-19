read l
read h
read b
if [ $l = $h -a $l = $b ]
then
    echo "EQUILATERAL"
elif [ $l != $h -a $l != $b -a $h != $b ]
then
    echo "SCALENE"
else
    echo "ISOSCELES"
fi
