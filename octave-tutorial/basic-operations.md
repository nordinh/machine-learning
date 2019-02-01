## Basic operations
run octave
```
/usr/local/octave/3.8.0/bin/octave-3.8.0
```

```
octave:1> 5+6
ans =  11

octave:2> 3-2
ans =  1

octave:3> 5*8
ans =  40

octave:4> 1/2
ans =  0.50000

octave:5> 2^6
ans =  64

octave:6> 1==2
ans = 0

octave:7> 1~=2
ans =  1

octave:8> 1&0
ans = 0

octave:9> 1||0
ans =  1

octave:10> xor(1,0)
ans =  1
```

Changing prompt to '>> '
```
octave:10> PS1('>> ');
>> a=pi
a =  3.1416
>> disp(a)
 3.1416
>> disp(sprintf('2 decimals; %0.2f', a))
2 decimals; 3.14
>> format long
>> disp(a)
 3.14159265358979
>> format short
>> disp(a)
 3.1416
```

### Vectors and matrices
```
>> A = [1 2;3 4;5 6]
A =

   1   2
   3   4
   5   6

>> A = [1 2;
> 3 4;
> 5 6]
A =

   1   2
   3   4
   5   6

>> v = [1 2 3]
v =

   1   2   3

>> v = [1;2;3]
v =

   1
   2
   3

>> v = 1:0.1:2
v =

    1.0000    1.1000    1.2000    1.3000    1.4000    1.5000    1.6000    1.7000    1.8000    1.9000    2.0000

>> v = 1:6
v =

   1   2   3   4   5   6

>> ones(2,3)
ans =

   1   1   1
   1   1   1

>> C = 2*ones(2,3)
C =

   2   2   2
   2   2   2

>> w = ones(1,3)
w =

   1   1   1

>> w=zeros(1,3)
w =

   0   0   0

>> w=rand(1,3)
w =

   0.95620   0.47586   0.75228

>> rand(3,3)
ans =

   0.904017   0.633570   0.065152
   0.523243   0.959812   0.292227
   0.296555   0.193027   0.176185

>> rand(3,3)
ans =

   0.1242736   0.5963322   0.0059890
   0.6284632   0.8453573   0.2564052
   0.4415182   0.0345599   0.4621422

>> w = randn(1,3)
w =

  -0.41749  -0.10195  -0.21417

>> w = randn(1,3)
w =

   0.39390  -1.44820   1.21392

>> w=-6 + sqrt(10)*randn(1,10000);
>> hist(w)
>> hist(w, 50)

>> eye(4)
ans =

Diagonal Matrix

   1   0   0   0
   0   1   0   0
   0   0   1   0
   0   0   0   1

>> eye(3)
ans =

Diagonal Matrix

   1   0   0
   0   1   0
   0   0   1

>> help eye
>> help rand
>> help help
```