def main():
    number_of_ways = 0
    total = 0

    for a in range(1, -1, -1):  # 200p
        for b in range(2, -1, -1):  # 100p
            for c in range(4, -1, -1):  # 50p
                for d in range(10, -1, -1):  # 20p
                    for e in range(20, -1, -1):  # 10p
                        for f in range(40, -1, -1):  # 5p
                            for g in range(100, -1, -1):  # 2p
                                for h in range(200, -1, -1):  # 1p
                                    if a*200 + b*100 + c*50 + d*20 + e*10 + f*5 + g*2 + h == 200:
                                        number_of_ways += 1
    return number_of_ways


print(main())
