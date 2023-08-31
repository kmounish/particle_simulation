class Particle:
    def __init__(self, x, y, size, id):
        self.id = id
        self.velocity = 0
        self.gravity = 9.8
        self.x = x
        self.y = y
        self.size = size

    def get_pos(self):
        return (self.x, self.y)

    def update_pos(self, *args):
        # TODO:Should make it more dynamic, window size
        if len(args) == 0:
            if self.y > 720:
                self.y = 720
            elif self.y == 720:
                self.y = 720
            else:
                self.y = self.y + self.velocity
        else:
            self.y = args[0][1]-args[1]
            if len(args) == 3:
                if args[2] == "left":
                    self.x = args[0][0]-args[1]
                if args[2] == "right":
                    self.x = args[0][0]+args[1]
            self.update_velocity()

    def update_velocity(self, *args):
        if len(args) == 0:
            self.velocity = 0
        else:
            self.velocity = (self.gravity*args[0])*.01 + self.velocity

    def get_speed(self):
        return self.velocity
