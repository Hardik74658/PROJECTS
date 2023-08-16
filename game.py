import random
import requests_cache

print(requests_cache.ALL_METHODS)
choice = 1
Final_Score = 0
Matches = 0
while (1):
    print("\n1---Play\n2---Exit\n\n")
    choice = int(input("Enter Your Choice : "))
    if choice == 2:
        break
    Matches += 1
    flag = 0
    value = random.choice(range(1, 11))
    # print(value)
    while (1):
        guess = int(input("Enter Your Guess(1-10) : "))
        if (guess == value):
            print("Congratulations!! You Won The Game")
            flag += 1
            temp_score = 10-flag
            Final_Score = Final_Score + temp_score
            print(f"\n\nScore : {temp_score}")
            break

        elif (guess > value):
            flag += 1
            print("Less")

        else:
            flag += 1
            print("Greater")
print("---------------------------------------------------FINAL SCORES----------------------------------------------------------------")
print(f"\nTotal Matches : {Matches}")
print(f"Total Score     : {Final_Score}")
