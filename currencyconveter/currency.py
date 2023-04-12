
dollars = float(input("Enter the amount in US dollars: "))


exchange_rate = 111.00  # 1 US dollar = 111.00 Kenyan shillings
shillings = dollars * exchange_rate


print(f"${dollars:.2f} is KES{shillings:.2f}")
