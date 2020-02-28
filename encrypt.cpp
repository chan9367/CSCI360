#include <stdio.h>
#include <ctype.h>

int main()
{
	FILE* input = stdin;
	FILE* output = stdout;
	char c,k='F';
	while ((c=getc(input)) != EOF)
	{
		//YOUR CODE HERE//
    c+=5; if(c>90)c-=26; 
		putc(c,output);
	}
}
