CC=gcc
CFLAGS= -O0 -fno-stack-protector

all: la_goutte_public la_goutte

la_goutte_public: la_goutte.c
	$(CC) $(CFLAGS) $< -o $@

la_goutte: la_goutte.c
	$(CC) $(CFLAGS) $< -o $@ -D SERVER

clean:
	rm -f la_goutte la_goutte_public
