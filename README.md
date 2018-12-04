# The Simple Python Profiler - `tspp`

If you are looking for a very simple profiler that lets you measure the time each part of your programs took, `tspp` is for you!

`tspp` typically replaces code that would look like:

```python
start = time.clock()
do_something()
print "do_something took", time.clock() - start
```

## Example usage
```python
import time
from tspp import Profiler

pr = Profiler()

def do_something():
    for i in xrange(100000):
    	pass

for i in xrange(10):
    pr.register("start")
    do_something()
    pr.register("end of do_something")
print pr.profile()
```

Which outputs something like
```
Profiling 
	Total: 0.013912
	start 5.1e-05 0.37%
	end of do_something 0.013861 99.63%
```

## Install
`git clone` this repo, `cd` to the repo, then run `pip install ./`.
