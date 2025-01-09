## 机考Cheet sheet

刘子龙 物理学院 2024.12.26

#### 0.提醒：注意浅拷贝

#### 1.各种import

###### 1.1 deque

```python
from collections import deque
q=deque()
q.pop(); q.popleft() ;q.append()
```

###### 1.2 defaultdict

```python
from collections import defaultdict
dic1=defaultdict(int)
dic2=defaultdict(list)
dic3=defaultdict(lambda :-1) #默认值为-1
```

###### 1.3 cmp_to_key

```python
from functools import cmp_to_key
def compare(x,y):
    if y应在x前面:
        return 1
    else:
        return -1
lst.sort(key=cmp_to_key(compare))
```

###### 1.4 lru_cache

```python
from functools import lru_cache
@lru_cache(maxsize=None)
def dfs():
```

###### 1.5 bisect

保顺序的插入的最左/最右可能位置

```python
from bisect import bisect_left,bisect_right
```

###### 1.6 heapq

```python
import heapq
heapq.heappush,heappop,heapify
```

#### 2.输入输出

```python
import sys
data=sys.stdin.read()
lines=data.split()
#lines[0],lines[1],...
```

```python
print("%d %s %.3f" % (1,"2",3.00))
```

#### 3.位运算

```python
& 与 1+1 ->1
| 或 1+1 or 1+0 or 0+1 ->1
^ 异或 1+0 or 0+1 ->1
<<:*2, >>://2 左移、右移
```



