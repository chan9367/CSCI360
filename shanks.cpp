#include<stdio.h>
#include<iostream>
#include<assert.h>
#include <string.h>
#include <map>
/* Compile with:

g++ shanks.cpp 

*/


using namespace std;

typedef __int128 number;

/* Square and multiply function to calculate (x^y)%p in O(log y) */
// based on code from here: https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
unsigned long power(number x, number y, number p)
{
    unsigned long res = 1;      // Initialize result
    x = x % p;  // Update x if it is more than or
                // equal to p
    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y & 1)
            res = (res*x) % p;
        // y must be even now
        y = y>>1; // y = y/2
        x = (x*x) % p;
        //cout << x << " " << y << endl;
    }
    return res;
}


int main()
{
  number beta = 1682398169711;
  number p = 1799431327777;// |G| = p-1
  number alpha = 2;
  
  number m=1341429; //found in sage via m=ceil(sqrt(p-1))

  map<number,number> table;
  number x_g =0;
  number x_b =0;
    
  /*Your work here...*/
  for(number i=2; i<=m-1; i++){ //store all values of alpha^x_b into a table i.e. baby step
    x_b=i;
    table[power(alpha,x_b,p)]=i;
  }

  number amm=1522793735228, val, k=2;        //value of amm found in sage via G = Zmod(1799431327777) then alpha = G(2) then (1/alpha)^m
  
  for (number i=2; i<=m-1; i++){  //find x_g and x_b based on which entry in map has the value beta*(alpha^-m)^x_g. 
    x_g=i;
    val = (power(amm,x_g,p)*beta)%p;
    if (table.count(val)>0){
        x_b=table.at(val);
        x_g=i;
        break;
      }
    } //when an entry's value is the same as beta*(alpha^-m)^x_g, it means we found x_b and x_g

  /* Use baby step giant step to find x_g,x_b*/  
  cout <<"x_g is: "<< (unsigned long) x_g << "\t" <<"x_b is: "<< (unsigned long) x_b << endl;

  number x = x_g*m + x_b;
  if (power(alpha,x,p)==beta)
  {
    cout << "match!" << endl;
  } else {
    cout << "failure" << endl;
  }
 
  cout << "x = " << (unsigned long) (x_g*m + x_b) << endl;
  
  cout << (unsigned long) power(1002,621,4969)<<endl;
  cout << (unsigned long) power(1002,184,4969)<<endl;
  cout << (unsigned long) power(1002,4668/23,4969)<<endl;


}