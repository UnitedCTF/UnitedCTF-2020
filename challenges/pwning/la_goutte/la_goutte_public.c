#include <stdio.h>

void degoutte() {
 volatile int pourquoi = 5;
 volatile long quoi = -1;
 volatile double comment = 252.04;
 volatile float ou = 33.5;
 volatile int quand = 4;
 char qui[16];

 puts("Quel est ton nom jeune apprenti?");
 gets(qui);
 if (pourquoi == 0xcafecafe) {
  printf("%s\nTu n'a pas besoin d'être mon apprenti, le savoir est déjà en toi.\n", "FLAG-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
 } else {
  printf("Bienvenue %s, le chemin sera long.\n", qui);
 }
}

int main(int argc, char* argv[]) {
 setvbuf(stdin, NULL, _IONBF, 0);
 setvbuf(stdout, NULL, _IONBF, 0);
 setvbuf(stderr, NULL, _IONBF, 0);
 degoutte();
 return 0;
}
