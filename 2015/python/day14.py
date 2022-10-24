import re


# Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.

def parse_line(line: str):
    p = re.compile('(\d+)')
    result = re.findall(p, line)
    if len(result) != 3:
        return 0, 0, 0
    return int(result[0]), int(result[1]), int(result[2])


class Reindeer:
    def __init__(self, speed, speed_seconds, rest_seconds):
        self.speed = speed
        self.speed_seconds = speed_seconds
        self.rest_seconds = rest_seconds
        self.distance = 0
        self.score = 0

    def run(self, seconds):
        run_seconds = 0
        distance = 0
        while run_seconds <= seconds:
            distance += self.speed * self.speed_seconds
            run_seconds += self.speed_seconds
            run_seconds += self.rest_seconds
        return distance

    def run_next(self, total_seconds):
        state = total_seconds % (self.speed_seconds + self.rest_seconds)
        if state < self.speed_seconds:
            self.distance += self.speed
        return self.distance

    def add_score(self):
        self.score += 1

    def get_score(self):
        return self.score


def create_reindeers(results):
    reindeers = []
    for result in results:
        reindeers.append(Reindeer(result[0], result[1], result[2]))
    return reindeers


def test():
    reindeers = create_reindeers([[14, 10, 127], [16, 11, 162]])
    print(reindeers[0].run(1000))
    print(reindeers[1].run(1000))


def test2():
    reindeers = create_reindeers([[14, 10, 127], [16, 11, 162]])
    reindeer_distances = {}

    for i in range(0, 1000):
        reindeer_distances = {}
        for idx in range(len(reindeers)):
            distance = reindeers[idx].run_next(i)
            reindeer_distances[idx] = distance

        max_distance = 0
        for k, v in reindeer_distances.items():
            if max_distance < v:
                max_distance = v

        for k, v in reindeer_distances.items():
            if v == max_distance:
                reindeers[k].add_score()

    for reindeer in reindeers:
        print(reindeer.get_score())


def part1():
    with open('inputs/input14') as file:
        results = [parse_line(line.strip()) for line in file.readlines() if
                   line.strip()]
        reindeers = create_reindeers(results)
        max_distance = 0
        for reindeer in reindeers:
            distance = reindeer.run(2503)
            if max_distance < distance:
                max_distance = distance
        print(max_distance)


def part2():
    with open('inputs/input14') as file:
        results = [parse_line(line.strip()) for line in file.readlines() if
                   line.strip()]
        reindeers = create_reindeers(results)
        reindeer_distances = {}

        for i in range(0, 2503):
            reindeer_distances = {}
            for idx in range(len(reindeers)):
                distance = reindeers[idx].run_next(i)
                reindeer_distances[idx] = distance

            max_distance = 0
            for k, v in reindeer_distances.items():
                if max_distance < v:
                    max_distance = v

            for k, v in reindeer_distances.items():
                if v == max_distance:
                    reindeers[k].add_score()

        max_score = 0
        for reindeer in reindeers:
            score = reindeer.get_score()
            if max_score < score:
                max_score = score
        print(max_score)


# part1()
# test2()
part2()