#!/bin/bash
#Create arrays
if [[ $1 == "" ]]; then
	echo "No rom specified. First argument must be rom file."
	fail=true
fi
if [[ $2 == "" ]]; then
	echo "No arrays loaded. Second argument must be bash array from file."
	fail=true
fi
if [[ $fail == "true" ]]; then
	exit
fi
if [[ $3 == "" ]]; then
	output='extracted.zyx'
else
	output=$3
fi
declare address
declare length
counter=0
#Load list of addreses and lengths. You can create your own if you want to.
eval $(cat $2)
#Extract archives
while [[ $counter -ne $countto ]]; do
	echo "Extracting block" $counter "@ byte" ${address[$counter]} "(size" ${length[$counter]} "bytes)"
	dd if=$1 bs=1 skip=${address[$counter]} count=${length[$counter]} of=.block$counter.7z &> /dev/null
	let counter++
done
counter=0
echo "Extracted. Compiling file."
#Compile file in one
if [[ $(ls $output) ]]; then
	rm $output
fi
touch $output
while [[ $counter -ne $countto ]]; do
	echo "Adding block" $counter
	xz --format=lzma --decompress --stdout -Q .block$counter.7z >> $output
	let counter++
done
echo "Removing Archives"
rm .block*.7z
echo "Done."

