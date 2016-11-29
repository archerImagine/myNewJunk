# Chapter 06 | Operators and Expressions #

Each python statement in some way or other will contain an **expression**. The most simplest expression will be like this, `3 + 4`. An expression consist of two things.

* **Operator**
    - Operator's depicts functionality, like we would like to do addition, subtraction etc. Operator can be a symbols like `+` in the above case or a special keywords.
* **Operands**
    - Operands are the data on which the Operator works on. In the above case `3` and `4` are operands.


## Operators ##

Major Operators available in Python can be classified as below.

* Arithmetic Operators
    - `+` : This adds two objects.
        + `3 + 4` gives `7`
        + `'a' + 'b'` gives `ab` which is string concatenation.
    - `-` : Subtraction of two numbers.
        + `-5.6` gives a negative number, because the first number is assumed to be `0`
        + `50 - 24` gives `26`
    - `*` : Multiplication.
        + `2 * 3` gives `6`
        + `'a' * 3` gives `aaa`, multiplication on string gives repetition of the string.
    - `**` : Power, returns x to the power y
        + `3 ** 4` gives `81`
    - `/` : Divide
        + `13/3` gives `1`
        + `13.0/3` gives `4.333`
    - `%` : modulo
        + Returns the remainder of the division.
        + `13 % 3` gives `1`
    - `//` : Floor Division
        + `9 // 2` gives `4`
* Comparison (Relational) Operators
    - `<` : less than
        + Returns weather `x` is less than `y`.
    - `>` : greater than
        + Returns weather `x` is greater than `y`.
    - `<=` : less than equal to.
        + Returns weather `x` is less than `y` or if it is equal.
    - `>=` : greater than equal to.
        + Returns weather `x` is greater than `y` or if it is equal.
    - `==` : equal to
        + Returns weather `x` is equal to `y`.
    - `!=` : not equal to
        + Returns weather `x` is not equal to `y`.
    - `<>` : not equal to.
* Assignment Operators
    - All the **Arithmetic Operators** can be used with assignment operator to update the value of the same variable.
    - `=` : Assign value
        + `c = a + b`, adds `a` and `b` and stores the value to `c`
    - `+=` : Updated the variable with `+` operation.
        + `a += 1` = `a = a + 1`
    - `-=` : Updated the variable with `-` operation.
        + `a -= 1` = `a = a - 1`
    - `*=` : Updated the variable with `*` operation.
        + `a *= 1` = `a = a * 1`
    - `/=` : Updated the variable with `/` operation.
        + `a /= 1` = `a = a / 1`
    - `%=` : Updated the variable with `%` operation.
        + `a %= 1` = `a = a % 1`
    - `**=` : Updated the variable with `**` operation.
        + `a **= 1` = `a = a ** 1`
    - `//=` : Updated the variable with `//` operation.
        + `a //= 1` = `a = a // 1`
* Logical Operators
    - The same `and`, `or` and `not` operator behave differently when the operands are different.
    - If the operands are boolean values it act as boolean operators.
    - When the operands are non boolean values it acts as logical operators. We will look into the Logical Operators here.
    - `and` : if all values are `True`, it returns the last evaluated value, else it returns the first evaluated value.
        + `a = 10` `b = 20` then `a and b` returns `20`
    - `or` : Returns the first True value else the last value.
        + `a = 10` `b = 20` then `a or b` returns `10`
    - `not` :  Returns `False` for a `True` value else `True`
* Boolean Operators
    - `not` : boolean NOT
        + if x is `True ` then, `not x` returns `False `
    - `and` : boolean and
        + `x and y` returns `False` if `x` is false, else it returns evaluation of `y`. This behavior is consistent with logical operation.
    - `or` : boolean OR
        + `x and y` returns `True` if `x` is True, else it returns evaluation of `y`. This behavior is consistent with logical operation.
* Bitwise Operators
    - `<<` : left shift
        + Shifts the bits of the number to the left by the number of bits specified.
        + `2 << 2` gives `8`, binary of `2` is `10`, after left shift by `2` it becomes `100` which is decimal `8`
    - `>>` : right shift
        + Shifts the bits of the number to the right by the number of bits specified.
        + `11 >> 1` gives `5`, binary of `11` is `1011` which after right shift by `1` becomes `101` which is `5` in decimal.
    - `&` : bitwise and
        + Operator copies a bit to the result if it exists in both operands
        + `5 & 3` returns `1`, because, the binary of `5` is `101` and `3` is `11`, so the only bit set are last digit, so the output will be `1`.
    - `|` : bitwise or.
        + It copies a bit if it exists in either operand.
        + `5 | 3` gives `7`, because the binary of `5` is `101` and of `3` is `11`, so he output becomes `111`, with all the bit set, so the decimal is `7`.
    - `^` : bitwise XOR
        + It copies the bit if it is set in one operand but not both.
        + `5 ^ 3` gives `6`, because the binary of `5` is `101` and of `3` is `11`, so the output become `110`, which is binary equivalent of `6`.
    - `~` : bitwise invert.
        + It is unary and has the effect of 'flipping' bits.
        + `~x` = `-(x + 1)`
* Membership Operators
    - There is Membership operator in Python, which checks the presence of an member in a list, tuple, strings.
    - `in` : Returns `True ` if the member is available in the sequence.
        + `x in y` : returns `True ` if the member `x` is present in `y`.
    - `not in` : Returns `True ` if the member is not available in the sequence.
        + `x not in y` : returns `True ` if the member `x` is not present in `y`.
* Identity Operators
    - Identity Operators checks the memory location of two object.
    - `is` : Returns `True ` if both operands points to the same object.
        + `a = b = "Hello` then `a is b` returns `True `
    - `not is` : Returns `True ` if both operands points to the different object.
        + `a = b = "Hello` then `a is not b` returns `False `.
## Evaluation Order | Operator Precedence ##

We have operator precedence coming into picture if we have expression like `2 + 3 * 5`. In place of using expression like this we can have `()` parentheses to solve the precedence as we want, so the above expression can be changed to `(2 + 3) * 5`.

