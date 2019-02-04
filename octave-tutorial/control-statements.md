## Control Statements

```
>> for i=1:10,
v(i) = 2^i;
end;
>> v
v =

      2
      4
      8
     16
     32
     64
    128
    256
    512
   1024

>> for i=indices,
v(i)=2^i;
end;
>> v
v =

      2
      4
      8
     16
     32
     64
    128
    256
    512
   1024

>> i = 1;
>> while i <= 5,
v(i)=100;
i=i+1;
end;
>> v
v =

    100
    100
    100
    100
    100
     64
    128
    256
    512
   1024

>> i=1;
>> while true,
v(i)=999;
i=i+1;
if (i==6) break;
end;
end;
>> v
v =

    999
    999
    999
    999
    999
     64
    128
    256
    512
   1024

>> if v(1) == 1,
      disp('The value is one');
    elseif v(1) == 2,
      disp('The value is two');
    else
      disp('The value is not one and not two');
    end;
The value is two
```

```
>> squareThisNumber(5)
ans =  25
>> addpath('/USers/nordinhaouari');
>> squareAndCubeThisNumber(5)
ans =  25
>> [a,b] = squareAndCubeThisNumber(5)
a =  25
b =  125
```

```
>> X = [1 1;1 2;1 3]
X =

   1   1
   1   2
   1   3

>> y = [1;2;3]
y =

   1
   2
   3

>> theta = [0;1];
>> j = costFunctionJ(X,y,theta)
j = 0
>> theta = [0;0];
>> j = costFunctionJ(X,y,theta)
j =  2.3333
```