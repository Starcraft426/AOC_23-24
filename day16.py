input = open("day16.txt", "r").read().split("\n")
input = [list(line) for line in input]

coords = (0, 0)
direction = (0, 1)  # (y, x)
to_visit = []
visited = []
while True:
    returned = False
    try:
        char = input[coords[0]][coords[1]]
    except IndexError:
        if len(to_visit) == 0:
            break
        returned = True
        coords, direction = to_visit.pop()
    if (abs(coords[0]), abs(coords[1])) != coords:
        if len(to_visit) == 0:
            break
        returned = True
        coords, direction = to_visit.pop()

    if coords not in visited:
        show = True
        match char:
            case "/"|"%":
                input[coords[0]][coords[1]] = "%"
                direction = (-direction[1], -direction[0])
            case "\\"|"@":
                input[coords[0]][coords[1]] = "@"
                direction = (direction[1], direction[0])
            case "-"|"*":
                input[coords[0]][coords[1]] = "*"
                if direction[0] != 0:
                    to_visit.append([coords, (direction[1], direction[0])])
                    direction = (-direction[1], -direction[0])
                visited.append(coords)
            case "|"|"$":
                input[coords[0]][coords[1]] = "$"
                if direction[1] != 0:
                    to_visit.append([coords, (direction[1], direction[0])])
                    direction = (-direction[1], -direction[0])
                visited.append(coords)
            case _:
                show = False
        if show:
            for i in input:
                print("".join(i))
            print()
    else:
        if not returned:
            if len(to_visit) == 0:
                break
            coords, direction = to_visit.pop()
    if input[coords[0]][coords[1]] == ".":
        input[coords[0]][coords[1]] = "#"
    coords = (coords[0] + direction[0], coords[1] + direction[1])

total =0
for i, elem in enumerate(input):
    for j, elem2 in enumerate(elem):
        if elem2 in ["@", "$", "*", "%", "#"]:
            input[i][j] = "#"
            total += 1
        else:
            input[i][j] = "."
for i in input:
    print("".join(i))
print(total)