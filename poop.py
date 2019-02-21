from random import randint

# print(" ~*~")
# print("       /)")
# print("      (__)")
# print("    (__/__)  ~*~")
# print("  (_/______)")

print("running poop...")

print(randint(0,2))
# levels of poop
levels = randint(1,20)
# tip starting position, where max width of base of poop is levels*4
tip_start = randint(levels, (levels*3))

#list of thiccobjects: [width, left_indent, slope_placement_index, right_indent, fly_index]
thiccness = []
curr_thicc = 1

for x in range(0, levels):
    curr_level = []
    # I don't want there to be a lot of 0 indents, so randint range of 5 and then adjust based on probabilities. 
    # This (below) gives 2/5 chance for 1 and 2, 1/5 chance for 0
    left_indent = randint(1,5)%3
    right_indent = randint(1,5)%3

    width = curr_thicc + left_indent + right_indent
    slope_placement_index = 0
    
    # we don't want a slope put on a level that's too small or it'll look weird.
    if width > 5:
        
