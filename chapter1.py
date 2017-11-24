# 1.9 Chapter 1 Exercises

# Exercise 1

# It is a good idea to read this book in front of
# a computer so you can try out the
# examples as you go.

# Whenever you are experimenting with a new
# feature, you should try to make mistakes. For
# example, in the “Hello, world!” program, what
# happens if you leave out one of the quotation
# marks? What if you leave out both? What if you
# spell print wrong?

# This kind of experiment helps you remember what
# you read; it also helps when you are
# programming, because you get to know what the
# error messages mean. It is better to make
# mistakes now and on purpose than later and
# accidentally.

# 1.1 In a print statement, what happens if you
# leave out one of the parentheses, or both?

# print("Hello, World!"
# SyntaxError: unexpected EOF while parsing

# 1.2 If you are trying to print a string, what
# happens if you leave out one of the quotation
# marks, or both?

# print("Hello, World!)
# SyntaxError: EOL while scanning string literal

# 1.3 You can use a minus sign to make a negative
# number like -2. What happens if you put a
# plus sign before a number? What about 2++2?

# x = -2
# print(x)
# -2

# y = +2
# print(y)
# 2

# z = ++2
# print(z)
# 2

# 1.4 In math notation, leading zeros are ok, as
# in 02. What happens if you try this in Python?

# a = 02
# print(a)
# SyntaxError: invalid token

# 1.5 What happens if you have two values with no
# operator between them?

# print(3 7)
# SyntaxError: invalid syntax

# Exercise 2

# Start the Python interpreter and use it as a
# calculator.

# 2.1 How many seconds are there in 42 minutes 42
# seconds?

time_seconds = (42 * 60) + 42
print(time_seconds)
# 2562

# 2.2 How many miles are there in 10 kilometers?
# Hint: there are 1.61 kilometers in a mile.

mile_to_kilometer = float(1.0 / 1.61)
race_distance_miles = 10 * mile_to_kilometer
print(race_distance_miles)
# 6.211180124223602

# 2.3 If you run a 10 kilometer race in 42
# minutes 42 seconds, what is your average pace
# (time per mile in minutes and seconds)? What
# is your average speed in miles per hour?

time_minutes = (time_seconds / 60)
average_pace_miles = (time_minutes / race_distance_miles)
miles_per_hr = (60 / (average_pace_miles))

print(average_pace_miles)
print(miles_per_hr)
