%{

#include <stdlib.h>
#include <string.h>


int line_number = 1;
char printf_str[100];
char identifier_name[50];
int symbol_table_length = 0;
int i = 0;
int j = 0;
char type[30][10];
char name[30][10];
char value[30][100];
int line_num[30];
char for_spe[30];
int scope=0;
int scopes[100];
%}
alpha [A-Za-z_]
digit [0-9]
%%
"\n" line_number++;
int[' '][a-zA-Z][a-zA-Z0-9]*['=']{digit}*";" {int r=0; int flag=0; char id[100]="";;
		for(int q=4;yytext[q]!='=';++q)
		id[r++]=yytext[q];
		//cout<<id;
	for(int p=0;p<symbol_table_length;p++)
	{
if(strcmp(id,name[p])==0)
{
flag=1;
break;
}
}
if(flag!=1){
                            strcpy(type[symbol_table_length], "int");
			    scopes[symbol_table_length]=scope;
                            for(i = 4; yytext[i]!='='; ++i)
                                name[symbol_table_length][j++] = yytext[i];
                            while(yytext[i]!='\0') {
                                if(yytext[i] == '='){
                                    j = 0;
                                    i++;
                                    for(;yytext[i]!=';'; ++i)
                                        value[symbol_table_length][j++] = yytext[i];
                                    break;
                                }
                            }
                            for_spe[symbol_table_length] = 'd';
                            line_num[symbol_table_length] = line_number;
                            symbol_table_length++;j=0;} else {cout<<"Multiple declarations of"<<id<<"at line number "<<line_number<<"\n";exit(0);}};
float[' '][a-zA-Z][a-zA-Z0-9]*['=']{digit}*\.{digit}*";" {int r=0; int flag=0; char id[100];
		for(int q=6;yytext[q]!='=';++q)
		id[r++]=yytext[q];
	for(int p=0;p<symbol_table_length;p++)
	{
if(strcmp(id,name[p])==0)
{
flag=1;
break;
}
}
if(flag!=1){
                            strcpy(type[symbol_table_length], "float");
			scopes[symbol_table_length]=scope;
                            //strcpy(name[symbol_table_length], yytext);
                            j = 0;
                            for(i = 6; yytext[i]!='='; ++i)
                                name[symbol_table_length][j++] = yytext[i];
                                while(yytext[i]!='\0') {
                                    if(yytext[i] == '='){
                                        j = 0;
                                        i++;
                                        for(;yytext[i]!=';'; ++i)
                                            value[symbol_table_length][j++] = yytext[i];
                                        break;
                                    }
                                }
                                for_spe[symbol_table_length]= 'f';
                            line_num[symbol_table_length] = line_number;
                            symbol_table_length++;j=0;} else {cout<<"Multiple declarations of"<<id<<"at line number "<<line_number<<"\n";exit(0);}
				};
char[' '][a-zA-Z][a-zA-Z0-9]*['='][\'][a-zA-z][\']";" {int r=0; int flag=0; char id[100];
		for(int q=5;yytext[q]!='=';++q)
		id[r++]=yytext[q];
	for(int p=0;p<symbol_table_length;p++)
	{
if(strcmp(id,name[p])==0)
{
flag=1;
break;
}
}
if(flag!=1){
                            strcpy(type[symbol_table_length], "char");
				scopes[symbol_table_length]=scope;
                            //strcpy(name[symbol_table_length], yytext);
                            j = 0;
                            for(i = 5; yytext[i]!='='; ++i)
                                name[symbol_table_length][j++] = yytext[i];
                                while(yytext[i]!='\0') {
                                    if(yytext[i] == '='){
                                        j = 0;
                                        i++;
                                        for(;yytext[i]!=';'; ++i)
                                            value[symbol_table_length][j++] = yytext[i];
                                        break;
                                    }
                                }
                                for_spe[symbol_table_length] = 'c';
                            line_num[symbol_table_length] = line_number;
                            symbol_table_length++;j=0;} else {cout<<"Multiple declarations of"<<id<<"at line number "<<line_number<<"\n";exit(0);}};
[ \t\n]

"//".*["\n"*] {line_number++;};
"/*"(.|"\n")*"*/"(" "|\n)* {line_number++;};
"while" return WHILE;
"for" return FOR;
"if" return IF;
"else" return ELSE;
"cout" return COUT;
"endl" return ENDL;
"break" return BREAK;
"continue" return CONTINUE;
"int" return INT;
"float" return FLOAT;
"char" return CHAR;
"void" return VOID;
"#include" return INCLUDE;
"main()" return MAINTOK;
{digit}+    return NUM;
{alpha}({alpha}|{digit})*    return ID;
{alpha}({alpha}|{digit})*"\.h"?   return H;
\".*\" return STRING;
"<"   return T_lt;
">"     return T_gt;
"="     return T_eq;
"<="    return T_lteq;
">="    return T_gteq;
"=="    return T_eqeq;
"!="    return T_neq;
"+"     return T_pl;
"-"     return T_min;
"*"     return T_mul;
"/"     return T_div;
"++"    return T_incr;
"--"    return T_decr;
"!"     return T_neq;
"||"    return T_or;
"&&"    return T_and;
"{"	{scope++; return open;}
"}"	{return clo;}
.    return yytext[0];
%%
