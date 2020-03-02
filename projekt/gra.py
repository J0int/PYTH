import pygame
import random

POCZĄTEK_RUNDY = 1
odl =0


pygame.init()
pygame.display.set_caption('Prost gra')
ROZMIAR = SZEROKOŚĆ, WYSOKOŚĆ = 1000, 600
ekran = pygame.display.set_mode(ROZMIAR)
BIAŁY = pygame.color.THECOLORS['white']
ZIELONY = pygame.color.THECOLORS['darkgreen']
CZARNY = pygame.color.THECOLORS['black']
CZERWONY = pygame.color.THECOLORS['red']
zegar = pygame.time.Clock()
obraz_statku = "statek.png"
tło = pygame.image.load("tlo.png").convert()
###

class trol():
    def __init__(self):
        self.odl = 0
        self.ilosc = 0
        self.początek_rundy = 1
class Gracz(pygame.sprite.Sprite):
    """ Klasa gracza. """
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(obraz_statku)
        self.rect = self.image.get_rect()
        self.rect.centery = 770
        self.pozycja = 480
        self.ruch = 0
    def update(self):
        """Aktualizacjia położenia obiektu klasy Gracz."""
        if self.rect.centerx < 10:
            if self.ruch > 0:
                self.pozycja += self.ruch
                self.rect.centerx = self.pozycja
            else:
                self.pozycja = self.pozycja
                self.ruch = 0
        elif self.rect.centerx > 990:
            if self.ruch < 0:
                self.pozycja += self.ruch
                self.rect.centerx = self.pozycja
            else:
                self.pozycja = self.pozycja
                self.ruch = 0
        else:
            self.pozycja += self.ruch
            self.rect.centerx = self.pozycja
        
    
    def idź_w_lewo(self):
        self.ruch = -5
        
    def idź_w_prawo(self):
        self.ruch = 5

    def stop(self):
        self.ruch = 0



class Pocisk(pygame.sprite.Sprite):
    """ Klasa reprezentująca klasę pocisku."""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(BIAŁY)
        self.rect = self.image.get_rect()

    def update(self):
        """ Przesuwanie pocisku """
        self.rect.centery -= 7
        
class Pocisk_wroga(pygame.sprite.Sprite):
    """ Klasa reprezentująca klasę pocisku."""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 8])
        self.image.fill(CZERWONY)
        self.rect = self.image.get_rect()

    def update(self):
        """ Przesuwanie pocisku """
        self.rect.centery += 5

