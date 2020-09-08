CC=gcc
CFLAGS= -O0 -fno-stack-protector -z execstack

all: le_lac_public le_lac

le_lac_public: le_lac.c
	$(CC) $(CFLAGS) $< -o $@

le_lac: le_lac.c
	$(CC) $(CFLAGS) $< -o $@ -D SERVER

clean:
	rm -f le_lac le_lac_public
