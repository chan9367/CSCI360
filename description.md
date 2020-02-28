### Project 5

#### Discrete Logarithm Problem

*Honor Code Statement:  This project asks you to implement a standard algorithm.  In all situations like this it is possible to find a solution online and use that to help you form your own solution.  But this is not allowed and everyone is on their honor not to do this.*

Suppose $p$ is prime and $\alpha \in \mathbb{Z}_p^*$.  The *order* of $\alpha$ is the least positive integer $k$ such that $\alpha^k \equiv 1 \mod p$.  Suppose that for some unknown integer $x$, 

$$\beta \equiv \alpha^x \mod p.$$

We know $\beta$ and want to know the secret value $x$.  This is called the *discrete logarithm problem* (in $\mathbb{Z}_p^*$).

One way to find $x$ is to simply try all powers $x=0,1,\ldots,k-1$ where $k$ is the order of $\alpha$.  But in cryptographic situations this will be infeasible.  There are ways of finding $x$ that are much faster than brute force, however.  These are discussed in our textbook in Chapter 8, beginning on page 221. 

The first method presented is called *Shanks' Baby-Step Giant-Step Method*.  (If you haven't read that material, please take a break from reading this and give it a once-over--if you don't have your book handy the PDF of Understanding Cryptography is easy to find online.)  The BSGS method can solve the discrete logarithm problem in $\mathbb{Z}_p^*$ where $p$ is a $n$ bit prime in $O(\sqrt{n})$ time and $O(\sqrt{n})$ space.   

In this project we will implement BSGS to crack the discrete log problem when $p$ is 42 bits.  (This is long enough to resist brute force on Cocalc. ).  Thus, with BSGS, we need about 21 bits of space and time to execute about $2^{21}$ steps, both of which are available even on Cocalc.  

Our numbers will be $\beta = 1682398169711$, $p = 1799431327777$, and $\alpha = 2$. In the notation used in the book, $|G| = p-1$.  In this directory you will find a skeleton solution in the file `shanks.cpp`.  Please complete the code in this file to find a value $x$ such that $\alpha^x \equiv \beta \mod p$. 

#### Notes on the code

In `shanks.cpp` notice that you already have fast modular exponentiation available in the function called `power()`.  You might observe that we're not quite using normal integers in this code.  We're using 128 bit integers, which I've type defined to be a `number` type.  The point of doing it this way is we can work with larger integers (or even GMP integers) by changing only the line of code where `number` is typedef-ed.  We can't quite use unsigned longs for our integer type because the square and multiply algorithm needs at least $2\cdot42 = 84$ bit integers, and unsigned longs are 64 bits. 

Another thing to notice is that for the table we're using the C++ type called `map`.  Some of you may not have used `map` before. It's not that straightforward to use, but it's probably the easiest way of creating the necessary table.  You can find a lot of tutorials online by Googling "C++ map example" and things like that.  [Here](https://www.studytonight.com/cpp/stl/stl-container-map) is one you might use. 

Feel free to create a Sage worksheet in this directory for scratchwork and for computing handy values (such as $m = \lceil \sqrt{p-1} \,\rceil$)
 
### Project 5

#### Discrete Logarithm Problem

*Honor Code Statement:  This project asks you to implement a standard algorithm.  In all situations like this it is possible to find a solution online and use that to help you form your own solution.  But this is not allowed and everyone is on their honor not to do this.*

Suppose $p$ is prime and $\alpha \in \mathbb{Z}_p^*$.  The *order* of $\alpha$ is the least positive integer $k$ such that $\alpha^k \equiv 1 \mod p$.  Suppose that for some unknown integer $x$, 

$$\beta \equiv \alpha^x \mod p.$$

We know $\beta$ and want to know the secret value $x$.  This is called the *discrete logarithm problem* (in $\mathbb{Z}_p^*$).

One way to find $x$ is to simply try all powers $x=0,1,\ldots,k-1$ where $k$ is the order of $\alpha$.  But in cryptographic situations this will be infeasible.  There are ways of finding $x$ that are much faster than brute force, however.  These are discussed in our textbook in Chapter 8, beginning on page 221. 

The first method presented is called *Shanks' Baby-Step Giant-Step Method*.  (If you haven't read that material, please take a break from reading this and give it a once-over--if you don't have your book handy the PDF of Understanding Cryptography is easy to find online.)  The BSGS method can solve the discrete logarithm problem in $\mathbb{Z}_p^*$ where $p$ is a $n$ bit prime in $O(\sqrt{n})$ time and $O(\sqrt{n})$ space.   

In this project we will implement BSGS to crack the discrete log problem when $p$ is 42 bits.  (This is long enough to resist brute force on Cocalc. ).  Thus, with BSGS, we need about 21 bits of space and time to execute about $2^{21}$ steps, both of which are available even on Cocalc.  

Our numbers will be $\beta = 1682398169711$, $p = 1799431327777$, and $\alpha = 2$. In the notation used in the book, $|G| = p-1$.  In this directory you will find a skeleton solution in the file `shanks.cpp`.  Please complete the code in this file to find a value $x$ such that $\alpha^x \equiv \beta \mod p$. 

#### Notes on the code

In `shanks.cpp` notice that you already have fast modular exponentiation available in the function called `power()`.  You might observe that we're not quite using normal integers in this code.  We're using 128 bit integers, which I've type defined to be a `number` type.  The point of doing it this way is we can work with larger integers (or even GMP integers) by changing only the line of code where `number` is typedef-ed.  We can't quite use unsigned longs for our integer type because the square and multiply algorithm needs at least $2\cdot42 = 84$ bit integers, and unsigned longs are 64 bits. 

Another thing to notice is that for the table we're using the C++ type called `map`.  Some of you may not have used `map` before. It's not that straightforward to use, but it's probably the easiest way of creating the necessary table.  You can find a lot of tutorials online by Googling "C++ map example" and things like that.  [Here](https://www.studytonight.com/cpp/stl/stl-container-map) is one you might use. 

Feel free to create a Sage worksheet in this directory for scratchwork and for computing handy values (such as $m = \lceil \sqrt{p-1} \,\rceil$)
 
