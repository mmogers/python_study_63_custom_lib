# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## It's... undefinable!

👉 Why is it not importing my file?


```python

import test

print("Countdown")
countdown()
```

<details> <summary> 👀 Answer </summary>

We've not referenced the `countdown()` subroutine as belonging to the `test` file on line 3.

```python
import test

print("Countdown")
test.countdown()
```

</details>

## It's Running The Subroutine Twice?

👉 What is the problem here?
```python
import test

print("Countdown")
test.countdown()
```

<details> <summary> 👀 Answer </summary>

This is a cunning one, the error is *not in the main.py file*.  In fact, it's because we've called the `countdown()` subroutine **inside the test.py file**.

Be careful to remove any internal subroutine calls in separate files, especially if you're copying code over from other programs.

This is the code from the **test.py** file:
```python

def countdown():
  for i in range(10):
    print(i+1)

countdown() # Remove this line
```
</details>

