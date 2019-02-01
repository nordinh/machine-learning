## Moving data around
```
>> A = [1 2;3 4;5 6]
A =

   1   2
   3   4
   5   6

>> size(A)
ans =

   3   2

>> sz = size(A)
sz =

   3   2

>> size(sz)
ans =

   1   2

>> size(A,1)
ans =  3
>> size(A,2)
ans =  2
>> v = [1 2 3 4]
v =

   1   2   3   4

>> length(v)
ans =  4
```

```
>> pwd
ans = /Users/nordinhaouari
>> cd '/Users/nordinhaouari/Documents/workspace/machine-learning/octave-tutorial'
>> pwd
ans = /Users/nordinhaouari/Documents/workspace/machine-learning/octave-tutorial
>> ls
basic-operations.md	moving-data-around.md	octave-workspace
>> load featuresX.dat
>> who
Variables in the current scope:

A    ans  sz   v    w

>> whos
Variables in the current scope:

   Attr Name        Size                     Bytes  Class
   ==== ====        ====                     =====  ===== 
        A           3x2                         48  double
        ans         1x73                        73  char
        sz          1x2                         16  double
        v           1x4                         32  double
        w           1x10000                  80000  double

Total is 10085 elements using 80169 bytes

>> clear sz
>> who
Variables in the current scope:

A    ans  v    w

>> v = w(1:10)
v =

   -0.87185   -5.78726   -1.74725   -5.10960  -10.77408   -6.72481   -7.93634   -7.07257   -4.88679   -7.56749

>> save hello.mat v;
>> ls
basic-operations.md	hello.mat		moving-data-around.md	octave-workspace
>> clear
>> who
>> load hello.mat
>> who
Variables in the current scope:

v

>> save hello.txt v -ascii
```

```
>> A = [1 2;3 4;5 6]
A =

   1   2
   3   4
   5   6

>> A(3,2)
ans =  6
>> A(2,:)
ans =

   3   4

>> A(:,2)
ans =

   2
   4
   6

>> A
A =

   1   2
   3   4
   5   6

>> A([1 3],:)
ans =

   1   2
   5   6

>> A(:,2)
ans =

   2
   4
   6

>> A(:,2) = [10;11;12]
A =

    1   10
    3   11
    5   12

>> A = [A, [100;101;102]]
A =

     1    10   100
     3    11   101
     5    12   102

>> A(:)
ans =

     1
     3
     5
    10
    11
    12
   100
   101
   102

>> A = [1 2;3 4;5 6]
A =

   1   2
   3   4
   5   6

>> B = [10 20;30 40;50 60]
B =

   10   20
   30   40
   50   60

>> C = [A B]
C =

    1    2   10   20
    3    4   30   40
    5    6   50   60

>> [A,B]
ans =

    1    2   10   20
    3    4   30   40
    5    6   50   60


```