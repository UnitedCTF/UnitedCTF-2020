#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <string.h>

#define flag "FLAG-na5ty-buff3r-0verfl0w"

void singal_handler(int sig, siginfo_t *sinfo, void *ctxt)
{
	puts(flag);

	if (sinfo->si_signo == SIGSEGV)
	{
		puts("signal (11). Segmentation fault");
		puts("*** stack smashing detected ***: terminated");
		puts("Aborted (core dumped)");
	}
	else if (sinfo->si_signo == SIGBUS)
	{
		puts("Bus error (core dumped)");
	}
	else
	{
		puts("Erreur fatale!!! Elle est même monumentale!!!");
	}

	exit(1);
}

int ask_secret()
{
	char receiver[40];
	printf("Entrez votre code secret: ");
	gets(receiver);
	// On veut retourner mais un débordement écrase l'adresse de retour

	return strnlen(receiver, 25) > 24;
}

void crashme()
{
	puts("Portail secret. Accès restraint.");

	while (1)
	{
		int ret = ask_secret();
		if (!ret)
			puts("Code invalide!");
		else
			puts("Code invalide! SVP ne pas entrer de codes trop longs.");
	}
}

int main(int argc, char* argv[])
{
	setvbuf(stdin,  NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);

	struct sigaction act;
	memset(&act, 0, sizeof(struct sigaction));
	sigemptyset(&act.sa_mask);

	act.sa_sigaction = singal_handler;
	act.sa_flags = SA_SIGINFO;

	if (sigaction(SIGSEGV, &act, NULL) < 0 || sigaction(SIGBUS, &act, NULL) < 0)
	{
		// J'espère que ça va jamais arriver
		puts("Le défi est brisé. Contactez un administrateur du UnitedCTF.");
		exit(1);
	}

	crashme();
	return 0;
}
