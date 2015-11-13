#!/bin/bash

srcdir=$(dirname $0)

outfile1=$(mktemp)
outfile2=$(mktemp)

cleanup()
{
	rm -f $outfile1 $outfile2
}

trap cleanup EXIT

test_1()
{
	arki-scan --inline ${srcdir}/test.grib1 | ${srcdir}/singlepoint 10 2>/dev/null && return 1 || return 0
}
test_2()
{
	arki-scan --inline ${srcdir}/test.grib1 | ${srcdir}/singlepoint 23 43 > $outfile1 || return 1
	[[ -s $outfile1 ]] || return 1
	dbamsg dump --interpreted --csv $outfile1 | awk -F, '{ if ($12 == "B05001" || $12 == "B06001") { if (($12 == "B05001" && $13 != 43) || ($12 == "B06001" && $13 != 23)) { print ; exit 1 } } }' || return 1
}
test_3()
{
	arki-scan --inline ${srcdir}/test.grib1 | ${srcdir}/singlepoint 60 80 > $outfile1 || return 1
	dbamsg dump --interpreted --csv $outfile1 | awk -F, '/^60,80/{ if ($4 != "") { print ; exit 1 }}' || return 1
}

numok=0
numko=0
for (( i = 1 ; i <= 3 ; ++i ))
do
	if test_$i
	then
		(( numok++ ))
	else
		echo "Failed test_$i"
		(( numko++ ))
	fi
done

echo "Success: $numok, Failed: $numko"

[[ $numko -eq 0 ]]
