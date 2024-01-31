%{
#include<stdio.h>
int cnt=0;
%}
punc [?|,|.|!]
chars [a-z|A-Z|0-9|" "|\t]
%%
{chars}*{punc} {printf("Sentence ends with punctuation");}
{chars}* {printf("Sentence does not end with punctuation");}
%%
int yywrap()
{
}
int main()
{
yylex();
return 0;
} 

