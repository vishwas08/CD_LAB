%{
#include<stdio.h>
int cnt=0;
%}
chars [a-z|A-Z|0-9]
check [A|a|AN|An|THE|The]
%%
{check}+{chars}* {printf("The sentence begins with the article %s\n",yytext);}
{chars}* {printf("The sentence does not begins with articles\n");}
%%
int yywrap()
{
}
int main()
{
printf("Enter the sentence : ");
yylex();
return 0;
}


