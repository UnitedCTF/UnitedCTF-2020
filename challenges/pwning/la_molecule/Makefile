CC=gcc
CFLAGS= -O0 -fno-stack-protector

all: la_molecule

la_molecule: la_molecule.c
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f la_molecule 
