def eat_and_open(counter, dinner_and_gifts):
    """Populate the dinner and gifts lists."""
    if counter == 0:
        dinner_and_gifts[0].append("steak")
        dinner_and_gifts[0].append("twice-baked potato")
        dinner_and_gifts[0].append("chocolate pie")
    elif counter == 1:
        dinner_and_gifts[1].append("racquet")
        dinner_and_gifts[1].append("tennis balls")
        dinner_and_gifts[1].append("sweatband")
    
    return dinner_and_gifts


def main():
    """Main function to create and populate dinner and gifts lists."""
    dinner_and_gifts = [[], []]
    #If you have to for loop in the function, you are only running the program once, so you will only get one of the lists. You have to bring the for loop outside of the function so it would run the function numerous times.
    for counter in range(2):
        dinner_and_gifts = eat_and_open(counter, dinner_and_gifts)
    
    print(dinner_and_gifts)


if __name__ == "__main__":
    main()
