NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

JOHN_PAUL = NAMES[:2] #slices the string after first two
GEORGE_RINGO = NAMES[2:] #keeps first two
REVERSE = NAMES[::-1] # reverses the list
EVERY_OTHER = NAMES[::2] #jumps to every alternate index
#slicing syntax arrname[start:end:step] ex: names[:2], names[::-1]

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
