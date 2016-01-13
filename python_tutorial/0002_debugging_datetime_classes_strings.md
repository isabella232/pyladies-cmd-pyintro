Debugging, working with datetime, classes
======

The examples used so far are easy to try out, but it is not possible to save the work for later.

For that case we will save program code into a text file and then feed that text file to python interpreter.

# Preparation

Open Windows Power Shell and go to your Desktop, where create a folder called 'python_tutorial'.

```

Open Notepad++ by going to 'Start Menu' -> typing Notepad, then clicking on Notepad++.

TODO: Add screenshots

We're going to use python datetime standard module, meaning whenever python is installed this module is available.

[Datetime documentation](https://docs.python.org/2/library/datetime.html)

* [datetime.timedelta](https://docs.python.org/2/library/datetime.html#datetime.timedelta)
* [datetime.datetime](https://docs.python.org/2/library/datetime.html#datetime.datetime)

Type the following into notepad++ and save it as `seconds_since_midnight.py` this program is supposed to display the number of seconds since midnight

```python

from datetime import datetime, timedelta

now = datetime.now()
today = datetime(now.year, now.month, now.day)

difference = now - today

print("Seconds since midnight: " + difference)

```

Now open Windows PowerShell and go to `Desktop\python_tutorial` then run the program:

```
python.exe seconds_since_midnight.py
```

TODO: add screenshot.

As you see right now, the program doesn't work. We are going to debug it. See how this term has come about in [Wikipedia article](https://en.wikipedia.org/wiki/Debugging#Origin)

There's obviously a problem with mashing `datetime.timedelta` object with a string, first thing we can do is to print out just the `difference` object and see how it looks, this approach will work just fine for a small program, however for larger programs especially the once that output lots of things to the console, the output might get drown out by other things, another problem is that we're changing the source code, and after we're done we'll have to go and hunt for all the print statements; source control tools partially solve the problem, but do we really need to write code that we're never going to run?

An easier solution is to use [python debugger -- pdb](https://docs.python.org/2/library/pdb.html). Basically it gives us python REPL with all of the variables already loaded, so we can try and determine what is about to go wrong with the program.
After reading the error message, we know that the program is going to crash on line ` N  ` with the error message `  `. So on the line ` N - 1 ` we're gonna add this statement that imports debugger module and activates the debugger

```python
import pdb; pdb.set_trace()
```

There are few commands available like `n` - execute next line, `c` - continue running the program or `q` - quit the program. **Exercise: ** try these commands, as they promptly crash the program.

This investigating technique is effective when program doesn't crash and you're just looking for the code looking where things might have gone wrong, in this case, we can use post-mortem debugger, where you don't need to modify any source code as the debugger gets loaded after program crashes


```
    C:\Users\Alex\Desktop\python_tutorial\python.exe -m pdb seconds_since_midnight.py
```
