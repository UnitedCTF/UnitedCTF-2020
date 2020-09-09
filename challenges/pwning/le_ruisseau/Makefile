CC=gcc
CFLAGS= -O0 -fno-stack-protector -no-pie

all: le_ruisseau_public le_ruisseau

le_ruisseau_public: le_ruisseau.c
	$(CC) $(CFLAGS) $< -o $@

le_ruisseau: le_ruisseau.c
	$(CC) $(CFLAGS) $< -o $@ -D SERVER

clean:
	rm -f le_ruisseau le_ruisseau_public
