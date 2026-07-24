orders =  ['biryani','pulao','pizza','burger','pizza','pulao','ice-cream','pulao','pulao','biryani','burger','pizza','pulao']

def order_check(food):
    order_frequency = {}

    for dish in food:
        if dish in order_frequency:
            order_frequency[dish] = order_frequency[dish] + 1
        else:
            order_frequency[dish] = 1

    return order_frequency

bleh = order_check(orders)
print(bleh)

