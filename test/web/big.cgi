#!/bin/sh

echo "Content-type: text/plain"
# echo "Content-Length: 500000"
echo ""

i=0
while [ $i -lt 1000 ]
do
    cat <<!EOF 
0123456789012345678901234567890123456789012345678
0123456789012345678901234567890123456789012345678
0123456789012345678901234567890123456789012345678
0123456789012345678901234567890123456789012345678
0123456789012345678901234567890123456789012345678
0123456789012345678901234567890123456789012345678
0123456789012345678901234567890123456789012345678
0123456789012345678901234567890123456789012345678
0123456789012345678901234567890123456789012345678
0123456789012345678901234567890123456789012345678
!EOF
    # sleep 10
    i=$((i + 1))
done
