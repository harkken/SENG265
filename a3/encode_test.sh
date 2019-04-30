#!/bin/bash
 


echo "Testing encode for assignment 3... "
echo "Please allow up to ten seconds for script to run"
./encode.py test11.txt 
./encode.py test12.txt
./encode.py test13.txt 
./encode.py test14.txt
./encode.py test15.txt 
./encode.py test16.txt
./encode.py test17.txt 
./encode.py test18.txt
./encode.py test19.txt 

if diff test11.mtf tests/test11.mtf >/dev/null ; then
	echo test11 passed
else
	echo test11 failed

fi


if diff test12.mtf tests/test12.mtf >/dev/null ; then
	echo test12 passed
else
	echo test12 failed
fi

if diff test13.mtf tests/test13.mtf >/dev/null ; then
	echo test13 passed
else
	echo test13 failed
fi

if diff test14.mtf tests/test14.mtf >/dev/null ; then
	echo test14 passed
else
	echo test14 failed
fi

if diff test15.mtf tests/test15.mtf >/dev/null ; then
	echo test15 passed
else
	echo test15 failed
fi

if diff test16.mtf tests/test16.mtf >/dev/null ; then
	echo test16 passed
else
	echo test16 failed
fi
if diff test17.mtf tests/test17.mtf >/dev/null ; then
	echo test17 passed
else
	echo test17 failed
fi

if diff test18.mtf tests/test18.mtf >/dev/null ; then
	echo test18 passed
else
	echo test18 failed
fi

if diff test19.mtf tests/test19.mtf >/dev/null ; then
	echo test19 passed
else
	echo test19 failed
fi














