#include <iostream>
#include <vector>
#include <string>
#include <random>

#include <unistd.h>

using namespace std;

//#define buildflag

const vector<string> v = {
	"Once upon a midnight dreary, while I pondered, weak and weary.",
	"Over many a quaint and curious volume of forgotten lore.",
	"While I nodded, nearly napping, suddenly there came a tapping.",
	"As of some one gently rapping, rapping at my chamber door.",
	"Ah, distinctly I remember it was in the bleak December.",
	"And the silken, sad, uncertain rustling of each purple curtain.",
	"So that now, to still the beating of my heart, I stood repeating.",
	"Tis some visitor entreating entrance at my chamber door.",
	"This it is and nothing more.",
	"Presently my soul grew stronger; hesitating then no longer.",
	"And so faintly you came tapping, tapping at my chamber door.",
	"Darkness there and nothing more.",
	"Deep into that darkness peering, long I stood there wondering, fearing.",
	"Back into the chamber turning, all my soul within me burning.",
	"In there stepped a stately Raven of the saintly days of yore.",
	"Ghastly grim and ancient Raven wandering from the Nightly shore",
	"Quoth the Raven “Nevermore.”",
	"Be that word our sign of parting, bird or fiend!"
};

const string stream = "Get thee back into the tempest and the Night’s Plutonian shore!";

const vector<unsigned char> data = {26, 240, 69, 59, 121, 115, 60, 48, 72, 156, 13, 192, 189, 95, 79, 216, 117, 94, 106, 140, 39, 216, 255, 7, 60};

const int iter = 100'000;

string crypt(const string& s, const int j)
{
	string newstr = "";
	for (int i = 0; i < s.size(); i++)
	{
		newstr += s[i] ^ ((stream.at(j % stream.size()) + j + i) % 256);
	}
	return newstr;
}

int main()
{
	string str = "REEEEEEE";
	seed_seq seed(str.begin(), str.end());
	mt19937 randomizer(seed);

	uniform_int_distribution<int> uid(0, v.size() - 1);

#ifdef buildflag

	string flag = "flag-g0dD0Ilik3libN0Sl33p";

	for (int i = 0; i < iter; i++)
		flag = crypt(flag, i);

	for (int i = 0; i < flag.size(); i++)
		cout << static_cast<unsigned int>(flag[i]) % 256 << ", ";

	cout << endl;

#else

	string junk(data.begin(), data.end());

	for (int i = iter - 1; i >= 0; i--)
	{
		int var = static_cast<unsigned int>(uid(randomizer));
		cout << v.at(var) << endl;

		usleep(1974019);		// wait about 2 seconds

		junk = crypt(junk, i);
	}

	sleep(1987200);		// wait about 23 days (lol)

	cout << junk <<endl;

#endif

	return 0;
}
