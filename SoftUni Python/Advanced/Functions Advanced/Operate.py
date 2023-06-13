from functools import reduce


def operate(operator, *args):
    #def sum_nums():
       # return sum(args)

   # def subtract():
     #   res = 0
     #   for num in args:
      #      res -= num
      #  return res

    #def multiply():
       # res = 1
      #  for num in args:
       #     res *= num
      #  return res

  #  def divide():
      # res = 0
       # for num in args:
       #     res /= num
      #  return res

    if operator == "+":
        return reduce(lambda a, b: a+b, args)
    elif operator == "-":
        return reduce(lambda a, b: a-b, args)
    elif operator == "*":
        return reduce(lambda a, b: a*b, args)
    else:
        return reduce(lambda a, b: a/b, args)
