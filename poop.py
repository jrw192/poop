from random import randint

# print(" ~*~")
# print("       /)")
# print("  ~*~ (__)")
# print("    (__/__)  ~*~")
# print("  (_/______)")

print("running poop...")

print(randint(0,2))
# levels of poop
levels = randint(1,20)
# tip starting position, where max width of base of poop is levels*4
tip_start = randint(levels, (levels*3))

#list of thiccobjects: [beginning, slope_placement, end, fly_index]
thiccness = []

### ------------ MAKE THE POOP STRUCTURE ------------
for x in range(0, levels):
    curr_level = []
    # I don't want there to be a lot of 0 indents, so randint range of 5 and then adjust based on probabilities. 
    # This (below) gives 2/5 chance for 1 and 2, 1/5 chance for 0

    #fly_index is between 2 and 

    beginning = tip_start - randint(1,5)%3
    end = tip_start + 1 + randint(1,5)%3
    fly_index = False
    slope_placement = False

    # we don't want a slope put on a level that's too small or it'll look weird.
    if end - beginning - 1 > 5:
        slope_placment = randint(beginning + 2, end - 2)

    if randint(1, 5)%5 == 0:
        fly_index = randint(0, end + 5)
        #ensure that fly_index doesn't land between beginning or end
        while fly_index in range(beginning - 4, end + 2):
            fly_index = randint(0, end + 5)

### ------------ PRINT THE POOP STRUCTURE ------------
