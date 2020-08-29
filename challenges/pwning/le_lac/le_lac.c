#include <stdio.h>

void vide() {
	char bateau[256];

	printf("Imaginez un bateau vide qui flotte sur un lac. Tentez de trouver le coquillage dans le bateau vide qui se trouve à %p\n", bateau);
	gets(bateau);
}

int main(int argc, char* argv[]) {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	vide();
	return 0;
}
