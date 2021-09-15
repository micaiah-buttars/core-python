ratings = {}

def parser():
    with open('scores.txt') as scores:
        for line in scores:
            restaurant = line.rstrip().split(':')
            ratings[f"{restaurant[0]}"] = f"{restaurant[1]}"
    
    for item in sorted(ratings.items()):
        print(f"{item[0]} is rated at {item[1]}.")

    scores.close()


def new_restaurant():
    name = input("What is this new restaurant's name?\n")
    score = int(input("What is this new restaurant's rating?\n"))

    ratings[f"{name}"] = f"{score}"

    parser()

parser()
new_restaurant()