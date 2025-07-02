#! /bin/bash

#archive that components will be fit for
archive=$1

#get the maximum amplitude of the input profile
max_amp=$(pdv -FTp -A $archive | grep -v File | grep -v MJD | sort -gk4,4 | tail -n1 | awk '{print $4}')

#define the maximum number of components to fit and the number of trials for each number of components
n_components=14
n_trials=100


for components in `seq 1 $n_components`; do
	for trial in `seq 1 $n_trials`; do
		echo "log height" > paas.m
		python3.12 generate_input.py -f $max_amp -n $components >> paas.m 
		paas -L -r paas.m $archive -f
		if [ -e paas.txt ]; then
			chisq=$(cat paas.txt | head -n1 | awk '{print $7}')
			echo $(cat paas.m | grep -v log) "$chisq" >> output_"$components".dat
		fi
		rm paas.std
		rm paas.m
		rm paas.txt
	done
done



