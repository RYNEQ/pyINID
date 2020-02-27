
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
   or use class based approach: 

```python
import inid

obj1 = inid.INID("0012345679")
obj1.is_valid() # True

obj2 = inid.INID("001234567")  # incomplete
obj1.value  # True

# iterate through all NIDs
for nid in inid.INID_RANGE():
	print(nid)

# all NIDs for one/multiple cities
for nid in inid.INID_RANGE(city_codes=inid.CITY_CODES['تهران']['تهران مرکزی']):
	print(nid)

# all NIDs for one/multiple cities from a range
for nid in inid.INID_RANGE(100, 777, city_codes=inid.CITY_CODES['تهران']['تهران مرکزی']):
	print(nid)
	
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


