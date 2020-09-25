available = set(["1","2","3"])
visited = set([])

while available != visited:
    remaining = available.difference(visited)
    remaininglist = (list(remaining))
    remainingStr = [aisle for aisle in remaininglist]
    choice = input(f"Which aisle do you want to visit, {remainingStr}: ")
    if choice == "1":
        print("You are visiting aisle 1!")
        visited.add("1")
    elif choice == "2":
        print("You are visiting aisle 2!")
        visited.add("2")
    elif choice == "3":
        print("You are visiting aisle 3!")
        visited.add("3")

print("You've visited all the aisles! yay!")