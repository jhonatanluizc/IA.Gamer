import pygame
import game


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y, self.game.WHITE)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.fatecx, self.fatecy = self.mid_w + 100, self.mid_h + 120
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Trabalho de inteligencia artificial', 25, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 - 250, self.game.WHITE)
            self.game.draw_text('PACMAN', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100, self.game.YELLOW)
            self.game.draw_text("Iniciar", 20, self.startx, self.starty, self.game.WHITE)
            self.game.draw_text("Opcoes", 20, self.optionsx, self.optionsy, self.game.WHITE)
            self.game.draw_text("Creditos", 20, self.creditsx, self.creditsy, self.game.WHITE)
            self.game.draw_text("Fatec Cruzeiro 2021", 10, self.fatecx, self.fatecy, self.game.WHITE)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Pacman'
        self.pacmanx, self.pacmany = self.mid_w, self.mid_h + 20
        self.ghostx, self.ghosty = self.mid_w, self.mid_h + 40
        self.passosx, self.passosy = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.pacmanx -20+ self.offset, self.pacmany)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Escolha o algoritmo e Numero de Passos', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30,
                                self.game.WHITE)
            self.game.draw_text("Pacman", 15, self.pacmanx, self.pacmany, self.game.WHITE)
            self.game.draw_text("Fantasmas", 15, self.ghostx, self.ghosty, self.game.WHITE)
            self.game.draw_text("Numero de passos", 15, self.passosx, self.passosy, self.game.WHITE)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.DOWN_KEY:
            if self.state == 'Pacman':
                self.cursor_rect.midtop = ((self.ghostx-20) + self.offset, self.ghosty)
                self.state = 'Fantasmas'
            elif self.state == 'Fantasmas':
                self.cursor_rect.midtop = ((self.passosx-20) + self.offset, self.passosy)
                self.state = 'Passos'
            elif self.state == 'Passos':
                self.cursor_rect.midtop = ((self.pacmanx-20)+ self.offset, self.pacmany)
                self.state = 'Pacman'
        elif self.game.UP_KEY:
            if self.state == 'Pacman':
                self.cursor_rect.midtop = ((self.passosx-20) + self.offset, self.passosy)
                self.state = 'Passos'
            elif self.state == 'Passos':
                self.cursor_rect.midtop = ((self.ghostx-20) + self.offset, self.ghosty)
                self.state = 'Fantasmas'
            elif self.state == 'Fantasmas':
                self.cursor_rect.midtop = ((self.pacmanx-20)+ self.offset, self.pacmany)
                self.state = 'Pacman'
        elif self.game.START_KEY:
            if self.state == 'Pacman':
                self.game.curr_menu = self.game.pacman
                self.run_display = False
            elif self.state == 'Fantasmas':
                self.game.curr_menu = self.game.ghost
                self.run_display = False
            elif self.state == 'Passos':
                self.game.curr_menu = self.game.passos
                self.run_display = False


class PacmanMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Amplitude'
        self.amplitudex, self.amplitudey = self.mid_w, self.mid_h + 20
        self.profundidadex, self.profundidadey = self.mid_w, self.mid_h + 40
        self.profundidadeintx, self.profundidadeinty = self.mid_w, self.mid_h + 60
        self.profundidadelimx, self.profundidadelimy = self.mid_w, self.mid_h + 80
        self.bidirecionalx, self.bidirecionaly = self.mid_w, self.mid_h + 100
        self.custouniformex, self.custouniformey = self.mid_w, self.mid_h + 120
        self.greedyx, self.greedyy = self.mid_w, self.mid_h + 140
        self.estrelax, self.estrelay = self.mid_w, self.mid_h + 160
        self.cursor_rect.midtop = (self.amplitudex + self.offset, self.amplitudey)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Algoritmo dos Pacman', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100,
                                self.game.YELLOW)
            self.game.draw_text("Amplitude", 15, self.amplitudex, self.amplitudey, self.game.WHITE)
            self.game.draw_text("Profundidade", 15, self.profundidadex, self.profundidadey, self.game.WHITE)
            self.game.draw_text("Aprofundamento iterativo", 15, self.profundidadeintx, self.profundidadeinty,
                                self.game.WHITE)
            self.game.draw_text("Profundidade limitado", 15, self.profundidadelimx, self.profundidadelimy,
                                self.game.WHITE)
            self.game.draw_text("Bidirecional", 15, self.bidirecionalx, self.bidirecionaly, self.game.WHITE)
            self.game.draw_text("Custo Uniforme", 15, self.custouniformex, self.custouniformey, self.game.WHITE)
            self.game.draw_text("Greedy", 15, self.greedyx, self.greedyy, self.game.WHITE)
            self.game.draw_text("Estrela", 15, self.estrelax, self.estrelay, self.game.WHITE)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        elif self.game.START_KEY:
            if self.state == 'Amplitude':
                game.pacmanRoute = 'amplitude'
                self.game.curr_menu = self.game.options
                self.run_display = False
            if self.state == 'Profundidade':
                game.pacmanRoute = 'profundidade'
                self.game.curr_menu = self.game.options
                self.run_display = False
            if self.state == 'Aprofundamento iterativo':
                game.pacmanRoute = 'aprofundamento iterativo'
                self.game.curr_menu = self.game.options
                self.run_display = False
            if self.state == 'Profundidade limitado':
                game.pacmanRoute = 'profundidade limitada'
                self.game.curr_menu = self.game.profundidade
                self.run_display = False
            if self.state == 'Bidirecional':
                game.pacmanRoute = 'bidirecional'
                self.game.curr_menu = self.game.options
                self.run_display = False
            if self.state == 'Custo Uniforme':
                game.pacmanRoute = 'custo uniforme'
                self.game.curr_menu = self.game.options
                self.run_display = False
            if self.state == 'Greedy':
                game.pacmanRoute = 'greedy'
                self.game.curr_menu = self.game.options
                self.run_display = False
            if self.state == 'Estrela':
                game.pacmanRoute = 'estrela'
                self.game.curr_menu = self.game.options
                self.run_display = False

        elif self.game.DOWN_KEY:
            if self.state == 'Amplitude':
                self.cursor_rect.midtop = (self.profundidadex + self.offset, self.profundidadey)
                self.state = 'Profundidade'
            elif self.state == 'Profundidade':
                self.cursor_rect.midtop = (self.profundidadeintx + -180, self.profundidadeinty)
                self.state = 'Aprofundamento iterativo'
            elif self.state == 'Aprofundamento iterativo':
                self.cursor_rect.midtop = (self.profundidadelimx + -180, self.profundidadelimy)
                self.state = 'Profundidade limitado'
            elif self.state == 'Profundidade limitado':
                self.cursor_rect.midtop = (self.bidirecionalx + self.offset, self.bidirecionaly)
                self.state = 'Bidirecional'
            elif self.state == 'Bidirecional':
                self.cursor_rect.midtop = (self.custouniformex + -120, self.custouniformey)
                self.state = 'Custo Uniforme'
            elif self.state == 'Custo Uniforme':
                self.cursor_rect.midtop = (self.greedyx + self.offset, self.greedyy)
                self.state = 'Greedy'
            elif self.state == 'Greedy':
                self.cursor_rect.midtop = (self.estrelax + self.offset, self.estrelay)
                self.state = 'Estrela'
            elif self.state == 'Estrela':
                self.cursor_rect.midtop = (self.amplitudex + self.offset, self.amplitudey)
                self.state = 'Amplitude'

        elif self.game.UP_KEY:
            if self.state == 'Amplitude':
                self.cursor_rect.midtop = (self.estrelax + self.offset, self.estrelay)
                self.state = 'Estrela'
            elif self.state == 'Estrela':
                self.cursor_rect.midtop = (self.greedyx + self.offset, self.greedyy)
                self.state = 'Greedy'
            elif self.state == 'Greedy':
                self.cursor_rect.midtop = (self.custouniformex + -120, self.custouniformey)
                self.state = 'Custo Uniforme'
            elif self.state == 'Custo Uniforme':
                self.cursor_rect.midtop = (self.bidirecionalx + self.offset, self.bidirecionaly)
                self.state = 'Bidirecional'
            elif self.state == 'Bidirecional':
                self.cursor_rect.midtop = (self.profundidadelimx + -180, self.profundidadelimy)
                self.state = 'Profundidade limitado'
            elif self.state == 'Profundidade limitado':
                self.cursor_rect.midtop = (self.profundidadeintx + -180, self.profundidadeinty)
                self.state = 'Aprofundamento iterativo'
            elif self.state == 'Aprofundamento iterativo':
                self.cursor_rect.midtop = (self.profundidadex + self.offset, self.profundidadey)
                self.state = 'Profundidade'
            elif self.state == 'Profundidade':
                self.cursor_rect.midtop = (self.amplitudex + self.offset, self.amplitudey)
                self.state = 'Amplitude'


class GhostMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Amplitude'
        self.amplitudex, self.amplitudey = self.mid_w, self.mid_h + 20
        self.profundidadex, self.profundidadey = self.mid_w, self.mid_h + 40
        self.profundidadeintx, self.profundidadeinty = self.mid_w, self.mid_h + 60
        self.profundidadelimx, self.profundidadelimy = self.mid_w, self.mid_h + 80
        self.bidirecionalx, self.bidirecionaly = self.mid_w, self.mid_h + 100
        self.custouniformex, self.custouniformey = self.mid_w, self.mid_h + 120
        self.greedyx, self.greedyy = self.mid_w, self.mid_h + 140
        self.estrelax, self.estrelay = self.mid_w, self.mid_h + 160
        self.cursor_rect.midtop = (self.amplitudex + self.offset, self.amplitudey)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Algoritmo dos Fantasmas', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100,
                                self.game.YELLOW)
            self.game.draw_text("Amplitude", 15, self.amplitudex, self.amplitudey, self.game.WHITE)
            self.game.draw_text("Profundidade", 15, self.profundidadex, self.profundidadey, self.game.WHITE)
            self.game.draw_text("Aprofundamento iterativo", 15, self.profundidadeintx, self.profundidadeinty,
                                self.game.WHITE)
            self.game.draw_text("Profundidade limitado", 15, self.profundidadelimx, self.profundidadelimy,
                                self.game.WHITE)
            self.game.draw_text("Bidirecional", 15, self.bidirecionalx, self.bidirecionaly, self.game.WHITE)
            self.game.draw_text("Custo Uniforme", 15, self.custouniformex, self.custouniformey, self.game.WHITE)
            self.game.draw_text("Greedy", 15, self.greedyx, self.greedyy, self.game.WHITE)
            self.game.draw_text("Estrela", 15, self.estrelax, self.estrelay, self.game.WHITE)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        elif self.game.START_KEY:
            if self.state == 'Amplitude':
                game.ghostRoute = "amplitude"
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            if self.state == 'Profundidade':
                game.ghostRoute = "profundidade"
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            if self.state == 'Aprofundamento iterativo':
                game.ghostRoute = "aprofundamento iterativo"
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            if self.state == 'Profundidade limitado':
                game.ghostRoute = "profundidade limitada"
                self.game.curr_menu = self.game.profundidade
                self.run_display = False
            if self.state == 'Bidirecional':
                game.ghostRoute = "bidirecional"
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            if self.state == 'Custo Uniforme':
                game.ghostRoute = "custo uniforme"
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            if self.state == 'Greedy':
                game.ghostRoute = "greedy"
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            if self.state == 'Estrela':
                game.ghostRoute = "estrela"
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

        elif self.game.DOWN_KEY:
            if self.state == 'Amplitude':
                self.cursor_rect.midtop = (self.profundidadex + self.offset, self.profundidadey)
                self.state = 'Profundidade'
            elif self.state == 'Profundidade':
                self.cursor_rect.midtop = (self.profundidadeintx + -180, self.profundidadeinty)
                self.state = 'Aprofundamento iterativo'
            elif self.state == 'Aprofundamento iterativo':
                self.cursor_rect.midtop = (self.profundidadelimx + -180, self.profundidadelimy)
                self.state = 'Profundidade limitado'
            elif self.state == 'Profundidade limitado':
                self.cursor_rect.midtop = (self.bidirecionalx + self.offset, self.bidirecionaly)
                self.state = 'Bidirecional'
            elif self.state == 'Bidirecional':
                self.cursor_rect.midtop = (self.custouniformex + self.offset, self.custouniformey)
                self.state = 'Custo Uniforme'
            elif self.state == 'Custo Uniforme':
                self.cursor_rect.midtop = (self.greedyx + -120, self.greedyy)
                self.state = 'Greedy'
            elif self.state == 'Greedy':
                self.cursor_rect.midtop = (self.estrelax + self.offset, self.estrelay)
                self.state = 'Estrela'
            elif self.state == 'Estrela':
                self.cursor_rect.midtop = (self.amplitudex + self.offset, self.amplitudey)
                self.state = 'Amplitude'

        elif self.game.UP_KEY:
            if self.state == 'Amplitude':
                self.cursor_rect.midtop = (self.estrelax + self.offset, self.estrelay)
                self.state = 'Estrela'
            elif self.state == 'Estrela':
                self.cursor_rect.midtop = (self.greedyx + self.offset, self.greedyy)
                self.state = 'Greedy'
            elif self.state == 'Greedy':
                self.cursor_rect.midtop = (self.custouniformex + -120, self.custouniformey)
                self.state = 'Custo Uniforme'
            elif self.state == 'Custo Uniforme':
                self.cursor_rect.midtop = (self.bidirecionalx + self.offset, self.bidirecionaly)
                self.state = 'Bidirecional'
            elif self.state == 'Bidirecional':
                self.cursor_rect.midtop = (self.profundidadelimx + -180, self.profundidadelimy)
                self.state = 'Profundidade limitado'
            elif self.state == 'Profundidade limitado':
                self.cursor_rect.midtop = (self.profundidadeintx + -180, self.profundidadeinty)
                self.state = 'Aprofundamento iterativo'
            elif self.state == 'Aprofundamento iterativo':
                self.cursor_rect.midtop = (self.profundidadex + self.offset, self.profundidadey)
                self.state = 'Profundidade'
            elif self.state == 'Profundidade':
                self.cursor_rect.midtop = (self.amplitudex + self.offset, self.amplitudey)
                self.state = 'Amplitude'


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Criado por:', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50,
                                self.game.WHITE)
            self.game.draw_text('Thiago Henrique', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10,
                                self.game.WHITE)
            self.game.draw_text('Hiero Batista', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 40,
                                self.game.WHITE)
            self.game.draw_text('Vitoria Narsciso', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 70,
                                self.game.WHITE)
            self.game.draw_text('Diego Paiva', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 100,
                                self.game.WHITE)
            self.game.draw_text('Brayan Marcelo', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 130,
                                self.game.WHITE)
            self.blit_screen()

class PassosMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        game.numeroPassos = ''
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Execucao a quantos passos?', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50,
                                self.game.WHITE)
            self.game.draw_text('Digite a quantidade e pressione enter:', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2,
                                self.game.WHITE)
            self.game.draw_text(game.numeroPassos, 15, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 + 20,
                                self.game.WHITE)
            self.pressNum()
            self.blit_screen()

    def pressNum(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.unicode in '1234567890':
                game.numeroPassos += event.unicode

class ProfundidadeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        game.profundidadeLimitada = ''
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Digite o limite:', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50,
                                self.game.WHITE)
            self.game.draw_text(game.profundidadeLimitada, 15, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2,
                                self.game.WHITE)
            self.pressNum()
            self.blit_screen()

    def pressNum(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.unicode in '1234567890':
                game.profundidadeLimitada += event.unicode
