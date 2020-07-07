#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FLAG_LENGTH 20

void flag(unsigned char output[])
{
	// 410 almost random chars
	unsigned char arr410[] = {'y', 'y', 'v', 'o', 'l', 'o', 'r', 'h', 'u', 'u', 'g', 'l', 'c', 'n', 'k', 'l', 'q', 'c', 'g', 'u', 'z', 'q', 'z', 'q', 'e', 'q', 'n', 't', 'a', 'r', 'm', 'i', '-', 'e', 'z', 'e', 'y', 'i', 'u', 'y', 'h', 'v', 'f', 'n', 'x', 'k', 'd', 'n', 'y', 't', 'p', 'q', 'c', 'b', 'h', 'y', 'd', 'o', 'g', 'i', 'u', 't', 'k', 'b', 'c', 's', 'd', 'd', 'e', 'q', 'j', 'o', 'd', 'w', 'u', 'z', 'f', 'a', 'd', 'h', 'v', 't', 'v', 'g', 'g', 'i', 'l', 'j', 'v', 'x', 'j', 'e', 'i', 'h', 'f', 'j', 'c', 'm', 'n', 'e', 'z', 'o', 'g', 'w', 'g', 'd', '4', 'b', 't', 'p', 'c', 'a', 'n', 'o', 'x', 'i', 'd', 'w', 'o', 'r', 'y', 'z', 'c', 'f', 'l', 'g', 'v', 'h', 'd', 'e', 'q', 'i', 'q', 'p', 'l', 'f', 't', 'o', 'j', 'a', '5', 'n', 'b', '4', 'r', 'q', 'p', 'p', 'f', 'j', 'y', 'g', 'g', 'b', 'd', 'v', 'w', 'a', 'c', 'p', 'v', 'x', 'h', 'v', 'g', 'q', 'f', 'p', 'g', 'w', 'm', 'h', '7', 'i', 's', '7', 'e', 'v', 'i', 'k', 'c', 'j', 'r', 'h', 'm', 'e', 'c', 't', 'z', 'f', 's', 'z', 'h', 'p', 'm', 'u', 'r', 'z', 'q', 'g', 'k', 'b', 'u', 'b', 'h', 'x', 'y', 'q', 'a', 't', 't', 'h', 'g', 'q', 'a', 'g', 'o', 'e', 'w', 'q', 'o', 'b', 't', 'r', 'l', 'g', 'z', 'u', 'n', 'x', 'p', '0', 'g', 'g', 'a', 'u', 'k', 'f', 'o', 'w', 't', 'h', 'x', 'q', 't', 'u', 'h', 'r', 'z', 's', 'n', 'l', 'o', 'y', 'g', 'v', 'c', '5', 'k', 'r', 'n', 'k', 'z', 'j', 'j', 'y', 'v', 'a', 'w', 'q', 'f', 'l', 'r', 'k', 'm', 's', 'j', 'o', 'n', 'x', 'b', 'w', 'w', 'y', 'g', 'k', 'h', 's', 'x', 's', 'f', 'a', 'i', 'q', 'd', 'v', 'd', 'w', 'j', 'r', 'u', 'e', 'v', 'c', 'r', 'z', 'y', 'd', 'k', 'n', 'i', 'i', 'n', 'k', 'v', 't', 'i', 'u', 'q', 'n', 'c', 'b', 'o', 'g', 'd', 'f', 'f', 'p', 'c', 'f', 'd', 'f', 'n', 'g', 'q', 'q', 'c', 'g', 'd', 'j', 'q', 'x', 'b', 's', 'j', 'n', 'f', 'v', 'a', 'b', 'g', 'r', 'y', 'u', 'l', 'h', 'g', 'q', 'e', '0', 'w', 'i', 'k', 'o', 'm', 'u', 'p', 'r', 't', 's', 'p', 'p', 'o', 's', 'n', 's', 'v', 'm', 'n', 'q', 'l', 'w', 't', 'y', 'j', 'k', 'g', 'i', 'l', 'd', 'j', 'i', 'v', 'w', 'r', '7', 'j', 'd', 'r', 'l', 'z', 'm', 'r', 'n', 'z', 'v', 'f', 'b', 'r', 'q'};

	for (int i = 0; i < FLAG_LENGTH; i++)
	{
		output[i] = arr410[rand() % 410];
	}
}

int main()
{
	puts("Enter the secret password:");

	unsigned char password[80] = {0};

	int n = scanf("%79s", password);

	if (n > 0 && !strcmp(password, "goobers"))
	{
		unsigned char output[FLAG_LENGTH] = {0};

		srand(7337);
		flag(output);
		printf("%20s\n", output);
	}
	else
	{
		puts("Wrong password!");
	}
}
