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
