import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Game constants
GRAVITY = -0.3  # Acceleration due to gravity (m/s^2)
THRUST = 1 # Rocket thrust (m/s^2)
CRASH_SPEED = -3.0  # Maximum speed for safe landing (m/s)
GROUND_HEIGHT = 0.0  # Ground level (m)
ORBIT_HEIGHT = 1000.0  # Orbit altitude (m)
INITIAL_FUEL = 100.0  # Initial fuel level (units)
FUEL_CONSUMPTION_RATE = 1.0  # Fuel consumption rate per thrust (units/s)
rocket_altitude = GROUND_HEIGHT
rocket_speed = 0.0 
rocket_acceleration = 0.0 
fuel = INITIAL_FUEL 
game_over = False

# UI
fuel_gauge_width = 200
fuel_gauge_height = 20
fuel_gauge_x = 10
fuel_gauge_y = 10

# Conversion factors
PIXELS_PER_METER = (SCREEN_HEIGHT - 100) / (ORBIT_HEIGHT - GROUND_HEIGHT)  # Adjust as needed
GROUND_LOCATION = SCREEN_HEIGHT - int(GROUND_HEIGHT * PIXELS_PER_METER)

def reset_game():
    global rocket_altitude, rocket_speed, rocket_acceleration, fuel, game_over
    
    rocket_altitude = GROUND_HEIGHT
    rocket_speed = 0.0
    rocket_acceleration = 0.0
    fuel = INITIAL_FUEL
    game_over = False

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    rocket_acceleration = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
            elif event.key == pygame.K_q:
                running = False

    if not game_over:
        # Thrust control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and fuel > 0:
            rocket_acceleration += THRUST
            fuel -= FUEL_CONSUMPTION_RATE

        # Apply gravity only if the rocket is not on the ground
        if rocket_altitude > GROUND_HEIGHT:
            rocket_acceleration += GRAVITY

        # Update physics
        rocket_speed += rocket_acceleration
        rocket_altitude += rocket_speed

        # Check for win/lose conditions
        if rocket_altitude <= GROUND_HEIGHT:
            if rocket_speed < CRASH_SPEED:
                print(f"Crash! Speed: {rocket_speed:.2f} m/s, Altitude: {rocket_altitude:.2f} m, Fuel: {fuel:.2f}")
                game_over = True
            elif fuel <= 10:
                print("Safe landing!")
                game_over = True

            rocket_altitude = GROUND_HEIGHT  # Reset altitude to ground
            rocket_speed = 0.0  # Reset speed to 0 to stop moving

        if rocket_altitude >= ORBIT_HEIGHT:
            print("Reached orbit!")
            game_over = True

    rocket_y = SCREEN_HEIGHT - int(rocket_altitude * PIXELS_PER_METER)
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 5, rocket_y - 10, 10, 20))

    pygame.draw.rect(screen, WHITE, (fuel_gauge_x, fuel_gauge_y, fuel_gauge_width, fuel_gauge_height), 2)
    pygame.draw.rect(screen, RED, (fuel_gauge_x + 2, fuel_gauge_y + 2, (fuel_gauge_width - 4) * fuel / INITIAL_FUEL, fuel_gauge_height - 4))

    font = pygame.font.Font(None, 36)
    text = font.render(f"Altitude: {rocket_altitude:.2f} m", True, WHITE)
    screen.blit(text, (10, 40))

    speed_text = font.render(f"Speed: {rocket_speed:.2f} m/s", True, WHITE)
    screen.blit(speed_text, (10, 70))

    pygame.draw.rect(screen, GREEN, (0, GROUND_LOCATION, SCREEN_WIDTH, 10))
    orbit_y = SCREEN_HEIGHT - int(ORBIT_HEIGHT * PIXELS_PER_METER)
    color = GREEN if game_over else WHITE
    pygame.draw.circle(screen, color, (SCREEN_WIDTH // 2, orbit_y), 50, 2)

    # Update display
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
