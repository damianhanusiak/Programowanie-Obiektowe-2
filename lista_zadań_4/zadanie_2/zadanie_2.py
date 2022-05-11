import time
import random


class Ball:
    def __init__(self, number, weighed_down):
        self.number = number
        self.weighed_down = weighed_down

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return str(self.number)


class LotteryMachine:
    def __init__(self):
        self.list_of_balls = []
        self.weighed_down_balls = []
        for i in range(6):
            self.weighed_down_balls.extend(
                random.sample([i for i in range(49)], 6))
        for i in range(49):
            b = Ball(i+1, i in self.weighed_down_balls)
            self.list_of_balls.append(b)

    def start(self, drawtime):
        for i in range(0, drawtime * 1000, 10):
            self._randomizer()

    def stop(self):
        return self.list_of_balls[:6]

    def _randomizer(self):
        x = random.randint(0, 48)
        y = random.randint(0, 48)
        self.list_of_balls[x], self.list_of_balls[y] = self.list_of_balls[y], self.list_of_balls[x]
        for i in range(1, 49):
            if self.list_of_balls[i].weighed_down:
                self.list_of_balls[i], self.list_of_balls[i -
                                                          1] = self.list_of_balls[i-1], self.list_of_balls[i]
        time.sleep(0.01)


l = LotteryMachine()
print([b for b in l.list_of_balls if b.weighed_down])
l.start(5)
print(l.stop)
