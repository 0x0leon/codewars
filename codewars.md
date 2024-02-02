# upside down numbers



0 - 10
10 - 19
100 - 999
1000 - 9999
10000 - 99999
100000 - 999999

```python
def check_pblt(x):
	return dict(list(spinners.items())[x:])

def generate_pre_number(x, y):
	'''recursive function to find all following bases of 10'''
	bases = []
	# check if number % 10
		# if not then find next % 10
	# generate 10 * 10 if number kleiner y 
	''' 10 - 100 - 1000 '''
	if x % 10 == 0:
		bases.append(x)
	else:
		# findNext10Base()
		# add to bases
	return generate_pre_numbers(x * 10, y)


for x in num:
	check_pblt(x)
	
```