all:
	gcc src/main.c -o shell

run:
	./shell

clean:
	rm -f shell