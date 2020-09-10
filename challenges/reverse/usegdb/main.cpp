#include <iostream>
#include <vector>
#include <string>
#include <random>

#include <unistd.h>

using namespace std;

//#define buildflag

const string stream = "\xf9\xb4\x1c\xb5\x18\x25\x56\x1c\x77\x2e\x94\xfe\xd0\x6f\x50\x3a\x16\xb2\x8e\x96\x4a\xbb\xf0\x6b\x9b\x97\x2c\xa2\x73\x32\xb1\x9d";

const vector<unsigned char> data = {176, 126, 163, 145, 211, 133, 230, 252, 71, 1, 86, 225, 203, 17, 82, 227};

const int iter = 100;//'000;
const int iter_flag = 58;//58731;

string crypt(const string& s, const int j, const int k)
{
	string newstr = "";
	for (int i = 0; i < s.size(); i++)
	{
		newstr += s[i] ^ ((stream.at(j % stream.size()) + j + i + k) % 256);
	}
	return newstr;
}

int main()
{
	string str_seed = "\x5f\x37\x35\x9c\x50\x75\x9f\x16\xb3\x40\xaf\xc3\xb3\xe7\x55\x3b";
	seed_seq seed(str_seed.begin(), str_seed.end());
	mt19937 randomizer(seed);

	uniform_int_distribution<int> uid(0, 255);

#ifdef buildflag

	string flag = "flag-gdb1s4wes0m";
	vector<int> random_nums;
	int random_index;

	for (int i = iter_flag; i < iter; i++)
		random_nums.push_back(static_cast<unsigned int>(uid(randomizer)));

	random_index = random_nums.size();

	for (int i = iter_flag; i < iter; i++)
		flag = crypt(flag, i, random_nums[--random_index]);

	// This prints the 'data' needed to get this flag.
	for (int i = 0; i < flag.size(); i++)
		cout << static_cast<unsigned int>(flag[i]) % 256 << ", ";

	cout << endl;

#else

	string junk(data.begin(), data.end());

	for (register int i = iter - 1; i >= 0; i--)
	{
		junk = crypt(junk, i, static_cast<unsigned int>(uid(randomizer)));

		const char* c = junk.c_str();

		// Uncomment 'junk' to test the flag. The `if` is optimized out.
		if (i == iter_flag)
		{
//			cout << junk << endl;
		}
	}

#endif

	return 0;
}
