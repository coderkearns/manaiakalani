from .. import Observable, derived

first_name = Observable("John")
last_name = Observable("Doe")


@derived([first_name, last_name])
def full_name():
    return f"{first_name()} {last_name()}"


first_name.subscribe(lambda v, ov: print("first_name", ov, "->", v))
last_name.subscribe(lambda v, ov: print("last_name", ov, "->", v))
full_name.subscribe(lambda v, ov: print("full_name", ov, "->", v))

print("First Name is", first_name())  # => First Name is John
print("Last Name is", last_name())  # => Last Name is Doe
print("Full Name is", full_name())  # => Full Name is John Doe

first_name.set("Jane")
# (=> full_name John Doe -> Jane Doe) and (=> first_name John -> Jane)

print("Full Name is", full_name())  # => Full Name is Jane Doe
