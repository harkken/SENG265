#!/bin/bash
 


echo "Testing decode_main() ... "

./mtf2text.py test00.mtf 
./mtf2text.py test01.mtf 
./mtf2text.py test02.mtf 
./mtf2text.py test03.mtf 
./mtf2text.py test04.mtf 
./mtf2text.py test05.mtf 
./mtf2text.py test06.mtf 
./mtf2text.py test07.mtf 
./mtf2text.py test08.mtf 
./mtf2text.py test09.mtf 
./mtf2text.py test10.mtf 


if cmp test00.txt tests/test00.txt >/dev/null ; then
	echo test00 passed
else
	echo test00 failed

fi


if cmp test01.txt tests/test01.txt >/dev/null ; then
	echo test01 passed
else
	echo test01 failed
fi

if cmp test02.txt tests/test02.txt >/dev/null ; then
	echo test02 passed
else
	echo test02 failed
fi

if cmp test03.txt tests/test03.txt >/dev/null ; then
	echo test03 passed
else
	echo test03 failed
fi

if cmp test04.txt tests/test04.txt >/dev/null ; then
	echo test04 passed
else
	echo test04 failed
fi

if cmp test05.txt tests/test05.txt >/dev/null ; then
	echo test05 passed
else
	echo test05 failed
fi

if cmp test06.txt tests/test06.txt >/dev/null ; then
	echo test06 passed
else
	echo test06 failed
fi

if cmp test07.txt tests/test07.txt >/dev/null ; then
	echo test07 passed
else
	echo test07 failed
fi

if cmp test08.txt tests/test08.txt >/dev/null ; then
	echo test08 passed
else
	echo test08 failed
fi

if cmp test09.txt tests/test09.txt >/dev/null ; then
	echo test09 passed
else
	echo test09 failed
fi

if cmp test10.txt tests/test10.txt >/dev/null ; then
	echo test10 passed
else
	echo test10 failed
fi















