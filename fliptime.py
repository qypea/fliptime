#!/usr/bin/env python3

"""What times on a digital clock can be flipped over the colon and still be valid?"""

def generate_minutes():
    for minute in range(0, 60):
        yield str(minute).zfill(2)

def generate_12h():
    """Generate all of the 12h times."""
    for hour in range(1, 13):
        for minute in generate_minutes():
            yield f"{hour}:{minute}"

VALID_12H = frozenset(generate_12h())

def generate_24h():
    """Generate all of the 24h times."""
    for hour in range(0, 24):
        hour = str(hour).zfill(2)
        for minute in generate_minutes():
            yield f"{hour}:{minute}"

VALID_24H = frozenset(generate_24h())

FLIPPED = {
    "0": "0",
    "1": "1",
    "2": "5",
    "5": "2",
    "8": "8",
}

def flip_24h(original):
    """Flips a 24h time over the colon or returns none if impossible."""
    assert original[2] == ':'
    assert len(original) == 5
    return FLIPPED.get(original[4], 'X') + \
           FLIPPED.get(original[3], 'X') + \
           ':' + \
           FLIPPED.get(original[1], 'X') + \
           FLIPPED.get(original[0], 'X')

count = 0
for original in generate_24h():
    flipped = flip_24h(original)
    if flipped in VALID_24H:
        print(original, flipped)
        count += 1
print(count, "flippable values in 24h time")


def flip_12h(original):
    """Flips a 12h time at the middle or returns none if impossible."""
    if len(original) == 5:
        # Two-digit hour case is the same as 24h time
        return flip_24h(original)

    assert original[1] == ':'
    assert len(original) == 4
    # 0:23->3:20
    return FLIPPED.get(original[3], 'X') + \
           ':' + \
           FLIPPED.get(original[2], 'X') + \
           FLIPPED.get(original[0], 'X')

count = 0
for original in generate_12h():
    flipped = flip_12h(original)
    if flipped in VALID_12H:
        print(original, flipped)
        count += 1
print(count, "flippable values in 12h time")


