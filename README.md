# The Simple Python Profiler - `tspp`

If you are looking for a very simple profiler that lets you measure the time each part of your programs took, `tspp` is for you!

`tspp` typically replaces code that would look like:

```python
start = time.time()
do_something()
print "do_something took", time.time() - start
```

## Example usage
```python
import time
from tspp import Profiler

pr = Profiler()

def do_something():
    time.sleep(0.1)

for i in xrange(10):
    pr.register("start")
    do_something()
    pr.register("end of do_something")
print pr.profile()
```

## Install
`git clone` this repo, `cd` to the repo, then run `pip install ./`.
