## bc only truncate the input not the rounding of number
read inp
printf "%.3f\n" $(echo "$inp" | bc -l)

