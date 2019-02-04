
# pyINID
Iran National ID Tools

 - Check validity of Iran National ID as the following algorithm:

	![ds = \sum_{n=1}^{10} \frac{1}{10^n}(x \bmod 10^{n + 1} - x \bmod 10^n) \times (n+1)  \\  
m = ds \bmod 11  \\
checksum = \left(m \lt 2 \rightarrow m \right)\wedge\left(m \ge 2 \rightarrow 11 - m\right)](http://mathurl.com/render.cgi?%5Ctextmode%20ds%20=%20%5Csum_%7Bn=1%7D%5E%7B10%7D%20%5Cfrac%7B1%7D%7B10%5En%7D%28x%20%5Cbmod%2010%5E%7Bn%20%20%201%7D%20-%20x%20%5Cbmod%2010%5En%29%20%5Ctimes%20%28n%201%29%20%20%5C%5C%0A%5C%5C%0Am%20=%20ds%20%5Cbmod%2011%20%20%5C%5C%0A%5C%5C%0Achecksum%20=%20%5Cleft%28m%20%5Clt%202%20%5Crightarrow%20m%20%5Cright%29%5Cwedge%5Cleft%28m%20%5Cge%202%20%5Crightarrow%2011%20-%20m%5Cright%29%5Cnocache)

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


