# A library capable of implementing TOPSIS

```
PROJECT 1, UCS633 - Data Analysis and Visualization
Nikhil Gupta  
COE17
Roll number: 101703371
```
Output is the best allternative out of list of all allternatives. Other ranks are streamed to the csv file.

`Best Attribute: Mobile 3`

## Installation
`pip install topsispack_NG`

*Note the name has an underscore not a hyphen. If installation gives error or package is not found after installing, install as sudo.*

*Recommended - test it out in a virtual environment.* 

## To use via command line
`Topcli myData.csv "1,1,1,1" "-,+,+,+"`

First argument after nikcli is the location of the .csv file. The weights and impacts should be passed as strings in double quotes with each weight or impact separated by a comma (',').

## To use in .py script
```
from toplib.models import topsis
topsis(['myData.csv',"1,1,1,1","-,+,+,+"])
```

The argument passed should be a list.

*Can email me for any issues or suggestions*
