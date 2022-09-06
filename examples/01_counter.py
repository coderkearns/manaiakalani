from .. import Observable

count = Observable(0)


@count.subscribe
def unsubscribe(value, old_value):
    print("[count]", old_value, "->", value)


# or: unsubscribe = count.subscribe(lambda value, old_value: print("[count]", old_value, "->", value))

print("Count is", count())  # => Count is 0

count.set(count() + 1)  # => [count] 0 -> 1
count.set(count() + 1)  # => [count] 1 -> 2
unsubscribe()
count.set(count() + 1)  # *Does not print, but count is now 3*

print("Count is", count())  # => Count is 3
