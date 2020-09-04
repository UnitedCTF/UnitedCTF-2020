#include <stdio.h>
#include <string.h>

void check(int value)
{
	if (value != 1)
	{
		puts("Wrong password!");
	}
	else
	{
		puts("Good password!");
	}
}

char asymbol()
{
	return '!';
}

#define ROR(x,y) ((unsigned)(x) >> (y) | (unsigned)(x) << 32 - (y))

int main(int argc, char* argv[], char** envp)
{
	// good passwd?
	int valid = 0;

	if (argc > 1)
	{
		// values for password validation
		volatile unsigned int i = 0;
		volatile unsigned int j = 0;
		char str[200];

		// storing the argument in a way to limit its size
		char arg[200];
		strncpy(arg, argv[1], 199);	// Note: strncpy pads with nulls for the remaining length
		arg[199] = '\0';

		// by how much to shift? (not to optimize)
		volatile unsigned int two = 2;
		volatile unsigned int three = 3;
		volatile unsigned int four = 4;

		// other symbols not to optimize
		volatile char sym_Y = 'Y';
		volatile char sym_nine = '9';
		volatile char sym_d = 'd';

		if (sscanf(arg, "flag-%d-%x.%s", &i, &j, str) == three)
		{
			// 'i' = 0x31337 (decimal 201527), then xored with 0x17337, shifted left by two. This gives 0x98000. (decimal 622592)
			if (((i ^ 0x17337) << two) == 0x98000)
			{
				// 'j' = 0xFEEDC0DE, then ROR 3 gives 0xDFDDB81B. Xor 0xDFDDB81B with 'i' == 0x31337 to give 0xDFDEAB2C.
				if ((ROR(j, three) ^ i) == 0xDFDEAB2C)
				{
					// constraints for str
					if (str[0] - sym_Y == asymbol() && str[1] == sym_nine && str[2] == (4 << four) && str[3] == sym_d - str[6] && str[4] == 0)
					{
						valid = 1;    // User validated flag-201527-FEEDC0DE.z9@d
					}
				}
			}
		}
	}

	check(valid);
}
