### Project 1
#### CSCI 360, Cryptography
##### due: 9/10/19

---

### Introduction

In this project we will play around with simple substitution ciphers. We will implement and also attack a simple form of substitution cipher called a shift cipher which is defined as follows.

1. The space of messages $M$ consists of any message written using only upper case Roman letters. No spaces or other punctuation symbols occur in the messages.
2. The space of ciphertexts $C$ is mathematically the same as $M$.
3. The space of keys $K$ is the set of upper case Roman letters.

The encryption function $e_k()$ is defined by

$$e_k(x) = (x_1+k)\%26,(x_2+k)\%26,\cdots,(x_n+k)\%26$$

where the message $x = x_1x_2x_3\cdots x_n$ is $n$ letters long and each letter (as well as the key $k$) is understood as a number between 0 and 25, with $A=0$,$B=1$, etc.

---

**Example:**

If $k=X$, and $x=HAPPYBIRTHDAY$ (so that $x_1=H,x_2=A,\ldots,x_{12}=Y$), then $y=EXMMVYFOQEAXV$.

Why is the first ciphertext character E?  Let's work through and see.

The key $X$ is the 24th letter of the alphabet and therefore $X=23$ (because indexing starts at 0).  The letter $H = 7$.  So we add 23 and 7 and then mod out by 26.  Clearly $30\equiv 4\mod\,26$, and the letter E=4.  

The other characters in the ciphertext work similarly.

---

Decryption is accomplished by

$$d_k(y) = (y_1-k)\%26,(y_2-k)\%26,\cdots,(y_n-k)\%26$$

where the ciphertext $y = y_1y_2\cdots y_n$ is $n$ letters long, and where the characters are interpreted as numbers in the range $0,1,\ldots,25$.  Here we assume that $a\%b$ is always a number in the range $\{0,1,\ldots,|b|-1\}$ for nonzero $b$. Note that in C++ negative numbers present some problems for this assumption.  For example `-1%26==-1` in C++.  This difficulty can be overcome by adding multiples of 26, for example

$$-1 \equiv -1+26 \equiv 25\,\mod{26}$$

Thus, in our code, $(-1+26)\%26$ can be used to ensure that the output is in the correct range.

---

**Example:**

Like in the first example, let's assume

$k=X$, $x=HAPPYBIRTHDAY$ and $y=EXMMVYFOQEAXV$. Suppose we want to decrypt the first letter E in the ciphertext.  We know that $E=4$ and $X=23$.  So to decrypt we compute 4-23 = -19.  This number is negative, so we add 26.  Now we have 26-19 = 7.  We reduce 7 mod 26, to get 7 again.  (Notice 26 goes into 7 zero times with a remainder of 7.) 

And because $H=7$ this decryption is correct.

---



The shift cipher described above is a little bit less general than a substitution cipher, because every letter is shifted by the same amount, namely $k$.  In a true substitution cipher, any permutation of the letters would be permissible.  Therefore while the key space in a shift cipher is size 26, the key space in a general substitution cipher is 26!, which is quite a bit bigger.  Shift ciphers are very vulnerable to brute force key search while substitution ciphers may not be (if the alphabet is large enough). However both are vulnerable to statistical attacks, because the relationships between the letters in the plaintext are preserved in the ciphertext.

---
**Example**

