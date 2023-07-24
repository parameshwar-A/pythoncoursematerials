#include <stdio.h>
int main() {    

    inted number1, number2, sum;//error 1 
    
    printf("Enter two integers: ");
    scanfed("%d %d", &number1, &number2);

    // calculating sum
    sum = number1 + number2;      
    
    print("%d + %d = %d", number1, number2, sum);//error2
    return 0;
}

