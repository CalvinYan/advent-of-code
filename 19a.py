import numpy as np

ore_cost = []

clay_cost = []

obsidian_cost = []

geode_cost = []

counter = 0
with open('19.txt', 'r') as file:
    for line in file.readlines():
        line = line[:-1]
        tokens = line.split()

        ore_cost.append([int(tokens[6]), 0, 0, 0])
        clay_cost.append([int(tokens[12]), 0, 0, 0])
        obsidian_cost.append([int(tokens[18]), int(tokens[21]), 0, 0])
        geode_cost.append([int(tokens[27]), 0, int(tokens[30]), 0])

# print(ore_cost, clay_cost, obsidian_cost, geode_cost)

# robots input: [# ore bots, # clay bots, # obsidian bots, # geode_bots]
# resources input: [# ore, # clay, # obsidian, # geode]
def score(minute, robots, resources, blueprint):
    global counter
    # print("COUNTER:", counter)
    # counter += 1
    print("MINUTE:", minute, "ROBOTS:", robots, "RESOURCES", resources, "BLUEPRINT", blueprint)
    if any([r < 0 for r in resources]):
        return 0

    if minute == 24:
        return resources[-1]

    # for type, qty in enumerate(robots):
        # resources[type] += qty

    ans = 0

    for type, cost in enumerate(blueprint):
        if all(r >= c for r, c in zip(resources, cost)):

            new_resources = [r - c + q  for r, c, q in zip(resources, cost, robots)]

            new_robots = [r for r in robots]
            new_robots[type] += 1
        # print("NEW:", new_resources, resources, cost)
            ans = max(ans, score(minute + 1, new_robots, new_resources, blueprint))

    # If we do nothing
    new_resources = [r + q  for r, q in zip(resources, robots)]
    ans = max(ans, score(minute + 1, robots, new_resources, blueprint))


    return ans


ans = 0
for i, _ in enumerate(ore_cost):
    blueprint = [ore_cost[i], clay_cost[i], obsidian_cost[i], geode_cost[i]]

    ans += score(1, [1, 0, 0, 0], [0, 0, 0, 0], blueprint)

print(ans)