Consider the plaintext $x=ABCDEFGHIJKLMNOPQRSTUVWXYZ$.  Supposing that we are using a shift cipher, how many corresponding ciphertexts are there?  It's easy to list them all:

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ  (k = A)
BCDEFGHIJKLMNOPQRSTUVWXYZA  (k = B)
CDEFGHIJKLMNOPQRSTUVWXYZAB  (k = C)
DEFGHIJKLMNOPQRSTUVWXYZABC  (k = D)
EFGHIJKLMNOPQRSTUVWXYZABCD  (k = E)
FGHIJKLMNOPQRSTUVWXYZABCDE  (k = F)
GHIJKLMNOPQRSTUVWXYZABCDEF  (k = G)
HIJKLMNOPQRSTUVWXYZABCDEFG  (k = H)
IJKLMNOPQRSTUVWXYZABCDEFGH  (k = I)
JKLMNOPQRSTUVWXYZABCDEFGHI  (k = J)
KLMNOPQRSTUVWXYZABCDEFGHIJ  (k = K)
LMNOPQRSTUVWXYZABCDEFGHIJK  (k = L)
MNOPQRSTUVWXYZABCDEFGHIJKL  (k = M)
NOPQRSTUVWXYZABCDEFGHIJKLM  (k = N)
OPQRSTUVWXYZABCDEFGHIJKLMN  (k = O)
PQRSTUVWXYZABCDEFGHIJKLMNO  (k = P)
QRSTUVWXYZABCDEFGHIJKLMNOP  (k = Q)
RSTUVWXYZABCDEFGHIJKLMNOPQ  (k = R)
STUVWXYZABCDEFGHIJKLMNOPQR  (k = S)
TUVWXYZABCDEFGHIJKLMNOPQRS  (k = T)
UVWXYZABCDEFGHIJKLMNOPQRST  (k = U)
VWXYZABCDEFGHIJKLMNOPQRSTU  (k = V)
WXYZABCDEFGHIJKLMNOPQRSTUV  (k = W)
XYZABCDEFGHIJKLMNOPQRSTUVW  (k = X)
YZABCDEFGHIJKLMNOPQRSTUVWX  (k = Y)
ZABCDEFGHIJKLMNOPQRSTUVWXY  (k = Z)
```

Now suppose we switch to a general substitution cipher.  How many ciphertexts are there?  If we were to list them all it would be the same as the number of permutations of the alphabet.

But this is an impossibly large number: $26!  = 403291461126605635584000000.$

We could never brute force such a cipher on an ordinary computer. 

---


### Assignment

In the project folder you will see the following files and directories.

```
-rwxr-xr-x 1 hunter hunter   8856 Feb  3 11:29 clean*
-rw-r--r-- 1 hunter hunter    298 Feb  3 11:23 clean.cpp
-rwxr-xr-x 1 hunter hunter   9048 Feb  3 11:56 decrypt*
-rw-r--r-- 1 hunter hunter    689 Feb  3 11:56 decrypt.cpp
-rw-r--r-- 1 hunter hunter 159252 Feb  3 11:30 decrypt_me.txt
-rwxr-xr-x 1 hunter hunter   8752 Feb  3 12:02 encrypt*
-rw-r--r-- 1 hunter hunter    279 Feb  3 12:02 encrypt.cpp
-rw-r--r-- 1 hunter hunter 260837 Feb  3 11:31 encrypt_me.txt
drwxr-xr-x 2 hunter hunter   4096 Feb  3 12:09 example_backup/
-rwxr-xr-x 1 hunter hunter   9032 Feb  3 12:04 hist*
-rw-r--r-- 1 hunter hunter    441 Feb  3 11:41 histogram.cpp
-rw-r--r-- 1 hunter hunter  41467 Feb  3 12:09 x2.txt
-rw-r--r-- 1 hunter hunter 369464 Feb  3 11:32 x.clean
-rw-r--r-- 1 hunter hunter    234 Feb  3 11:43 x.hist
-rw-r--r-- 1 hunter hunter 481396 Feb  3 11:32 x.txt
-rw-r--r-- 1 hunter hunter 369464 Feb  3 11:34 y.txt
```

There are four source files, namely `clean.cpp`, `decrypt.cpp`, `encrypt.cpp`, and `histogram.cpp`.  Each of this is a program which you must implement, or finish implementing.(However `clean.cpp` is already complete and is included simply as an example of file IO).  Corresponding to these files you will also find executables `clean`,`decrypt`,`encrypt`,and `hist`. These are compiled versions of the corresponding source code (when the source code is implemented to specifications).  There are also some text files, `decrypt_me.txt`, `encrypt_me.txt`, `x2.txt`, `x.clean`, `x.hist`, `x.txt` and `y.txt`.  The first two of these are files that you must encrypt or decrypt with your working code, as described below.  The others are included as test cases to help you debug your programs, as we also cover in the following paragraphs.

I will now describe each source file and what you must do to make it work to specifications as part of a correct solution to this project. For your convenience I will also discuss compiling on Linux and some command line tools that will simplify your work.

#### `clean.cpp`

This file is included mostly as an example of file IO.  However it also solves the tedious problem of transforming normal English prose into an acceptable message in a shift cipher.  Namely, it removes all punctuation and converts all letters to upper case.  Let's look at the code.

```
#include <stdio.h>
#include <ctype.h>

