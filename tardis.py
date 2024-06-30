import pygame

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Time Travel with The Doctor")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define fonts
title_font = pygame.font.Font(None, 36)
message_font = pygame.font.Font(None, 24)

# Define time periods
time_periods = {
    range(0, 1000): "The earliest forms of life on Earth emerge.",
    range(1000, 2000): "The first human civilizations arise.",
    range(2000, 3000): "The Industrial Revolution transforms the world.",
    range(3000, 4000): "Humanity begins exploring the solar system.",
    range(4000, 5000): "Interstellar travel becomes a reality.",
    range(5000, 6000): "Earth's resources are depleted, and colonies are established on other planets.",
    range(6000, 7000): "Advanced technologies reshape human society.",
    range(7000, 8000): "Humanity encounters intelligent alien civilizations.",
    range(8000, 9000): "The Milky Way galaxy is explored and colonized.",
    range(9000, 10000): "The Earth is devoured by the expanding Sun, marking the end of life as we know it."
}

# Game loop
running = True
message = ""
user_input = ""
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not user_input:
                    message = "The Doctor: Enter the time period you wish to travel to (0-9999):"
                else:
                    time_input = int(user_input)
                    user_input = ""
                    for time_range, description in time_periods.items():
                        if time_input in time_range:
                            message = description
                            break
                    else:
                        message = "The Doctor: Invalid time period entered."
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    # Clear the window
    window.fill(BLACK)

    # Render the title
    title_text = title_font.render("Time Travel with The Doctor", True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.midtop = (window_width // 2, 10)
    window.blit(title_text, title_rect)

    # Render the message
    message_text = message_font.render(message, True, WHITE)
    message_rect = message_text.get_rect()
    message_rect.midtop = (window_width // 2, 50)
    window.blit(message_text, message_rect)

    # Render the user input
    input_text = message_font.render(user_input, True, WHITE)
    input_rect = input_text.get_rect()
    input_rect.midtop = (window_width // 2, 100)
    window.blit(input_text, input_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
