#include <stdio.h>
#include <curses.h>

int main ()
{
    int ch;
    printf("Hello, world!\n");
    ch = getch();

    printf("[ %d ]\n", ch);
    return 0;
}
