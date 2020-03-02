import pygame, random

POCZĄTEK_RUNDY = 1
odl =0


pygame.init()
pygame.display.set_caption('Prost gra')
ROZMIAR = SZEROKOŚĆ, WYSOKOŚĆ = 1000, 800
ekran = pygame.display.set_mode(ROZMIAR)
BIAŁY = pygame.color.THECOLORS['white']
ZIELONY = pygame.color.THECOLORS['darkgreen']
CZARNY = pygame.color.THECOLORS['black']
CZERWONY = pygame.color.THECOLORS['red']
CIEMNY_CZERWONY = CZERWONY = pygame.color.THECOLORS['darkred']
zegar = pygame.time.Clock()
obraz_statku = "statek.png"
obraz_statku_z_tarcza = "statek_z_tarcza.png"
tło = pygame.image.load("tlo.png").convert()
###

class trol():
    def __init__(self):
        self.odl = 0
        self.ilosc = 0
        self.początek_rundy = 1
        self.początek_gry = 1
        self.flaga_czasu = 0
        self.czas = 0
        self.odl = 0
    def reset(self, gracz):
        lista_wrogów.empty()
        lista_wszystkich_obiektów.empty()
        lista_wszystkich_obiektów.add(gracz)
        lista_graczy.add(gracz)
        
    def odczekaj(self, czas):
        if self.flaga_czasu == 0:
            self.czas = pygame.time.get_ticks() + czas
            self.flaga_czasu = 1
            return 0
        if pygame.time.get_ticks() >= self.czas :
            self.flaga_czasu = 0
            return 1
    #def stwórz_przeciwników(self):
        #if 1:
            #for i in range(19):
                #wróg = Wróg(30-self.odl,30)
                #lista_wrogów.add(wróg)
               # lista_wszystkich_obiektów.add(wróg)
               # self.odl += 80
    
class Gracz(pygame.sprite.Sprite):
    """ Klasa gracza. """
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(obraz_statku)
        self.rect = self.image.get_rect()
        self.rect.centery = 770
        self.pozycja = 480
        self.ruch = 0
        self.życia = 3
        self.wrażliwy = 1
        self.flaga_czasu = 0
        self.czas = 0
    def reset(self):
        self.rect.centery = 770
        self.pozycja = 480
        self.ruch = 0
        self.życia = 3
        self.wrażliwy = 1
        self.flaga_czasu = 0
        self.czas = 0
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

    def sprawdź_czy_wrażliwy(self):
        if self.flaga_czasu == 0:
            self.image = pygame.image.load(obraz_statku_z_tarcza)
            self.czas = pygame.time.get_ticks() + 1500
            self.flaga_czasu = 1
            
        if pygame.time.get_ticks() >= self.czas :
            self.image = pygame.image.load(obraz_statku)
            self.wrażliwy = 1
            self.flaga_czasu = 0
        



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
        self.ruch = random.randint(12,30) 
        self.kierunek_ruchu = "p"
        self.licznik_ruchów = 0
        self.ko_x = 100
        self.ko_y = 100
        self.flaga_y = 0
        self.flaga_x = 0

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
        if self.flaga_y == 1 and self.flaga_x == 1:
            self.ustawiony=1
        if typ_przeciwnika == 1:
            if self.rect.centerx < 850 and self.koniec_ustawiania == 0:
                self.rect.centerx += 5
            if self.rect.centerx < 860 and self.rect.centerx > 750 and self.koniec_ustawiania == 0:
                if self.rect.centery < 500:
                    self.rect.centery +=5
            if self.rect.centery < 500 and self.rect.centery > 490:
                self.koniec_ustawiania = 1
            if self.koniec_ustawiania == 1 and self.koniec_ustawiania_2 == 0:
                if self.rect.centerx >= 80:
                    self.rect.centery -= 1
                    self.rect.centerx -= 6
                else:
                    self.koniec_ustawiania_2 = 1
                    if Trol.ilosc < 10:
                        self.ko_y = 100
                    else:
                        self.ko_y = 200
                    
                    self.ko_x = 50 + Trol.odl
                    Trol.odl += 100
                    Trol.ilosc += 1
                    if Trol.ilosc == 10:
                        Trol.odl = 20
            if self.koniec_ustawiania == 1 and self.koniec_ustawiania_2 == 1 and self.ustawiony == 0:
                if self.rect.centery > self.ko_y:
                    self.rect.centery -= 2
                else:
                    self.flaga_y = 1 
                if self.rect.centerx < self.ko_x:
                    self.rect.centerx += 10
                else:
                    self.flaga_x = 1
            
            
                     
             
    
