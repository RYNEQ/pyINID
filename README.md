
# pyINID
Iran National ID Tools

 - Check validity of Iran National ID as the following algorithm:

	![Checksum Algorithm](https://github.com/RYNEQ/pyINID/raw/master/formula.png)

	  (`checksum` will be the rightmost digit of National ID code )

 - Generate a random valid Iran National ID prefixed with desired numbers

## Installation

    [sudo -H ]pip(3) install pyinid

## Using  as a library
### Check validity
```python
import inid

if inid.check_id('0123456789'):
	print("Correct")
else: 
	print("Incorrect")
```
### Generate
```python
import inid
print(inid.generate_id())		# Completely Random
print(inid.generate_id('12345'))	# With Desired Prefix
print(inid.generate_id('123456789'))	# Only generate checksum
```
## Using  as a cli tool

    $ python3 -m inid


