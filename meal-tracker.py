amounts = {
    'oatmeal': [3, 'cups'],
    'peanut butter': [6, 'tbsp'],
    'protein powder': [2.5, 'servings'],
    'banana': [1, 'serving'],
    'blueberries': [0.5, 'cups'],
    'nuts': [0.5, 'cups'],
    'cottage cheese': [0.75, 'cups'],
    'yogurt': [1, 'cups']
}

def print_remaining_amounts():
    print 'Amounts Left:'
    for (k, v) in amounts.items():
        if v[0] > 0:
            print '%r: %r %s' % (k, v[0], v[1]) # v[0] = the amount, v[1] = the measurement

def add_meal():
    print_remaining_amounts()
    for (k, v) in amounts.items():
        if v[0] > 0:
            v[0] -= input('Enter the amount of %s (in %s): ' % (k, v[1]))

def check_for_completion():
    for (k, v) in amounts.items():
        # print '%r, %r' % (k, v)
        if v[0] <= 0:
            pass
        else:
            return False
    return True

while True:
    add_meal()
    if check_for_completion():
        print "You're done!"
        break
