import pygame
import sys # sys does stuff
pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("english proj")
font = pygame.font.SysFont("Times New Roman", 15)

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
        placeholder = font.render("Enter corresponding outcome in Salem", True, (180, 180, 180))
        screen.blit(placeholder, (box.x + 10, box.y + 8))
    else:
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (box.x + 10, box.y + 8 + i * line_height))


def make_slide(image=None, question="", choices=None, a=1, b=1):
    
    if image:
        img = pygame.image.load(image)
        img = pygame.transform.scale(img, (img.get_width()*a, img.get_height()*b))
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



choice1 = make_slide("salem_1692.jpg", "Salem, 1692: Your neighbor's pigs died after your argument. You're accused of witchcraft. First move:", ["Deny", "False confession", "Stay silent", ""], a=.15, b=.15)

match choice1:
    case "Deny":
        choice2 = make_slide("mccarthy.jpg", "1953 court case: You deny all the accusations. 'Only guilty people deny!' the council says. Next move:", ["Ask for lawyer", "Plead Fifth", "Name peers", "Accuse council"], a=1.15, b=1.15)
        match choice2:
            case "Ask for lawyer":
                choice3 = make_slide("salem_1692.jpg", "Salem: The judge yells 'Devil's agents do not need defense!' Final move:", ["Quote Bible", "Curse the court", "Say you're pregnant", "Claim accusers are witches"], a=.15, b=.15)
                match choice3:
                    case "Quote Bible": make_slide("mccarthy.jpg", "1953 Outcome: Cited for contempt. Blacklisted. Can't find work for decades.", a=1.15, b=1.15)
                    case "Curse the court": make_slide("mccarthy.jpg", "1953 Outcome: Declared mentally unstable. Confined to asylum 'rehabilitation'.", a=1.15, b=1.15)
                    case "Say you're pregnant": make_slide("mccarthy.jpg", "1953 Outcome: Put under FBI surveillance until 'proof' emerges.", a=1.15, b=1.15)
                    case "Claim accusers are witches": make_slide("mccarthy.jpg", "1953 Outcome: Countersuit backfires. labeled 'agitator.' Passport revoked.", a=1.15, b=1.15)
            case "Plead Fifth":
                choice3 = make_slide("salem_1692.jpg", "Salem: They say the devil has stopped you from speaking so they try to test your fate. Next move:", ["Say a prayer", "Stay silent", "Fake possession", "False confession"], a=.15, b=.15)
                match choice3:
                    case "Say a prayer": make_slide("mccarthy.jpg", "1953 Outcome: Career over, house vandalized.", a=1.15, b=1.15)
                    case "Stay silent": make_slide("mccarthy.jpg", "1953 Outcome: Expelled from union. Can't work legally again.", a=1.15, b=1.15)
                    case "Fake possession": make_slide("mccarthy.jpg", "1953 Outcome: Committed for CIA anti-communist experiments.", a=1.15, b=1.15)
                    case "False confession": make_slide("mccarthy.jpg", "1953 Outcome: Become informant naming old friends.", a=1.15, b=1.15)
            case "Name peers":
                choice3 = make_slide("salem_1692.jpg", "Salem: You name others. They demand evidence. Next move:", ["Bring poppet", "Point at shadow", "Cry", "Refuse"], a=.15, b=.15)
                match choice3:
                    case "Bring poppet": make_slide("mccarthy.jpg", "1953 Outcome: Possibly forged letters turn up and 'prove' your claims. Keep your job.", a=1.15, b=1.15)
                    case "Point at shadow": make_slide("mccarthy.jpg", "1953 Outcome: Your accusations spark office purges. Promoted because fear.", a=1.15, b=1.15)
                    case "Cry": make_slide("mccarthy.jpg", "1953 Outcome: Hailed as hero and patriot. Forced to testify at 28 hearings.", a=1.15, b=1.15)
                    case "Refuse": make_slide("mccarthy.jpg", "1953 Outcome: Marked 'unreliable.' Lose your job.", a=1.15, b=1.15)
            case "Accuse council":
                choice3 = make_slide("salem_1692.jpg", "Salem: You accuse the judge of witchcraft. Chaos erupts. Final move:", ["Present 'proof'", "Flee", "", ""], a=.15, b=.15)
                match choice3:
                    case "Present 'proof'": make_slide("mccarthy.jpg", "1953 Outcome: Found guilty of perjury.", a=1.15, b=1.15)
                    case "Flee": make_slide("mccarthy.jpg", "1953 Outcome: Escape to Mexico. Communist rumors follows you.", a=1.15, b=1.15)

    case "False confession":
        choice2 = make_slide("mccarthy.jpg", "1953: You admit past Party ties to save career and name some of your peers. The council demands proof:", ["Bring poppet", "Point at shadow", "Cry", "Refuse"], a=1.15, b=1.15)
        match choice2:
            case "Bring poppet": make_slide("mccarthy.jpg", "1953 Outcome: Possibly forged letters turn up and 'prove' your claims. Keep your job.", a=1.15, b=1.15)
            case "Point at shadow": make_slide("mccarthy.jpg", "1953 Outcome: Your accusations spark office purges. Promoted because fear.", a=1.15, b=1.15)
            case "Cry": make_slide("mccarthy.jpg", "1953 Outcome: Hailed as hero and patriot. Forced to testify at 28 hearings.", a=1.15, b=1.15)
            case "Refuse": make_slide("mccarthy.jpg", "1953 Outcome: Marked 'unreliable.' Lose your job.", a=1.15, b=1.15)
    case "Stay silent":
        choice2 = make_slide("mccarthy.jpg", "1953: You invoke the Fifth Amendment. The committee threatens you and your friends' careers.", ["Testify to protect them", "Stay silent", "Demand defense", ""], a=1.15, b=1.15)
        match choice2:
            case "Testify to protect them":
                choice3 = make_slide("salem_1692.jpg", "Salem: To save your friends, you speak — but your voice cracks. The crowd becomes even MORE suspicuous.", ["Blame the Devil", "Claim illness", "Collapse", ""], a=.15, b=.15)
                match choice3:
                    case "Blame the Devil": make_slide("mccarthy.jpg", "1953 Outcome: They say you've been 'brainwashed.' Forced into CIA anti-communist experiments", a=1.15, b=1.15)
                    case "Claim illness": make_slide("mccarthy.jpg", "1953 Outcome: Called a security risk. Fired, medical help denied.", a=1.15, b=1.15)
                    case "Collapse": make_slide("mccarthy.jpg", "1953 Outcome: Weakness is guilt! Become social outcast.", a=1.15, b=1.15)
            case "Stay silent":
                choice3 = make_slide("salem_1692.jpg", "Salem: You rot in jail. The council offers one last deal: confess or hang.", ["Confess falsely", "Stay defiant", "Bribe guard", "Write confession"], a=.15, b=.15)
                match choice3:
                    case "Confess falsely": make_slide("mccarthy.jpg", "1953 Outcome: Forced to confess on radio. Still added to Hollywood blacklist.", a=1.15, b=1.15)
                    case "Stay defiant": make_slide("mccarthy.jpg", "1953 Outcome: Guilty for contempt of court. Sent to federal prison for sedition.", a=1.15, b=1.15)
                    case "Bribe guard": make_slide("mccarthy.jpg", "1953 Outcome: Bribe discovered. Sent to prison.", a=1.15, b=1.15)
                    case "Write confession": make_slide("mccarthy.jpg", "1953 Outcome: Confession becomes bestseller. You're rich!", a=1.15, b=1.15)
            case "Demand defense":
                choice3 = make_slide("salem_1692.jpg", "Salem: 'Lawyers defend only the guilty!' they shout. Final choice:", ["Quote law", "Insist on rights", "Attack the judge", "Apologize"], a=.15, b=.15)
                match choice3:
                    case "Quote English law": make_slide("mccarthy.jpg", "1953 Outcome: Foreign influence accusation. Citizenship taken away.", a=1.15, b=1.15)
                    case "Insist on rights": make_slide("mccarthy.jpg", "1953 Outcome: Rights = Communism, Jailed without trial for 2 years.", a=1.15, b=1.15)
                    case "Attack the judge": make_slide("mccarthy.jpg", "1953 Outcome: Beaten for resisting arrest. Left crippled, unemployed.", a=1.15, b=1.15)
                    case "Apologize": make_slide("mccarthy.jpg", "1953 Outcome: Apology aired on radio. Hired as McCarthy's janitor.", a=1.15, b=1.15)












end_text = font.render("the end!", True, (255, 255, 255))
end_text2 = font.render("", True, (255, 255, 255))
end_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
end_rect2 = end_text2.get_rect(center=(WIDTH // 2, (HEIGHT // 2)+25))
screen.fill((30, 30, 30))
screen.blit(end_text, end_rect)
screen.blit(end_text2, end_rect2)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
