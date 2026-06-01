def making_sandwich(*ingredients):
    print('Making sandwich with:')
    for ingredient in ingredients:
        print(f'\t{ingredient.title()}')

making_sandwich('cheese')
making_sandwich('eggs', 'ham', 'cheese')
making_sandwich('cheese', 'ham')
