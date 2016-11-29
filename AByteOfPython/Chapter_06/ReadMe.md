# Chapter 06 | Operators and Expressions #

Most line of code will contain *expressions.* A simple expression will be ` 2 + 4`. Any expression consist of two parts:-

* Operators 
* Operands

In the above expression, the Operators is `+`, and the operands are `2` and `4`.

## Operator ##

Here are some operators and there purpose are described below.

| Operator |              Purpose              |        Example         |
| :------: | :-------------------------------- | :--------------------: |
|    +     | Adds Operands                     |       2 + 3  = 5       |
|    -     | Subtracts Operands                |       2 - 3 = -1       |
|    *     | Multiply Operands                 |       2 * 3 = 6        |
|    **    | Power                             |       2 ** 3 = 8       |
|    /     | Divide Operands                   |        3/2 = 1         |
|    %     | Modulo Operands returns remainder |       13 % 3 = 1       |
|    <<    | left shift                        |       2 << 2 = 8       |
|    >>    | right shift                       |      11 >> 1 = 5       |
|    &     | Bit wise AND                      |       5 & 3 = 1        |
|    ^     | Bit wise XOR                      |       5 ^ 3 = 7        |
|    ~     | Bit wise invert                   |        ~5 = -6         |
|    <     | Less Than                         |     5 < 3 = false      |
|    >     | Greater Than                      |     5 > 3  = True      |
|    <=    | Less than or equal to             |     3 <= 4 = True      |
|    >=    | Greater than or equal to          |      4 > 3 = True      |
|    ==    | Equal to                          |     2 == 2 = True      |
|    !=    | not Equal to                      |     2 != 3 = True      |
|   not    | boolean NOT                       |    not True = False    |
|   and    | boolean AND                       | False and True = False |
|    or    | Boolean Or                        |  True or False = True  |


We can do math operation like shown in the table

````
5 + 6
````

But most of the time we are interested doing a math operation on a variable and then assigning the same to the variable. There is a shortcut in python for doing this like most of the programming language.

````
x = 1
x += 5
````

which means

````
x = 1
x = x + 5
````

## Evaluation Order ##

What is the way this expression is evaluated `2 + 3 * 5`, Now if we remembered the [BODMAS](http://en.wikipedia.org/wiki/Order_of_operations) rule, we will do the multiplication.

Shown below is the precedence table from low precedence to high, demonstrating which expression should be evaluated first. This is directly taken from [Python Reference ](https://docs.python.org/3/reference/expressions.html#operator-precedence)

| S. No |                  Operator                 |      Description       |
| :---: | :---------------------------------------- | :--------------------- |
|   1   | lambda                                    | Lambda Expression      |
|   2   | if-else                                   | Conditional Expression |
|   3   | or                                        | Boolean OR             |
|   4   | and                                       | Boolean AND            |
|   5   | not x                                     | Boolean NOT            |
|   6   | in, not in, is, is not, <, <=,>,>=, !=,== | Comparison, membership |
|   7   |                                           | BitWise OR             |
|   8   | ^                                         | BitWise XOR            |
|   9   | &                                         | Bitwise AND            |
|   10  | <<, >>                                    | shifts                 |
|   11  | +, -                                      | Addition Subtraction   |
|   12  | *, /, //, %                               | Multiplication         |
|   13  | +x,-x, ~x                                 | plus, minus, bitwise   |
|   14  | **                                        | Exponentiation         |
|   15  | x[i]                                      | Subscription           |
|   16  | (),[],{},                                 |                        |

In place of remembering such a big list, it is always good to use parenthesis, for changing the order of evaluation.

## Changing the order of Evaluation ##

To read an expression more readable we can use parenthesis, `2 + ( 3 * 4)`, which is easier to understand than `2 + 3 * 4`. Also care should be taken not to over do parenthesize like `(2 + (3 * 4))`. 

## Associativity ##

Operators are usually associated from left to right, This means that operator of the same precedence will be evaluated from left to right.

This expression `2 + 4 + 5` will be evaluated as `(2 + 4) + 5`.

Some operators have right to left associativity. like `a = b = c` will be evaluated as `a = (b = c)`







