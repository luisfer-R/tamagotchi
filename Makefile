all: build
build: tamagotchi.c
	gcc -o tamagotchi tamagotchi.c
clean:
	rm tamagotchi
