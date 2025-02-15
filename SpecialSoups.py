def min_moves(test_cases):
    results = []
    for case in test_cases:
        N, flavors = case
        moves = 0
        prev_ingredients = set()
        for flavor in flavors:
            if flavor == 't':
                ingredients = {'tomato'}
            elif flavor == 'o':
                ingredients = {'onion'}
            elif flavor == 'b':
                ingredients = {'bell_pepper'}
            elif flavor == 'y':
                ingredients = {'onion', 'bell_pepper'}
            elif flavor == 'p':
                ingredients = {'tomato', 'onion'}
            elif flavor == 'c':
                ingredients = {'bell_pepper', 'tomato'}
            elif flavor == 's':
                ingredients = {'tomato', 'onion', 'bell_pepper'}
            
            new_ingredients = ingredients - prev_ingredients
            if new_ingredients:
                moves += len(new_ingredients)
            prev_ingredients = ingredients
        results.append(moves)
    return results

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    flavors = input().split()
    test_cases.append((N, flavors))

results = min_moves(test_cases)

for res in results:
    print(res)