int main()
{
	FILE* input = stdin;
	FILE* output = stdout;
	char c;
	while ((c=getc(input)) != EOF)
	{
		if(!(isalpha(c)))
			continue;
		c=toupper(c);
		putc(c,output);
	}
}
```
By default the program uses terminal input and output (`stdin` and `stdout`).  However if you want you can easily change to file IO (see the commented lines in `clean.cpp`). It gets characters from the keyboard until EOF is encountered (in Linux this is CTRL-D from the keyboard).  It then removes punctuation, and prints the letters entered in upper case.  You can run the program in a terminal like this.

```
./clean
```

The `./` is necessary because your project directory is not in the command path and so this executable must be specified exactly in the directory structure. In Linux the dot `.` is a quick reference to the current directory, so that `./clean` is equivalent (on my machine) to the command

```
/home/hunter/Dropbox/360_sprint_18/proj1/clean
```

which gives the full path to the executable. Your path will be different.  If you want to know the full path of your current directory, enter `pwd` which stands for Print Working Directory.  (None of this is relevant to the assignment, other than to answer natural questions about the weird way you execute the code)

Let's compile `clean.cpp`.  We already have a working executable, but this will illustrate how compilation works on this system.  Enter the following.

```
g++ clean.cpp
```

If all goes well (which it should) there will no output.  However a new file named `a.out` will have been added to your directory.  This is the default name of an executable created by the GNU C++ compiler `g++`.  You can run this executable just as you ran `clean`.  To use a custom executable name you can compile with the `-o` option:

```
g++ clean.cpp -o clean2
```
This will again compile `clean.cpp` but now the executable will be called `clean2`.

Let's use `clean` to do something useful.  You will notice that in your directory there is a file called `encrypt_me.txt`.  You can view the contents of this file through the cocalc file browser. However you can also see it from the command line by using this command:

```
cat encrypt_me.txt
```
The `cat` command dumps the contents of a file to terminal output.  Because `encrypt_me.txt` is very long, the text will go by too quickly for you to read it.  To solve this problem you can do this:

```
cat encrypt_me.txt | less
```

This uses the Unix pipe `|` feature, which is very useful.  It takes the output of the command on the left and makes it the input of the command on the right.  Thus this command is dumping out the contents of `encrypt_me.txt`, but rather than sending it to the screen it sends it to the program `less`.  The `less` program lets you use the arrows to navigate terminal output just as if it were a file.  You can also search the file with `/n` followed by the search term.  To quit `less` type `q`.

Just the way we piped `encrypt_me.txt` to `less`, we can pipe it to our executable `clean`.  Give this a try:

```
cat encrypt_me.txt | ./clean
```
or, if you prefer,
```
cat encrypt_me.txt | ./clean | less
```

You will see that this has the effect of cleaning up the book before it gets output to the screen. Even better, we can use Unix/Linux redirection to send the ultimate output directly to a file:

```
cat encrypt_me.txt | ./clean > encrypt_me.clean
```

If you now look at the contents of `encrypt_me.clean` (using `cat` or some other method) you will see that the contents of this file are the same as the terminal output we saw before.  This flexibility allows us to easily write programs with terminal IO and immediately use them as if we had implemented file IO.

Just as there is output redirection using the `>` symbol, there is similarly input redirection using the `<` symbol.  Try this:

```
./clean < encrypt_me.txt
```

and

```
./clean < encrypt_me.txt > encrypt_me.clean
```

Pretty neat, right? All of this is just practice to help you in developing and testing your other source files, `encrypt.cpp`, `decrypt.cpp`, and `hist.cpp`.

#### `encrypt.cpp`

This file should implement shift cipher encryption as described in the introduction.  I have given you a "skeleton" to complete:

```
#include <stdio.h>
#include <ctype.h>

