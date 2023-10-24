# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
## test.py file ##############
import random

num = randint(10,100)

def countdown():
  for i in range(num):
    print(i+1)

countdown()
### main.py file ###############

import tt

print("Countdown")
countdown()

```

<details> <summary> 👀 Answer </summary>

```python
## test.py file ##############
import random

num = random.randint(10,100) # Need the random. to refer to the random library

def countdown():
  for i in range(num):
    print(i+1)

# Removed internal subroutine call.

### main.py file ###############

import test as tt # No such file as tt, that's the nickname I want to give the 'test' file

print("Countdown")
tt.countdown() # Referenced 'tt' file nickname before the call.

```

</details>