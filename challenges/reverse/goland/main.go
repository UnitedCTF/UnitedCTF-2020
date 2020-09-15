package main

import (
	"fmt"
	"bufio"
	"os"
)

// flag: https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,13)Bit_shift_left(1)To_Hex('0x%20with%20comma',0)&input=Zmw0Zy03dV8zczdfN3IwcF9jMG1wMzc0bjdfcDB1cl8zN3IzXzR1X3VuMXQzZGM3Zg
var gfal = []byte{0xe6,0xf2,0x68,0xe8,0x5a,0x6e,0xd0,0xbe,0x66,0xcc,0x6e,0xbe,0x6e,0xca,0x60,0xc6,0xbe,0xe0,0x60,0xf4,0xc6,0x66,0x6e,0x68,0xc2,0x6e,0xbe,0xc6,0x60,0xd0,0xca,0xbe,0x66,0x6e,0xca,0x66,0xbe,0x68,0xd0,0xbe,0xd0,0xc2,0x62,0xce,0x66,0xe2,0xe0,0x6e,0xe6}	

// ROT13
// Le compilateur de Go l'inline dans la fonction "stuff" donc
// ça fait une fonction plus lourde à reverser  :-(
func secret(b byte) byte {
	if 'a' <= b && b <= 'z' {
		return (b - 'a' + 13) % ('z' - 'a' + 1) + 'a'
	}

	return b
}

// Logique de validation
func stuff(password string) bool {
	for i, rc := range password {

		// convertir de rune à byte
		ch := []byte(string(rc))

		if i >= len(gfal) { // indice: comparaison avec la taille
			return false
		}

		// on encore à moitié l'input dans la fonction "secret" et décode à moitié le flag
		if secret(ch[0]) != gfal[i] >> 1 {
			return false
		}
	}

	if len(gfal) <= len(password) { // indice: comparaison avec la taille
		return true
	}

	return false
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Println("Sup. Devine le flag. Donne-moi le! J'ai faim!  :D")
	fmt.Print("-> ")

	if scanner.Scan() {
		message := scanner.Text()
		if stuff(message) {
			fmt.Println("Like a bowss!  :O")
		} else {
			fmt.Println("You fail it.  :(")
		}
	} else {
		fmt.Print("Say wuuuut?  xD")
	}
}
