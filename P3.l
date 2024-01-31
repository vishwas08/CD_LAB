%{
#include<stdio.h>
int cnt=0;
%}
sign [+|-]
num [0-9]
dot [.]
%%
{sign}{num}*{dot}*{num}* {printf("Signed no.");cnt=1;}
{num}*{dot}*{num}* {printf("Unsigned no.");cnt=1;}
%%
int yywrap()
{
}
int main()
{
yylex();
if(cnt==0){
printf("Not floating pnt no.");
}
return 0;
}

