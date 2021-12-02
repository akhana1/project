from flask import Flask
import random
application = Flask(__name__)

@application.route("/")
def main():
    numberToGuess = random.randint(1, 100)
    # tester - print(numberToGuess)
    picked = int
    floor = 1
    ceiling = 100
    possibilities = [*range(floor, ceiling + 1)]
    correct = False

    while not correct:
        print("Enter a number between ", floor, " and ", ceiling)
        picked = int(input("Choice: "))

        if picked not in possibilities:
            print("Invalid")

        elif picked > numberToGuess:
            print("Your number is higher than the target")
            ceiling = picked
            for i in possibilities:
                if i < ceiling:
                    possibilities = [*range(floor, ceiling + 1)]
                    possibilities.append(i)


        elif picked < numberToGuess:
            print("Your number is lower than the target")
            floor = picked
            for i in possibilities:
                if i > floor:
                    possibilities = [*range(floor + 1, ceiling)]
                    possibilities.append(i)
            floor += 1

        else:
            print("Correct!")
            correct = True




if __name__ == "__main__":
    application.run()
