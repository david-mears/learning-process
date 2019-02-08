Developing a process for tackling problems in an unfamiliar language
====================================================================

My current process:

- (I tackle the logic of the problem in a language-neutral way - break it down into steps before writing)
- Find a cheatsheet for the language in question
- Find a linter
- Test small necessary elements (e.g. print statements) in a REPL before adding them to the program (read the error messages)
- Keep running the program every time I add a change, to prevent errors compounding

Applied to python:

```
def fizzbuzz(number):
  output = ''
  if number % 3 == 0:
    output = output + 'fizz'
  if number % 5 == 0:
    output = output + 'buzz'
  if output == '':
    return number
  return output

for i in range(1, 101):
    print(fizzbuzz(i))
```
