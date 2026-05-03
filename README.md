<img width="1920" height="1080" alt="screenshot-0221" src="https://github.com/user-attachments/assets/da7b7dc7-2161-47c2-b09c-c36125ce0687" />


---

# 🌊 Generative Study 003 — Flow

This project explores how invisible fields can give rise to visible motion.

At its core, the system steers particles using Perlin noise — a smooth, continuous form of randomness sampled across 2D space:

```python
angle = py5.noise(self.x * NOISE_SCALE, self.y * NOISE_SCALE) * py5.TWO_PI * 2
```

Each frame, 500 particles move through this field, leaving faint trails behind them.

---

## ⚙️ The System

The `draw()` loop runs continuously. Each iteration:

1. Applies a semi-transparent overlay to fade old trails
2. Updates and draws every particle

```python
py5.fill(0, 8)
py5.rect(0, 0, py5.width, py5.height)
```

The background is never fully cleared.

Trails accumulate and slowly dissolve, creating the illusion of flowing smoke or liquid.

---

## 🧠 What the Code Actually Does

The system is built around a `Particle` class. Each particle has:

```python
self.x, self.y        # current position
self.prev_x, self.prev_y  # previous position
self.lifetime         # how long it lives
self.age              # how old it is
self.speed            # how fast it moves
```

Every frame, the particle samples the noise field at its current position to determine which direction to move next.

---

### 1. The Noise Field

The field is sampled using 2D Perlin noise:

```python
angle = py5.noise(self.x * NOISE_SCALE, self.y * NOISE_SCALE) * py5.TWO_PI * 2
```

`NOISE_SCALE` controls how tightly the field curves:

```python
NOISE_SCALE = 0.003
```

A small value produces gentle, sweeping arcs. A larger value would create tighter, more chaotic motion.

---

### 2. Movement

The angle is converted into a velocity vector:

```python
self.x += py5.cos(angle) * self.speed
self.y += py5.sin(angle) * self.speed
```

Each particle follows the local direction of the field, nudged slightly by its individual speed.

---

### 3. Lifecycle

Particles have a limited lifespan:

```python
self.lifetime = int(py5.random(80, 220))
```

When a particle ages out — or drifts off-screen — it resets to a new random position:

```python
if (self.age >= self.lifetime or
        self.x < 0 or self.x > py5.width or
        self.y < 0 or self.y > py5.height):
    self.reset()
```

This keeps the field constantly populated without clearing the accumulated image.

---

### 4. Opacity and Weight as Life Signals

Each particle's visual properties are tied to its age:

```python
t = self.age / self.lifetime
alpha = py5.map(py5.sin(t * py5.PI), 0, 1, 0, 210)
weight = py5.map(py5.sin(t * py5.PI), 0, 1, 0.3, 2.0)
```

Using `sin(t * PI)` creates a smooth bell curve — particles fade in, peak, then fade out over their lifetime. They are never born or die abruptly.

---

### 5. Trail Rendering

Instead of drawing a dot, each particle draws a line from its previous to its current position:

```python
py5.line(self.prev_x, self.prev_y, self.x, self.y)
```

This tiny segment, repeated across 500 particles every frame, builds the flowing texture.

---

## 🌀 From Code to Behaviour

The image that emerges is not drawn — it is traced.

No single particle produces anything visible on its own. The field only becomes apparent through accumulation:

* particles cluster where the field curves inward
* open channels form where the field sweeps outward
* dense regions suggest invisible attractors
* the overall composition shifts slowly as old trails fade

What looks like fluid is actually:

> 500 independent agents, each following a local rule, never aware of the others.

---

## 🎛️ Order vs Noise

The field is deterministic — the same noise seed produces the same angles at the same coordinates every run.

But each particle starts at a random position, moves at a random speed, and lives for a random duration.

This creates a layered balance:

* **structure** from the continuous noise field
* **variation** from randomness in position, speed, and lifetime
* **emergence** from the interaction between the two

---

## 💾 Capturing the Output

The current frame can be saved with a key press:

```python
def key_pressed():
    if py5.key == 's':
        py5.save_frame("screenshot-####.png")
```

The `####` placeholder is automatically replaced with the current frame number, allowing multiple captures without overwriting.

---

## 🧠 Reflection (from a coding perspective)

This project introduced the idea of an **invisible field** driving **visible behaviour**.

The noise function is never drawn.
It has no colour.
No position.
No shape.

It only exists as a lookup table — a direction for every point in space.

Yet it completely determines what the sketch becomes.

This is a shift from:
> drawing things directly

to:
> defining the rules that things follow.

The result demonstrates that:

> an unseen structure can be more powerful than anything explicitly rendered.

---

*Study 003 — motion emerging from a field that cannot be seen.*
