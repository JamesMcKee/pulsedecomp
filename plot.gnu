set terminal pngcairo font ",12" #solid
set output "filename.png"

unset key

set multiplot layout 2,1 rowsfirst

set label 1 "ZZ" at screen 0.8,0.98
set label 2 "WW" at screen 0.12,0.98


plot 'paas.txt' u ($1/XX):($2/YY) w lines, \
'' u ($1/XX):($3/YY) w lines

plot 'paas.txt' u ($1/XX):(($2-$3)/YY) w lines

