age: int
name: str
height: float
is_human: bool


# specify the type of data to be taken in
# to decrease risk of type casting errors
def age_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if age_check(12):
    print("You may pass")
else:
    print("Pay a fine.")







