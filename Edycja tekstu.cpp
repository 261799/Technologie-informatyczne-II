#include <iostream>

void toLower(char *text){
    while(*text){
        if(*text>='A'&& *text<='Z'){
            *text -=('A'-'a');
        }
        text++;
    }
}

void toUpper(char *text){
    while(*text){
        if(*text>='a'&&*text<='z'){
            *text -=('a'-'A');
        }
        text++;
    }
}

int textSize(char *text){
    int size = 0;
    while(*text){
        size++;
        text++;

    }
    return size;
}

int main(){
    char text[] = "Ala ma kota.";
    printf("%s \n",text);
    toLower(text);
    printf("%s \n",text);
    toUpper(text);
    printf("%s \n",text);
    printf("%d \n",textSize(text));


    return 0;
}
