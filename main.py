import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("english proj")
font = pygame.font.SysFont("Times New Roman", 20)

def create_buttons(img_rect):
    buttons = []
    spacing_x = 320
    spacing_y = 55
    start_x = WIDTH // 2 - spacing_x // 2 - 150
    start_y = img_rect.bottom + 80

    for i in range(4):
        x = start_x if i % 2 == 0 else start_x + spacing_x
        y = start_y + (i // 2) * spacing_y
        rect = pygame.Rect(x, y, 300, 45)
        buttons.append(rect)
    return buttons

def draw_buttons(buttons, labels):
    for i, rect in enumerate(buttons):
        pygame.draw.rect(screen, (30, 30, 30), rect, border_radius=10)
        text = font.render(labels[i], True, (255, 255, 255))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

def draw_input_box(box, user_text, active):
    color = (255, 255, 255) if active else (180, 180, 180)
    max_width = box.width - 20
    words = user_text.split(" ")
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] < max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())

    line_height = font.get_height()
    new_height = max(45, 10 + line_height * len(lines))
    box.height = new_height

    pygame.draw.rect(screen, color, box, 2, border_radius=10)

    if user_text == "":
        placeholder = font.render("Type here...", True, (180, 180, 180))
        screen.blit(placeholder, (box.x + 10, box.y + 8))
    else:
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (box.x + 10, box.y + 8 + i * line_height))


def make_slide(image=None, question="", choices=None):
    if image:
        img = pygame.image.load(image)
        img_rect = img.get_rect()
        img_rect.centerx = WIDTH // 2
        img_rect.top = 50
    else:
        img = None
        img_rect = pygame.Rect(0, 0, 0, 0)
        img_rect.bottom = 50

    question_text = font.render(question, True, (255, 255, 255))
    question_rect = question_text.get_rect(center=(WIDTH // 2, img_rect.bottom + 30))

    if choices:
        buttons = create_buttons(img_rect)
        selected = None
    else:
        input_box = pygame.Rect(WIDTH // 2 - 200, img_rect.bottom + 80, 400, 45)
        active = False
        user_text = ""
        selected = None

    while selected is None:
        screen.fill((30, 30, 30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if choices:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for i, rect in enumerate(buttons):
                        if rect.collidepoint(event.pos):
                            selected = choices[i]
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    active = input_box.collidepoint(event.pos)
                elif event.type == pygame.KEYDOWN and active:
                    if event.key == pygame.K_RETURN:
                        selected = user_text
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        if img:
            screen.blit(img, img_rect)
        screen.blit(question_text, question_rect)

        if choices:
            draw_buttons(buttons, choices)
        else:
            draw_input_box(input_box, user_text, active)

        pygame.display.flip()
    return selected

choice1 = make_slide("image1.jpg", "johgnson", ["A", "B", "C", "D"])
text_response = make_slide("image2.jpg", "dsabnanbsdj:")
choice1 = make_slide("image1.jpg", "ababhbdas", ["A", "B", "C", "D"])








end_text = font.render("the end!", True, (255, 255, 255))
end_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.fill((30, 30, 30))
screen.blit(end_text, end_rect)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
