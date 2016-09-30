#include <stdio.h>


int main(int argc, char const *argv[])
{
	printf("%s\n", "Hello World");
	printf("Count of arguments passeed - %d\n", argc);
	printf("Arguments passeed are as belows -\n");
	for (int i = 0; i < sizeof(*argv)/sizeof(char); ++i)
	{
		printf("%s\n", argv[i]);
	}
	return 0;
}


/*
Know from the output


~$ gcc understanding_main_function.c
~$ ./a.out  12 kunal
Hello World
Count of arguments passeed - 3
Arguments passeed are as belows -
./a.out
12
kunal
(null)
TERM_PROGRAM=Apple_Terminal
SHELL=/bin/bash
TERM=xterm-256color
TMPDIR=/var/folders/2p/kp8zdx097gjgst81l12pqdqh0000gn/T/

*/
