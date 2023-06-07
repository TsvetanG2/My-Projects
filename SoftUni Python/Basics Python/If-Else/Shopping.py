budget = float(input())
sum_videocard = int(input())
sum_processor = int(input())
sum_ram_memory = int(input())


videocard_cost = sum_videocard * 250

ram_memory_cost = videocard_cost * 0.10
ram_price = ram_memory_cost * sum_ram_memory

processor_cost = videocard_cost * 0.35
processor_price = processor_cost * sum_processor

total_sum = videocard_cost + processor_price + ram_price

if sum_videocard > sum_processor:
    total_sum = total_sum - (total_sum * 0.15)


if total_sum <= budget:
    diff = abs(budget - total_sum)
    print(f'You have {diff:.2f} leva left!')
else:
    diff = abs(total_sum - budget)
    print(f'Not enough money! You need {diff:.2f} leva more!')


