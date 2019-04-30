#!/bin/bash
 


echo "Testing encode_main() ... "

./text2mtf.py test00.txt 
./text2mtf.py test01.txt
./text2mtf.py test02.txt 
./text2mtf.py test03.txt
./text2mtf.py test04.txt 
./text2mtf.py test05.txt
./text2mtf.py test06.txt 
./text2mtf.py test07.txt
./text2mtf.py test08.txt 
./text2mtf.py test09.txt
./text2mtf.py test10.txt 


if diff test00.mtf tests/test00.mtf >/dev/null ; then
	echo test00 passed
else
	echo test00 failed

fi


if diff test01.mtf tests/test01.mtf >/dev/null ; then
	echo test01 passed
else
	echo test01 failed
fi

if diff test02.mtf tests/test02.mtf >/dev/null ; then
	echo test02 passed
else
	echo test02 failed
fi

if diff test03.mtf tests/test03.mtf >/dev/null ; then
	echo test03 passed
else
	echo test03 failed
fi

if diff test04.mtf tests/test04.mtf >/dev/null ; then
	echo test04 passed
else
	echo test04 failed
fi

if diff test05.mtf tests/test05.mtf >/dev/null ; then
	echo test05 passed
else
	echo test05 failed
fi
if diff test06.mtf tests/test06.mtf >/dev/null ; then
	echo test06 passed
else
	echo test06 failed
fi

if diff test07.mtf tests/test07.mtf >/dev/null ; then
	echo test07 passed
else
	echo test07 failed
fi

if diff test08.mtf tests/test08.mtf >/dev/null ; then
	echo test08 passed
else
	echo test08 failed
fi
if diff test09.mtf tests/test09.mtf >/dev/null ; then
	echo test09 passed
else
	echo test09 failed
fi

if diff test10.mtf tests/test10.mtf >/dev/null ; then
	echo test10 passed
else
	echo test10 failed
fi















