#!/bin/bash
 


echo "Testing decode for assignment 3... "

./decode.py test11.mtf 
./decode.py test12.mtf 
./decode.py test13.mtf 
./decode.py test14.mtf 
./decode.py test15.mtf 
./decode.py test16.mtf 
./decode.py test17.mtf 
./decode.py test18.mtf 
./decode.py test19.mtf 

if cmp test11.txt tests/test11.txt >/dev/null ; then
	echo test11 passed
else
	echo test11 failed

fi


if cmp test12.txt tests/test12.txt >/dev/null ; then
	echo test12 passed
else
	echo test12 failed
fi

if cmp test13.txt tests/test13.txt >/dev/null ; then
	echo test13 passed
else
	echo test13 failed
fi

if cmp test14.txt tests/test14.txt >/dev/null ; then
	echo test14 passed
else
	echo test14 failed
fi

if cmp test15.txt tests/test15.txt >/dev/null ; then
	echo test15 passed
else
	echo test15 failed
fi

if cmp test16.txt tests/test16.txt >/dev/null ; then
	echo test16 passed
else
	echo test16 failed
fi

if cmp test17.txt tests/test17.txt >/dev/null ; then
	echo test17 passed
else
	echo test17 failed
fi

if cmp test18.txt tests/test18.txt >/dev/null ; then
	echo test18 passed
else
	echo test18 failed
fi

if cmp test19.txt tests/test19.txt >/dev/null ; then
	echo test19 passed
else
	echo test19 failed
fi











