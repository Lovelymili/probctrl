
# probctrl

`probctrl` 是一个轻量的 Python 装饰器库，支持三种函数执行控制方式：

- `@p(prob)`：按概率触发函数
- `@delay(seconds)`：延迟指定秒数后异步执行
- `@throttle(rate)`：限制函数每秒最大调用频率，超过频率后将自动延迟执行

## 安装

```bash
pip install probctrl
```

## 示例

```python
from probctrl import p, delay, throttle

@p(0.5)
def maybe_func():
    print("有 50% 的概率会执行")

@delay(2)
def delayed_func():
    print("这个函数会延迟 2 秒异步执行")

@throttle(3)
def throttled_func():
    print("受节流控制的函数")
```