class Wróg(pygame.sprite.Sprite):
    """Klasa wroga."""
    global odl
    odl = 0
    def __init__(self, pozycja_x, pozycja_y):
        super().__init__()
        self.image = pygame.image.load('wrog_1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = pozycja_x
        self.rect.centery = pozycja_y
        self.koniec_ustawiania = 0
        self.koniec_ustawiania_2 = 0
        self.ustawiony = 0
        self.ruch = random.randint(12,20) 
        self.kierunek_ruchu = "p"
        self.licznik_ruchów = 0

    def update(self, typ_przeciwnika = 1):
        if  Trol.początek_rundy:
            self.ustaw_przeciwnikow(typ_przeciwnika)
            if Trol.ilosc == 20:
                Trol.początek_rundy = 0
        
       #funkcja która porusza troche przeciwnikami
        if self.ustawiony == 1:
            #pass
            self.ruszaj()
        czy_strzał = random.randint(1,50)
        if czy_strzał == 2:
            pocisk_wroga = Pocisk_wroga()
            pocisk_wroga.rect.center = self.rect.center
            lista_wszystkich_obiektów.add(pocisk_wroga)
            lista_pocisków_wroga.add(pocisk_wroga)
            
        #funkcja która obniża przeciwników gdy jest ich 3 lub mniej
        #strzelanie przeciwników
    def ruszaj(self):
        if self.kierunek_ruchu == "p" and self.licznik_ruchów < self.ruch:
            self.rect.centerx += 1
            self.licznik_ruchów += 1
        if self.kierunek_ruchu == "l" and self.licznik_ruchów < self.ruch:
            self.rect.centerx -= 1
            self.licznik_ruchów += 1
        if self.licznik_ruchów >= self.ruch :
            if self.kierunek_ruchu == "p":
                self.kierunek_ruchu = "l"
                self.licznik_ruchów = 0
            elif self.kierunek_ruchu == "l":
                self.kierunek_ruchu = "p"
                self.licznik_ruchów=0
                
    def ustaw_przeciwnikow(self,typ_przeciwnika = 1):
        #ustawiam przeciwnikow:
        if typ_przeciwnika == 1:
            if self.rect.centerx < 850 and self.koniec_ustawiania == 0:
                self.rect.centerx += 5
            if self.rect.centerx <860 and self.rect.centerx > 800 and self.koniec_ustawiania == 0:
                if self.rect.centery < 500:
                    self.rect.centery +=5
            if self.rect.centery < 500 and self.rect.centery > 490:
                self.koniec_ustawiania = 1
            if self.koniec_ustawiania == 1 and self.koniec_ustawiania_2 == 0:
                if self.rect.centerx >= 100:
                    self.rect.centery -= 1
                    self.rect.centerx -= 6
                else:
                    self.koniec_ustawiania_2 = 1
                    if Trol.ilosc < 10:
                        self.rect.centery = 100
                        self.ustawiony = 1
                    else:
                        self.rect.centery = 200
                    
                    self.rect.centerx = 50 + Trol.odl
                    Trol.odl += 100
                    Trol.ilosc += 1
                    self.ustawiony = 1
                    if Trol.ilosc == 10:
                        Trol.odl = 20
                     
               
    
Trol =  trol()

lista_wszystkich_obiektów = pygame.sprite.Group()
lista_pocisków = pygame.sprite.Group()
lista_wrogów = pygame.sprite.Group()
lista_pocisków_wroga = pygame.sprite.Group()
lista_graczy= pygame.sprite.Group()


# tworzenie obiektu gracza
gracz = Gracz()
lista_wszystkich_obiektów.add(gracz)
lista_graczy.add(gracz)
odl = 0
for i in range(20):
    wróg = Wróg(30-odl,30)
    lista_wrogów.add(wróg)
    lista_wszystkich_obiektów.add(wróg)
    odl += 80

punkty = 0
punkty_font = pygame.font.Font(None,30)
punkty_obj = punkty_font.render("Score: {0}".format(punkty),1,BIAŁY)
ekran.blit(punkty_obj, [70,70])

życia = 3
życia_font = pygame.font.Font(None,30)
życia_obj = życia_font.render("Live(s): {0}".format(życia),1,BIAŁY)
ekran.blit(życia_obj, [10,50])



# pętla gry

okno_otwarte = True

while okno_otwarte:
    ekran.blit(tło, [0, 0])
    # pętla zdarzeń
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            okno_otwarte = False

        if zdarzenie.type == pygame.KEYDOWN:
            #poruszenie się gracza
            if zdarzenie.key== pygame.K_a:
                gracz.idź_w_lewo()
            if zdarzenie.key == pygame.K_d:
                gracz.idź_w_prawo()
            if zdarzenie.key == pygame.K_SPACE:
                pocisk = Pocisk()
                pocisk.rect.center = gracz.rect.center
                lista_wszystkich_obiektów.add(pocisk)
                lista_pocisków.add(pocisk)

        if zdarzenie.type == pygame.KEYUP:
            if zdarzenie.key == pygame.K_a and gracz.ruch < 0:
                gracz.stop()
            if zdarzenie.key == pygame.K_d and gracz.ruch > 0:
                gracz.stop()
    
    # aktualizacja obiektów
    lista_wszystkich_obiektów.update()

    for pocisk_wroga in lista_pocisków_wroga:
        if pygame.sprite.spritecollide(pocisk_wroga, lista_graczy, True):
            życia -= 1
            życia_obj = życia_font.render("Live(s): {0}".format(życia),1,BIAŁY)

            gracz.pozycja = 470
            lista_wszystkich_obiektów.add(gracz)
            lista_graczy.add(gracz)
            # niszecenie pocisków wychodzących poza planszę
        if pocisk_wroga.rect.centery > 810:
            lista_pocisków_wroga.remove(pocisk_wroga)
            lista_wszystkich_obiektów.remove(pocisk_wroga)
            
            

    # sprawdzaznie czy pocisk trafił w cel
    for pocisk in lista_pocisków:
        lista_trafionych_wrogów = pygame.sprite.spritecollide(pocisk, lista_wrogów, True)
 
        # dla trafionych bloczków liczymy punkty
        for wróg in lista_trafionych_wrogów:
            lista_pocisków.remove(pocisk)
            lista_wszystkich_obiektów.remove(pocisk)
            punkty += 1
            punkty_obj = punkty_font.render("Score: {0}".format(punkty),1,BIAŁY)
            
 
        # niszecenie pocisków wychodzących poza planszę
        if pocisk.rect.centery < -10:
            lista_pocisków.remove(pocisk)
            lista_wszystkich_obiektów.remove(pocisk)
      

    # czyszczenie ekranu
    #ekran.fill(CZARNY)
    # rysowanie wszystkich obiektów
    lista_wszystkich_obiektów.draw(ekran)
    
    ekran.blit(punkty_obj, [10,10])
    
    # aktualizacja ekrany po narysowaniu
    pygame.display.flip()
    
    zegar.tick(60)

    
pygame.quit()
