AIM to write a pythn function that computes more than one result and returns all of them to the caller in a single return statement

def divide_parts(dividend, divisor):
    """Return quotient, remainder, is_exact, message"""

    if divisor == 0:
        return None, None, False, "Cannot divide by zero"

    q = dividend // divisor
    r = dividend % divisor
    exact = (r == 0)

    msg = "Exact division" if exact else "Remainder left over"

    return q, r, exact, msg


tests = [(17, 5), (20, 4), (9, 0), (-13, 4)]
for a, b in tests:
    q, r, exact, msg = divide_parts(a, b)
    print(f"{a} ÷ {b} → q = {q}, r = {r}, exact = {exact} ({msg})")



output--

17 ÷ 5 → q = 3, r = 2, exact = False (Remainder left over)
20 ÷ 4 → q = 5, r = 0, exact = True (Exact division)
9 ÷ 0 → q = None, r = None, exact = False (Cannot divide by zero)
-13 ÷ 4 → q = -4, r = 3, exact = False (Remainder left over)

-------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------
AIM TO WRITE A FUNCTION WHOSE PARAMETERS HAVE FALL BAK VALUES SO THE CALLER MAY OMIT THEM 

def power(base, exp=2):
    return base ** exp


def pad(text, width=12, fill="*"):
    text = str(text)

    if len(text) >= width:
        return text

    extra = width - len(text)
    left = extra // 2
    right = extra - left

    return fill * left + text + fill * right


def add_item_wrong(item, box=[]):
    """BAD default. The same list is reused for every call."""
    box.append(item)
    return box


def add_item_right(item, box=None):
    """GOOD default. A fresh list is made when the caller sends nothing."""
    if box is None:
        box = []

    box.append(item)
    return box


print("power(5) =", power(5))
print("power(5, 3) =", power(5, 3))

print("pad('LAB') =", pad("LAB"))
print("pad('LAB', 10, '-') =", pad("LAB", 10, "-"))

print("wrong 1st call:", add_item_wrong("pen"))
print("wrong 2nd call:", add_item_wrong("ink"))

print("right 1st call:", add_item_right("pen"))
print("right 2nd call:", add_item_right("ink"))


OUTPUT
power(5) = 25
power(5, 3) = 125
pad('LAB') = ****LAB*****
pad('LAB', 10, '-') = ---LAB----
wrong 1st call: ['pen']
wrong 2nd call: ['pen', 'ink']
right 1st call: ['pen']
right 2nd call: ['ink']


----------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------

AIM  TO COUNT THE CHARACTERS IN A STRING WITHOUT CALLING len() str.count(), or any imported module

def length_while(text):
    count = 0

    while True:
        try:
            text[count]
            count += 1
        except IndexError:
            return count


def length_recursive(text):
    if text == "":
        return 0
    return 1 + length_recursive(text[1:])


def string_length(text):
    count = 0

    for ch in text:
        count = count + 1

    return count


word = "laboratory"

print("while :", length_while(word))
print("recursive :", length_recursive(word))
print("for-loop :", string_length(word))


OUTPUT

while : 10
recursive : 10
for-loop : 10

------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------
AIM  TO DECIDE WHETHER ONE STRING ( THE PIECE/NEDDLE) OCCURS INSIDE ANOTHER STRING ( THE TEXT / HAYSTACK)

def locate_all(text, piece, ignore_case=True):
    source = text.lower() if ignore_case else text
    target = piece.lower() if ignore_case else piece

    hits = []
    n = len(source)
    m = len(target)

    if m == 0:
        return []

    i = 0
    while i <= n - m:
        if source[i:i + m] == target:
            hits.append(i)
        i = i + 1

    return hits


text = "The Python laboratory teaches PYTHON strings."
piece = "python"

hits = locate_all(text, piece, ignore_case=True)

print("Text :", text)
print("Needle :", piece)
print("Found :", len(hits) > 0)
print("Count :", len(hits))
print("Starts :", hits)

print("Overlapping 'AA' in 'AAAA':",
      locate_all("AAAA", "AA", ignore_case=False))


OUTPUT
Text : The Python laboratory teaches PYTHON strings.
Needle : python
Found : True
Count : 2
Starts : [4, 30]
Overlapping 'AA' in 'AAAA': [0, 1, 2]

-------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------

AIM   TO PERFORM THREE OPERATION ON LISTS ADDITION ,INSERTION AND SLICING

# Program

internals = [18, 16, 19, 15]
external = [62, 54, 70, 48]

totals = []
for i in range(len(internals)):
    totals.append(internals[i] + external[i])

print("Paper totals (internal + external):", totals)
print("Concatenated lists :", internals + external)

avg = sum(totals) / len(totals)

totals.insert(0, round(avg, 1))

print("After inserting class average:", totals)
print("Only the four paper totals:", totals[1:])

totals[1:3] = [80, 80]

print("After slice assignment:", totals)
print("Every other value:", totals[::2])


OUTPUT

Paper totals (internal + external): [80, 70, 89, 63]
Concatenated lists : [18, 16, 19, 15, 62, 54, 70, 48]
After inserting class average: [75.5, 80, 70, 89, 63]
Only the four paper totals: [80, 70, 89, 63]
After slice assignment: [75.5, 80, 80, 89, 63]
Every other value: [75.5, 80, 63]

------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------
AIM TO TAKE ANY LIST AND APPLY FIVE BUILT_IN FUNCTIONS TO IT
# Program

def list_dashboard(values, label="data"):
    if not values:
        print(label, ": Empty - nothing to summarise")
        return

    print("\n" + "=" * 40)
    print("Dashboard for :", label)
    print("Values :", values)
    print("Count (len) :", len(values))
    print("Lowest (min) :", min(values))
    print("Highest (max) :", max(values))
    print("Total (sum) :", sum(values))
    print("Ordered :", sorted(values))
    print("Mean :", round(sum(values) / len(values), 2))


list_dashboard([85, 90, 76, 92, 88], "Unit II internal marks")
list_dashboard([12.5, 8.0, 11.0, 9.5], "Lab hours this week")
list_dashboard([], "Forgotten batch")


OUTPUT
========================================
Dashboard for : Unit II internal marks
Values : [85, 90, 76, 92, 88]
Count (len) : 5
Lowest (min) : 76
Highest (max) : 92
Total (sum) : 431
Ordered : [76, 85, 88, 90, 92]
Mean : 86.2

========================================
Dashboard for : Lab hours this week
Values : [12.5, 8.0, 11.0, 9.5]
Count (len) : 4
Lowest (min) : 8.0
Highest (max) : 12.5
Total (sum) : 41.0
Ordered : [8.0, 9.5, 11.0, 12.5]
Mean : 10.25

Forgotten batch : Empty - nothing to summarise
------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------
