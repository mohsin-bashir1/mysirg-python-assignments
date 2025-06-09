#Write a python script to calculate simple interest.

print("Enter principal, rate of interest, time interval: ")

pa, roi, ti = int(input()), float(input()), int(input())

si = pa * roi * ti / 100

print(f"The simple interest with principal amount {pa}, roi {roi}% and time interval {ti} years is {si:.2f}")