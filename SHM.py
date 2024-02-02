# Simple Harmonic Motion Simulation
import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 400
FPS = 60

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Harmonic Motion Simulation")

# Clock to control the frame rate
clock = pygame.time.Clock()

def draw_spring(start_pos, end_pos, num_coils, coil_radius, coil_spacing):
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    angle = math.atan2(dy, dx)
    length = math.hypot(dx, dy)

    for i in range(num_coils):
        theta = i * coil_spacing / length
        x = start_pos[0] + (length / num_coils) * i * math.cos(angle)
        y = start_pos[1] + (length / num_coils) * i * math.sin(angle)
        pygame.draw.circle(screen, BLUE, (int(x), int(y)), coil_radius)

def harmonic_motion(amplitude, frequency):
    time = 0

    spring_start = (WIDTH // 4, HEIGHT // 2)
    spring_end = (WIDTH * 3 // 4, HEIGHT // 2)
    num_coils = 20
    coil_radius = 5
    coil_spacing = 2 * math.pi  # Adjust for the number of coils

    # Time step
    dt = 1 / FPS

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update time
        time += dt

        # Calculate position based on simple harmonic motion
        x = WIDTH // 2 + amplitude * math.sin(2 * math.pi * frequency * time)

       
        screen.fill(WHITE)
        draw_spring(spring_start, (x, HEIGHT // 2), num_coils, coil_radius, coil_spacing)

        pygame.draw.circle(screen, BLUE, (int(x), HEIGHT // 2), 20)

        font = pygame.font.Font(None, 36)
        text_amplitude = font.render(f'Amplitude: {amplitude}', True, BLUE)
        text_frequency = font.render(f'Frequency: {frequency}', True, BLUE)
        screen.blit(text_amplitude, (10, HEIGHT - 60))
        screen.blit(text_frequency, (10, HEIGHT - 30))

        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

amplitude = 200
frequency = 2
harmonic_motion(amplitude, frequency)

# Wait for a key press before closing the window
pygame.event.clear()
pygame.event.wait()

pygame.quit()
sys.exit()

