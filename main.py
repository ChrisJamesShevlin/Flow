import py5

NUM_PARTICLES = 500
NOISE_SCALE = 0.003
MAX_SPEED = 2.5

particles = []

class Particle:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = py5.random(py5.width)
        self.y = py5.random(py5.height)
        self.prev_x = self.x
        self.prev_y = self.y
        self.lifetime = int(py5.random(80, 220))
        self.age = 0
        self.speed = py5.random(0.8, MAX_SPEED)

    def update(self):
        self.prev_x = self.x
        self.prev_y = self.y

        angle = py5.noise(self.x * NOISE_SCALE, self.y * NOISE_SCALE) * py5.TWO_PI * 2
        self.x += py5.cos(angle) * self.speed
        self.y += py5.sin(angle) * self.speed
        self.age += 1

        if (self.age >= self.lifetime or
                self.x < 0 or self.x > py5.width or
                self.y < 0 or self.y > py5.height):
            self.reset()

    def draw(self):
        t = self.age / self.lifetime
        alpha = py5.map(py5.sin(t * py5.PI), 0, 1, 0, 210)
        weight = py5.map(py5.sin(t * py5.PI), 0, 1, 0.3, 2.0)

        py5.stroke(255, alpha)
        py5.stroke_weight(weight)
        py5.line(self.prev_x, self.prev_y, self.x, self.y)


def setup():
    py5.size(1920, 1080)
    py5.background(0)
    for _ in range(NUM_PARTICLES):
        p = Particle()
        p.age = int(py5.random(p.lifetime))
        particles.append(p)


def draw():
    py5.no_stroke()
    py5.fill(0, 8)
    py5.rect(0, 0, py5.width, py5.height)

    for p in particles:
        p.draw()
        p.update()


def key_pressed():
    if py5.key == 's':
        py5.save_frame("screenshot-####.png")


py5.run_sketch()
