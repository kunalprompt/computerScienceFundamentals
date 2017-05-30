#include <stdio.h>

int main(int argc, char const *argv[])
{
	/* code */
    float f = 0.1;
    if (f == 0.1)
        printf("True");
    else
        printf("False");
    return 0;
}

/*
Answer: becoz while comparing "f" to 0.1, 
		f is getting compared with a "double" rather than "float".
		
*/ 