---
layout: default
title: "Lesson 2"
---

# Lesson 2

- [Lesson files](#lesson-files)
- [Worksheet](#worksheet)
    - [Investigate](#investigate)
    - [Modify](#modify)
    - [Make](#make)
- [Homework](#homework)
    - [Requirements](#requirements)
    - [Options](#options)

## Lesson files

### [models.py](models.py)
```python
{% include_relative models.py %}
```

### [main.py](main.py)
```python
{% include_relative main.py %}
```

## Worksheet

### Investigate
Answer these questions by examining the code.

1. What does `from models import Ball` do in `main.py`?
1. Why does `main.py` create a list of balls instead of storing them in separate variables?
1. What do the two `for` loops do in `main.py`?
1. What does `p_color=(255, 0, 0), p_vx=0, p_vy=0` mean in the constructor signature in `models.py`?
1. Why does the `Ball` object need all of the parameters as attributes? 
1. Why are the `_draw` and `_move` methods private?
1. Why does `update` call both `move` and `draw`?
1. Why does the `_draw` method need `screen` as a parameter?

### Modify
Make changes to explore how the code works.

1. Implement the constructor using the information below:
    | Visibility | Name   | Type | Description |
    |-----------|--------|------|-------------|
    | private   | `x`    | int  | Horizontal position of the ball’s centre |
    | private   | `y`    | int  | Vertical position of the ball’s centre |
    | private   | `vx`   | int  | Horizontal velocity (change in x each frame) |
    | private   | `vy`   | int  | Vertical velocity (change in y each frame) |
    | private   | `radius` | int | Size of the ball |
1. Implement the `_draw` method
1. Implement the `_move` method
    - At this stage, **do not** implement bouncing


### Make
1. Use the information below to implement the missing `get` methods (`get_coords`, `_get_left`, `_get_right`, `_get_top`, `_get_bottom`).

    The `_get_<direction>` methods should return the position of the ball's edge in that direction (hint: how can you use the ball's radius to work this out?).

| Visibility | Method Signature | Returns | Description |
|-----------|------------------|---------|-------------|
| public    | `get_coords()` | tuple[int, int] | Returns `(x, y)`, the ball’s current position |
| private   | `_get_left()`   | int | Returns the x-coordinate of the left edge (`x - radius`) |
| private   | `_get_right()`  | int | Returns the x-coordinate of the right edge (`x + radius`) |
| private   | `_get_top()`    | int | Returns the y-coordinate of the top edge (`y - radius`) |
| private   | `_get_bottom()` | int | Returns the y-coordinate of the bottom edge (`y + radius`) |
| private   | `_draw(screen)` | None | Draws the ball on the given `screen` |
| private   | `_move(x_bounds, y_bounds)` | None | Updates the ball’s position (later: add bouncing) |
| public    | `update(screen, x_bounds, y_bounds)` | None | Calls `_move` then `_draw` each frame |


2. Once all the getters work, update `move` so the ball cannot leave the window.
    - When the ball reaches and edge, it should bounce by reversing the appropriate velocity.

You will need to update the `update` method:
```python
def update(self, screen, x_bounds, y_bounds):
    """
    Move and draw the ball.

    Parameters:
        screen: a pygame screen
        x_bounds: a tuple containing the lower and upper x bounds, e.g. (0, WIDTH)
        y_bounds: a tuple containing the lower and upper y bounds, e.g. (0, HEIGHT)
    """
    self._move(x_bounds, y_bounds)
    self._draw(screen)
```

#### Extension tasks
Complete these tasks in any order.

##### Colour changing
1. Implement a `_change_color(new_color)` method to change the ball's colour
1. Modify `_move` so the ball changes colour each time it bounces.

##### Inside-bounds?
Implement `inside_bounds`:
- Returns True if every part of the ball is within given bounds
- Returns False otherwise

##### Randomised bounce velocities
Change `_move` so that, when the ball bounces, the velocity is slightly randomised.
Make sure the ball cannot become frozen!

##### Decaying velocity
Create a `DecayingBall` class that inherits from `Ball`.
- Add a new attribute, `decay_factor` (e.g., 0.9)
- Override `_move` so that velocity is scaled after each bounce