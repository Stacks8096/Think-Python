# 2.10 Exercises

# Exercise 2.1.
# Repeating my advice from the
# previous chapter, whenever you learn a new
# feature, you should try it out in interactive
# mode and make errors on purpose to see what
# goes wrong.

# We’ve seen that n = 42 is legal.
# What about 42 = n?

# 42 = n
# print(n)
# SyntaxError: can't assign to literal

# How about x = y = 1?

# x = y = 1
# print(x, y)
# 1 1

# In some languages every statement ends with
# semi-colon, ;. What happens if you put a
# semi-colon at the end of a Python statement?

# x = y = 1;
# print(x, y)
# 1 1
# Linter Error E703 statement ends with a
# semicolon

# What if you put a period at the end of a
# statement?

# x = y = 1.
# print(x, y)
# 1.0 1.0
# x, y become floats

# In math notation you can multiply x and y like
# this: xy. What happens if you try that in
# Python?

# x = y = 7
# print(xy)
# NameError: name 'xy' is not defined

# x = y = 7
# print(x * y)
# 49

# Exercise 2.2. Practice using the Python
# interpreter as a calculator:

# The volume of a sphere with radius r is
# 4 / 3 * pi * r**3
# What is the volume of a sphere with radius 5?

# pi = 3.14
# r = 5
# volume_sphere = 4/3*pi*r**3
# print(volume_sphere)

# 2. Suppose the cover price of a book is $24.95,
# but bookstores get a 40% discount. Shipping
# costs $3 for the first copy and 75 cents for
# each additional copy.

# What is the total wholesale cost for
# 60 copies?

# number_of_books = 60
# book_cover_price = 24.95
# bookstore_price = book_cover_price*(1-0.40)
# shipping_cost = 3+(0.75*(number_of_books-1))
# total_wholesale_cost =
# (bookstore_price*number_of_books) +
# shipping_cost

# print(total_wholesale_cost)
# 945.4499999999999

# 3. If I leave my house at 6:52 am and run 1
# mile at an easy pace (8:15 per mile), then 3
# miles at
# tempo (7:12 per mile) and 1 mile at easy pace
# again, what time do I get home for breakfast?

start_hr = 6
start_min = 52
hr_secs = 3600
start_secs = ((6 * 3600) + (52 * 60))
easy_pace = (60 * 8) + 15
tempo_pace = (60 * 7) + 12
run_time = (easy_pace * 2) + (tempo_pace * 3)
run_mins = run_time / 60
fin_hr = float((start_secs + run_time) / hr_secs)
fin_hr_int = int(fin_hr)
fin_min = ((fin_hr - fin_hr_int) * 60)

print(start_secs)
print(run_time)
print(run_mins)
print(fin_hr)
print(fin_hr_int)
print('Start Time : %d:%d' % (start_hr, start_min))
print('Run Time : %d' % (run_mins) + ' minutes')
print('Current Time : %d:%d' % (fin_hr_int, fin_min))
