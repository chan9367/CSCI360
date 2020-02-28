#include <stdio.h>
#include <ctype.h>
#include <iostream>

int main()
{
	FILE* input = stdin;
	char c,arr[26]={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
	int cc[26]={0};
  float x=0.0;
  while ((c=getc(input)) != EOF)
	{
    x++;
		for(int i=0; i<26; i++){
      if(c==arr[i]){cc[i]++;}
    }
	}
for(int j=0; j<26; j++){
      std::cout<<arr[j]<<": "<<cc[j]/x<<std::endl;
    }
}
