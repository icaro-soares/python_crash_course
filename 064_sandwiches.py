finished = False
sandwich_orders = ['american', 'double', 'tuna', 'vegan']
finished_orders = []
while not finished:
    if sandwich_orders:
        finished_orders.append(sandwich_orders.pop())
    else:
        finished = True
print('\n--- Your orders ---')
for order in finished_orders:
    print(f'Your {order} sandwich is finished.')
