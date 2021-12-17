from dataclasses import dataclass
from re import match

from util import sign


@dataclass
class Rectangle:
    x1: int
    x2: int
    y1: int
    y2: int


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Velocity:
    x: int
    y: int


@dataclass
class Projectile:
    position: Position
    velocity: Velocity


def target_rectangle_from_string(s) -> Rectangle:
    x1, x2, y1, y2 = map(
        int,
        match(
            r"^target area: x=([-+]?\d+)\.\.([-+]?\d+), y=([-+]?\d+)\.\.([-+]?\d+)$", s
        ).groups(),
    )
    return Rectangle(x1, x2, y1, y2)


def simulate_physics(projectile):
    return Projectile(
        Position(
            projectile.position.x + projectile.velocity.x,
            projectile.position.y + projectile.velocity.y,
        ),
        Velocity(
            projectile.velocity.x - sign(projectile.velocity.x)
            if projectile.velocity.x
            else 0,
            projectile.velocity.y - 1,
        ),
    )


def is_colliding(position: Position, hitbox: Rectangle) -> bool:
    return (
        position.x >= hitbox.x1
        and position.x <= hitbox.x2
        and position.y >= hitbox.y1
        and position.y <= hitbox.y2
    )


def shot_has_missed(projectile: Projectile, target: Rectangle):
    return projectile.position.x > target.x2 or projectile.position.y < target.y1


def simulate(projectile: Projectile, target: Rectangle):
    while not shot_has_missed(projectile, target):
        if is_colliding(projectile.position, target):
            return 1
        projectile = simulate_physics(projectile)
    return 0


rect = target_rectangle_from_string(input())

# part 1
y_distance = abs(rect.y1)
print((y_distance - 1) * (y_distance) // 2)

# part 2
print(
    sum(
        simulate(Projectile(Position(0, 0), Velocity(vx0, vy0)), rect)
        for vx0 in range(1, rect.x2+1)
        for vy0 in range(-abs(rect.y1), abs(rect.y1))
    )
)
