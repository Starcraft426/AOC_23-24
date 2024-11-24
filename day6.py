input = """Time: 41667266
Distance: 244104712281040""".split("\n")

times = input[0].split(": ")[-1].split(" ")
times = [int(time) for time in times if time != ""]

distances = input[1].split(": ")[-1].split(" ")
distances = [int(dist) for dist in distances if dist != ""]

record_broken = 0
timebreak = 0
for i, time in enumerate(times):
    timebreak = 0
    for j in range(time):
        distance = j*(time-j)
        if distance > distances[i]:
            timebreak += 1
    if record_broken ==0:
        record_broken = timebreak
    else:
        record_broken *= timebreak
print(record_broken)