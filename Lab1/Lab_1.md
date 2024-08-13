1. **Syntax Error**
   ```python
   print("hi)
   ```
   **A.** The code is missing a closing quotation mark. It should be:
   ```python
   print("hi")
   ```

2. **Runtime Error**
   ```python
   print(hello)
   ```
   **A.** The variable `hello` is not defined. Correct usage should be:
   ```python
   hello = "Hello, World!"
   print(hello)
   ```
   or
   ```python
   print("hello")
   ```

3. **Display a String Directly**
   ```python
   print("Hello, World!")
   ```
   **A.** This displays the greeting message directly.\
   ```python
   Hello, World!
   ```

4. **Display the Contents of a String Variable**
   ```python
   greeting = "Hello, Python!"
   print(greeting)
   ```
   **A.** This will display the contents of the string variable `greeting`.

5. **Display a String with Single Quotes**
   ```python
   print('Indian')
   ```
   **A.** This correctly displays a string containing single quotes.

6. **Display a String with Double Quotes**
   ```python
   print("Welcome to ABC")
   ```
   **A.** This correctly displays a string containing double quotes.

7. **Read Two Numbers and Perform Operations**
   ```python
   num1 = float(input("Enter the first number: "))
   num2 = float(input("Enter the second number: "))
   sum_ = num1 + num2
   difference = num1 - num2
   product = num1 * num2
   quotient = num1 / num2 if num2 != 0 else 'undefined'
   reminder = num1 % num2 if num2 != 0 else 'undefined'
   power = num1 ** num2
   ```
   **A.** This code reads two numbers and calculates various operations.

8. **Check if num1 is an Integer**
   ```python
   num1 = float(input("Enter a number: "))
   is_integer = num1.is_integer()
   print(f"Is num1 an integer? {is_integer}")
   ```
   **A.** This code checks if `num1` is an integer.

9. **Convert to Integer**
   ```python
   num1 = int(num1)
   print(num1)
   ```
   **A.** This code converts `num1` to an integer.

10. **Find Data Types**
    ```python
    print(type(num1))
    print(type(num2))
    ```
    **A.** This prints the data types of `num1` and `num2`.

11. **Read Float and Round to 2 Decimal Places**
    ```python
    float_value = float(input("Enter a float value: "))
    print(f"Rounded value: {round(float_value, 2)}")
    ```
    **A.** This rounds the float value to 2 decimal places.

12. **Read Float and Print Absolute Value**
    ```python
    float_value = float(input("Enter a float value: "))
    print(f"Absolute value: {abs(float_value)}")
    ```
    **A.** This prints the absolute value of the float.

13. **Store Different Types of Values**
    ```python
    string_var = "Hello"
    numeric_var = 123
    complex_var = 1 + 2j
    list_var = [1, 2, 3]
    dict_var = {"key": "value"}
    set_var = {1, 2, 3}
    tuple_var = (1, 2, 3)
    ```
    **A.** This code stores different types of values in variables.

14. **Find Data Type for Variables**
    ```python
    print(type(string_var))
    print(type(numeric_var))
    print(type(complex_var))
    print(type(list_var))
    print(type(dict_var))
    print(type(set_var))
    print(type(tuple_var))
    ```
    **A.** This prints the data type for each variable.

15. **Count Letters in a String**
    ```python
    greeting = "Welcome to Python Programming"
    letter_count = len(greeting.replace(" ", ""))
    print(f"Number of letters: {letter_count}")
    ```
    **A.** This counts the number of letters in the string excluding spaces.

16. **Combine First and Last Name**
    ```python
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    full_name = first_name + " " + last_name
    greeting_message = f"Hello, {full_name}!"
    print(greeting_message)
    ```
    **A.** This combines first and last names and a greeting message.

17. **Display String with Space**
    ```python
    print(first_name + " " + last_name)
    ```
    **A.** This displays the first and last names separated by a space.

18. **Display First Two Characters**
    ```python
    name = first_name + " " + last_name
    print(name[:2])
    ```
    **A.** This displays the first two characters of the full name.

19. **Display Last Three Characters**
    ```python
    print(name[-3:])
    ```
    **A.** This displays the last three characters of the full name.

20. **Display 3rd Character to Last Character**
    ```python
    print(name[2:])
    ```
    **A.** This displays from the 3rd character to the end of the full name.

21. **Display 3rd to 5th Character**
    ```python
    print(name[2:5])
    ```
    **A.** This displays characters from the 3rd to the 5th.

22. **Create and Modify a List**
    ```python
    food = ["Apple", "Banana"]
    food.append("Cherry")
    food.extend(["Date", "Elderberry"])
    print(food)
    ```
    **A.** This creates a list, appends, and extends it with more items.

23. **Count Number of Items in List**
    ```python
    print(len(food))
    ```
    **A.** This counts the number of items in the `food` list.

24. **Print the First Two Items Using Slicing Notation**
    ```python
    print(food[:2])
    ```
    **A.** This prints the first two items in the list.

25. **Print the Last Item Using Index Notation**
    ```python
    print(food[-1])
    ```
    **A.** This prints the last item in the list.

26. **Debug: Check if Number is Odd or Even**
    ```python
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")
    ```
    **A.** Corrects the code to check if a number is odd or even.

27. **Debug: Convert Centigrade to Fahrenheit**
    ```python
    c = float(input("Enter temperature in Centigrade: "))
    f = 9 * (c / 5) + 32
    print("Temperature in Fahrenheit is: ", f)
    ```
    **A.** Fixes the conversion formula and syntax issues.

28. **Debug: Sum and Average of Numbers**
    ```python
    count = int(input("Enter the count of numbers: "))
    summ = 0
    for i in range(count):
        x = int(input("Enter an integer: "))
        summ += x
    avg = summ / count
    print("The average is: ", avg)
    ```
    **A.** Corrects variable names and logic for summing and averaging numbers.


29. **Prove Mutability**
    - **Strings are Immutable:**
      ```python
      s = "hello"
      try:
          s[0] = 'H'
      except TypeError as e:
          print(e)  # Strings do not support item assignment
      ```
    - **Lists are Mutable:**
      ```python
      l = [1, 2, 3]
      l[0] = 10
      print(l)  # Lists support item assignment
      ```
    **A.** Demonstrates immutability of strings and mutability of lists.

