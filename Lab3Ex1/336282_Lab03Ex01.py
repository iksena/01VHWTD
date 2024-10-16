# Author: S336282
# Computer Programming in Python, A.A. 2024/25
# Lab Practice 03, Part 2 Decisions, 03.2.8 Shopping vouchers

def calculateCoupons(amount):
    winText = 'You win a discount coupon of $%.2f. (%d%% of your purchase)'
    if amount > 210:
        return winText % (0.14 * amount, 14)
    if amount > 150:
        return winText % (0.12 * amount, 12)
    if amount > 60:
        return winText % (0.1 * amount, 10)
    if amount >= 10:
        return winText % (0.08 * amount, 8)
    return 'You do not get any coupons'

def couponsExerciseS336282():
    amountSpent = float(input("Please enter the cost of your groceries: "))
    print(calculateCoupons(amountSpent))

couponsExerciseS336282()