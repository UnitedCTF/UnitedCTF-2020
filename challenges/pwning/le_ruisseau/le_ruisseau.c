#include <stdio.h>

#ifdef SERVER
#define flag "FLAG-RET2TEXT_4cc0mplished_j5fwyolcmPg"
#else
#define flag "FLAG-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
#endif

void detour() {
	printf("%s\nLe flux d'exécution d'un programme est comme un ruisseau, on peut le détourner en le faisant déborder\n", flag);
}

void flux() {
	volatile char w[8] = "woushhh";
	volatile short main_gauche = 0xc7;
	volatile short main_droite = 0xa4;
	char son[16];

	puts("Quel est le son d'une seule main qui applaudit?");
	gets(son);
	printf("Une main qui fait \"%s\"? Mais quelle idée absurde!\n", son);
}

int main(int argc, char* argv[]) {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	flux();
	return 0;
}
