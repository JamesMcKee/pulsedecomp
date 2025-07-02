set terminal pngcairo font ",12" #solid
set output "filename.png"

unset key

set multiplot layout 2,1 rowsfirst

set label 1 "1484" at screen 0.8,0.98
set label 2 "J0218+4232" at screen 0.12,0.98


plot 'paas.txt' u ($1/2048):($2/0.000565703) w lines, \
'' u ($1/2048):($3/0.000565703) w lines

plot 'paas.txt' u ($1/2048):(($2-$3)/0.000565703) w lines

