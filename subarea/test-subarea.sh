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
    arki-query --inline '' $srcdir/test.grib1 | $srcdir/subarea 10 2>/dev/null && return 1 || return 0
}
test_2()
{
    arki-query --inline '' $srcdir/test.grib1 | $srcdir/subarea 10 20 2>/dev/null && return 1 || return 0
}
test_3()
{
    arki-query --inline '' $srcdir/test.grib1 | $srcdir/subarea 10 20 30 2>/dev/null && return 1 || return 0
}
test_4()
{
    arki-query --inline '' $srcdir/test.grib1 | $srcdir/subarea 10 20 30 40 > $outfile1 || return 1
    [[ -s $outfile1 ]] || return 1
    grib_get_data $outfile1 | awk '/Latitude.*/{} /^[ \t]*[0-9]/{ lat=$1; lon=$2 ; if (lon < 9 || lon > 31 || lat < 19 || lat > 41 ) { print ; exit 1 ; } }' || return 1
}

numok=0
numko=0
for (( i = 1 ; i <= 4 ; ++i ))
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