Trol =  trol()

lista_wszystkich_obiektów = pygame.sprite.Group()
lista_pocisków = pygame.sprite.Group()
lista_wrogów = pygame.sprite.Group()
lista_pocisków_wroga = pygame.sprite.Group()
lista_graczy= pygame.sprite.Group()

odl = 0
for i in range(19):
    wróg = Wróg(30-odl,30)
    lista_wrogów.add(wróg)
    lista_wszystkich_obiektów.add(wróg)
    odl += 80


# tworzenie obiektu gracza
gracz = Gracz()
lista_wszystkich_obiektów.add(gracz)
lista_graczy.add(gracz)


punkty = 0
punkty_font = pygame.font.Font(None,30)
punkty_obj = punkty_font.render("Score: {0}".format(punkty),1,BIAŁY)
ekran.blit(punkty_obj, [10,10])


życia_font = pygame.font.Font(None,30)
życia_obj = życia_font.render("Live(s): {0}".format(gracz.życia),1,BIAŁY)
ekran.blit(życia_obj, [10,50])

kociec_gry = pygame.font.Font(None,60)
kociec_gry_obj = kociec_gry.render("NIE ŻYJESZ",1,CIEMNY_CZERWONY)
ekran.blit(kociec_gry_obj, [400,350])

początek_gry = pygame.font.Font(None,35)
początek_gry_obj = początek_gry.render("Nacisnij spacje aby zacząć.",1,BIAŁY)
ekran.blit(początek_gry_obj, [350,350])


# pętla gry

okno_otwarte = True

while okno_otwarte:
    ekran.blit(tło, [0, 0])
    #początek gry
    if gracz.życia < 0:
        if Trol.odczekaj(1500) :
            Trol.początek_gry = 1
            gracz.życia = 3
            Trol.reset(gracz)
            gracz.reset()
    while Trol.początek_gry and okno_otwarte:
        ekran.blit(początek_gry_obj, [350,350])
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                okno_otwarte = False
            if zdarzenie.type == pygame.KEYDOWN:
                if zdarzenie.key == pygame.K_SPACE:
                    Trol.początek_gry = 0
                    #Trol.stwórz_przeciwników()
        pygame.display.flip()
        zegar.tick(60)

        
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
            if zdarzenie.key == pygame.K_SPACE and  gracz.życia >= 0 :
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
    
    #śmierć gracza
    if gracz.życia < 0:
        ekran.blit(kociec_gry_obj, [400,350])
        lista_wszystkich_obiektów.remove(gracz)
        lista_graczy.remove(gracz)
    # sprawdzaznie czy pocisk trafił w gracza
    for pocisk_wroga in lista_pocisków_wroga:
        if pygame.sprite.spritecollide(pocisk_wroga, lista_graczy, True):
            if gracz.wrażliwy == 1:
                gracz.życia -= 1
                gracz.wrażliwy = 0
                gracz.pozycja = 470
            życia_obj = życia_font.render("Live(s): {0}".format(gracz.życia),1,BIAŁY)
            if gracz.życia >= 0 :
                lista_wszystkich_obiektów.add(gracz)
                lista_graczy.add(gracz)
            #niszecenie pocisków wychodzących poza planszę
        if pocisk_wroga.rect.centery > 810:
            lista_pocisków_wroga.remove(pocisk_wroga)
            lista_wszystkich_obiektów.remove(pocisk_wroga)

    #ochrona po stracie życia      
    if gracz.wrażliwy == 0:
        pass
        gracz.sprawdź_czy_wrażliwy()
  

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
      

    # rysowanie wszystkich obiektów
    lista_wszystkich_obiektów.draw(ekran)
    ekran.blit(punkty_obj, [10,10])
    ekran.blit(życia_obj, [10,50])
    # aktualizacja ekrany po narysowaniu
    pygame.display.flip()
    
    zegar.tick(60)

    
pygame.quit()