int main()
{
	FILE* input = stdin;
	FILE* output = stdout;
	char c,k='K';
	while ((c=getc(input)) != EOF)
	{
		//YOUR CODE HERE//
		putc(c,output);
	}
}
```

There is basically only one line missing.  Note that the key is K by default. You can test your code in the following way:

```
~/Crypto_Spring_18/proj1$ cat x.clean | ./encrypt > yy.txt
~/Crypto_Spring_18/proj1$ diff yy.txt y.txt
~/Crypto_Spring_18/proj1$
```
If your code works correctly then `yy.txt` should be identical to `y.txt`.  The fact that this is so is confirmed by the fact that `diff` produces no output.

#### `decrypt.cpp`

This program converts a shift ciphertext back to the corresponding plaintext. Let's look at the code you have:

```
int main(int argc,char* argv[])
{
	check(argc,argv);
	char k = argv[1][0];
	printf("key = %c\n",k);
	FILE* input = stdin;
	FILE* output = stdout;
	char c;
	while ((c=getc(input)) != EOF)
	{
        /*YOUR CODE HERE*/
		putc(c,output);
	}
}
```

Like the encryption program, there is basically only one missing line.  But unlike the encryption progam, this program takes command line input.  If you are not familiar with how command line input works in C++ you can have a look at this short article:

https://www.geeksforgeeks.org/command-line-arguments-in-c-cpp/

The command line input that `decrypt` takes is the key. For instance this command decrypts the example file `y.txt` with the key K:

```
./decrypt K < y.txt
```

You can test your decrypt code by compiling it and verifying that it also correctly decrypts the `y.txt` file.

#### `histogram.cpp`

The starting point of any statistical attack on a substitution cipher is to first find the probability distribution of each of the characters that occur.  We can approximate this for long inputs by analyzing the relative frequency of each letter.  For example try this command.

```
./hist < x.clean
```

You should see the following output.

```
A: 0.079
B: 0.015
C: 0.025
D: 0.045
E: 0.129
F: 0.026
G: 0.020
H: 0.065
I: 0.063
J: 0.001
K: 0.007
L: 0.037
M: 0.026
N: 0.063
O: 0.077
P: 0.018
Q: 0.001
R: 0.065
S: 0.061
T: 0.096
U: 0.029
V: 0.009
W: 0.024
X: 0.001
Y: 0.017
Z: 0.001
```

This means that the character A is 7.9 percent of all letters in the file, E is 12.9 percent, etc.  Technically the relative frequency of A is defined by

$$rf(A) = \frac{\text{number of occurrences of A}}{\text{total number of letters}}$$

For the file `x.clean` this value turns out to be 0.079.  Now consider the output of this command:

```
./hist < y.txt
```

It should look like this:

```
A: 0.001
B: 0.065
C: 0.061
D: 0.096
E: 0.029
F: 0.009
G: 0.024
H: 0.001
I: 0.017
J: 0.001
K: 0.079
L: 0.015
M: 0.025
N: 0.045
O: 0.129
P: 0.026
Q: 0.020
R: 0.065
S: 0.063
T: 0.001
U: 0.007
V: 0.037
W: 0.026
X: 0.063
Y: 0.077
Z: 0.018
```

Observe that the frequency of K in `y.txt` matches the frequency of A in `x.clean`.  This correspondence can be used to infer which characters in `y.txt` correspond to which characters in `x.clean`.  This powerful attack will also work on a general substitution cipher, not just a shift cipher.  Your job is to implement `histogram.cpp` from scratch.  It is currently blank.  You can use the other files as an example of how to do the IO.

#### Encrypt and decrypt

Now that your code is done, use the tools you have created to do the following.

1.  Produce an encryption of the file encrypt_me.txt with key F. Call the resulting file encrypted_me.txt
2.  Decrypt the file decrypt_me.txt and call the result decrypted_me.txt.

You can find the key for `decrypt_me.txt` either by brute force, or by using your histogram function.
