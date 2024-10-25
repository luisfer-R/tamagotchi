#include <stdio.h>
#include <ncurses.h>
#include <time.h>

#define FINE 0
#define HUNGRY 1
#define BORED 2
#define DEATH 3

void print_menu(void)
{
  printf("Select an option\n");
  printf("FEED\n");
  printf("PLAY\n");
}

int HEALT = 100;
int HUNGER = 0;
int AMUSE = 100;
int STATUS = 0;

int autom[4][6] = { { 0, 0, 0, 0, 0, 0 }, //HEALTY
                    { 1, 0, 0, 0, 0, 0 }, //HUNGRY
                    { 2, 0, 0, 0, 0, 0 }, // BORED
                    { 3, 3, 3, 3, 3, 3 } }; //DEAD

int main (int argc, char *argv)
{
  return 0;
}
