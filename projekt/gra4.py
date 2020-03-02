import pygame, random, pygame.mixer


POCZĄTEK_RUNDY = 15
odl =0

pygame.init()
pygame.mixer.init()

pygame.init()
pygame.display.set_caption('Ferblude')
ROZMIAR = SZEROKOŚĆ, WYSOKOŚĆ = 1000, 800
ekran = pygame.display.set_mode(ROZMIAR)
BIAŁY = pygame.color.THECOLORS['white']
ZIELONY = pygame.color.THECOLORS['darkgreen']
ŻÓŁTY = pygame.color.THECOLORS['yellow']
CZARNY = pygame.color.THECOLORS['black']
CZERWONY = pygame.color.THECOLORS['red']
CIEMNY_CZERWONY = CZERWONY = pygame.color.THECOLORS['darkred']
NIEBIESKI = CZERWONY = pygame.color.THECOLORS['blue']
zegar = pygame.time.Clock()
obraz_statku = "statek.png"
obraz_statku_z_tarcza = "statek_z_tarcza.png"
obraz_wróg_1 = "wrog_1.png"
obraz_wróg_2 = "wrog_2.png"
obraz_życie = "zycie.png"
obraz_borń = "bron.png"
tło = pygame.image.load("tlo.png").convert()

dzwiek_strzal_gracza = pygame.mixer.Sound('strzal_gracza.wav')
dzwiek_strzal_wroga = pygame.mixer.Sound('strzal_wroga.wav')
dzwiek_grab = pygame.mixer.Sound('grab.wav')
dzwiek_zycie = pygame.mixer.Sound('live.wav')
dzwiek_wybuch_wroga = pygame.mixer.Sound('wybuch_wroga.wav')
dzwiek_wybuch_gracza = pygame.mixer.Sound('wybuch_gracza.wav')

dzwiek_strzal_gracza.set_volume(0.35)
dzwiek_strzal_wroga.set_volume(0.15)
dzwiek_grab.set_volume(8.0)
dzwiek_zycie.set_volume(1.0)
dzwiek_wybuch_wroga.set_volume(0.5)
dzwiek_wybuch_gracza.set_volume(1)

pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.stop()

###

class trol():
    def __init__(self):
        self.odl = 0
        self.ilosc = 0
        self.początek_rundy = 1
        self.początek_gry = 1
        self.flaga_czasu = 0
        self.czas = 0
    def odczekaj(self, czas):
        if self.flaga_czasu == 0:
            self.czas = pygame.time.get_ticks() + czas
            self.flaga_czasu = 1
            return 0
        if pygame.time.get_ticks() >= self.czas :
            self.flaga_czasu = 0
            return 1
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
        self.rodzaj_broni = 1
        self.strzał = 0
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

    def sprawdź_czy_wrażliwy(self,czas):
        if self.flaga_czasu == 0:
            self.image = pygame.image.load(obraz_statku_z_tarcza)
            self.czas = pygame.time.get_ticks() + czas
            self.flaga_czasu = 1
            
        if pygame.time.get_ticks() >= self.czas :
            self.image = pygame.image.load(obraz_statku)
            self.wrażliwy = 1
            self.flaga_czasu = 0
        



class Pocisk(pygame.sprite.Sprite):
    """ Klasa reprezentująca klasę pocisku."""
    def __init__(self,kolor):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(kolor)
        self.rect = self.image.get_rect()
        self.szybkość_pocisku = 8
        

    def update(self):
        """ Przesuwanie pocisku """
        self.rect.centery -= self.szybkość_pocisku

class Pocisk_2(pygame.sprite.Sprite):
    """ Klasa reprezentująca klasę pocisku."""
    def __init__(self,kolor):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(kolor)
        self.rect = self.image.get_rect()
        self.szybkość_pocisku = 8
        

    def update(self):
        """ Przesuwanie pocisku """
        self.rect.centery -= self.szybkość_pocisku
        self.rect.centerx -=2

class Pocisk_3(pygame.sprite.Sprite):
    """ Klasa reprezentująca klasę pocisku."""
    def __init__(self, kolor):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(kolor)
        self.rect = self.image.get_rect()
        #strzał_gracza.play()
        self.szybkość_pocisku = 8
        

    def update(self):
        """ Przesuwanie pocisku """
        self.rect.centery -= self.szybkość_pocisku
        self.rect.centerx +=2

class Pocisk_wroga(pygame.sprite.Sprite):
    """ Klasa reprezentująca klasę pocisku."""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 8])
        self.image.fill(CZERWONY)
        self.rect = self.image.get_rect()
        dzwiek_strzal_wroga.play()

    def update(self):
        """ Przesuwanie pocisku """
        self.rect.centery += 5

class Wróg(pygame.sprite.Sprite):
    """Klasa wroga."""
    global odl
    odl = 0
    def __init__(self, pozycja_x, pozycja_y):
        super().__init__()
        self.image = pygame.image.load(obraz_wróg_1)
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
        self.drop_życie = random.randint(1,5)
        self.drop_broń = self.drop_życie - 1
        self.licznik = 80
        
              
    def update(self, typ_przeciwnika = 1):
        if  Trol.początek_rundy:
            self.ustaw_przeciwnikow(typ_przeciwnika)
            if Trol.ilosc == 20:
                Trol.początek_rundy = 0
        
       #funkcja która porusza troche przeciwnikami
        if self.ustawiony == 1:
            #pass
            self.ruszaj()
        if self.licznik < 2:
            self.licznik = 2
        else:
            self.licznik = 80-(nr_rundy * 6)
        czy_strzał = random.randint(1,self.licznik)
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
            if self.rect.centery < 510 and self.rect.centery > 490:
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

class Wróg_2(pygame.sprite.Sprite):
    """Klasa wroga."""
    global odl
    odl = 0
    def __init__(self, pozycja_x, pozycja_y):
        super().__init__()
        self.image = pygame.image.load(obraz_wróg_2)
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
        self.drop_życie = random.randint(1,18)
        self.drop_broń = self.drop_życie - 1
        self.licznik = 50
        
    def update(self, typ_przeciwnika = 1):
        if  Trol.początek_rundy:
            self.ustaw_przeciwnikow(typ_przeciwnika)
            if Trol.ilosc == 20:
                Trol.początek_rundy = 0
        
       #funkcja która porusza troche przeciwnikami
        if self.ustawiony == 1:
            #pass
            self.ruszaj()
        if self.licznik < 2:
            self.licznik = 2
        else:
            self.licznik = 50-(nr_rundy * 4)
        czy_strzał = random.randint(1,self.licznik)
        
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
            if self.rect.centerx > 10 and self.koniec_ustawiania == 0:
                self.rect.centerx -= 5
                
            if self.rect.centerx > 5 and self.rect.centerx < 250 and self.koniec_ustawiania == 0:
                if self.rect.centery < 700:
                    self.rect.centery +=3
            if self.rect.centery > 700 and self.rect.centery < 710:
                self.koniec_ustawiania = 1
            if self.koniec_ustawiania == 1 and self.koniec_ustawiania_2 == 0:
                if self.rect.centerx <= 980:
                    self.rect.centery -= 1
                    self.rect.centerx += 6
                else:
                    self.koniec_ustawiania_2 = 1
                    if Trol.ilosc < 10:
                        self.ko_y = 200
                    else:
                        self.ko_y = 300
                    
                    self.ko_x = 80 + Trol.odl
                    Trol.odl += 100
                    Trol.ilosc += 1
                    if Trol.ilosc == 10:
                        Trol.odl = 20
            if self.koniec_ustawiania == 1 and self.koniec_ustawiania_2 == 1 and self.ustawiony == 0:
                if self.rect.centery > self.ko_y:
                    self.rect.centery -= 2
                else:
                    self.flaga_y = 1 
                if self.rect.centerx > self.ko_x:
                    self.rect.centerx -= 10
                else:
                    self.flaga_x = 1
                    
class Życie(pygame.sprite.Sprite):
    def __init__(self, odleglosc_x, odleglosc_y):
        super().__init__() 
        self.image = pygame.image.load(obraz_życie)
        self.rect = self.image.get_rect()
        self.rect.centerx = odleglosc_x
        self.rect.centery = odleglosc_y
        self.szybkosc_spadania = random.randint(1,5)
    def update(self):
        self.rect.centery += self.szybkosc_spadania

class Broń(pygame.sprite.Sprite):
    def __init__(self, odleglosc_x, odleglosc_y):
        super().__init__() 
        self.image = pygame.image.load(obraz_borń)
        self.rect = self.image.get_rect()
        self.rect.centerx = odleglosc_x
        self.rect.centery = odleglosc_y
        self.szybkosc_spadania = random.randint(1,5)
    def update(self):
        self.rect.centery += self.szybkosc_spadania
    

while 1:
    pygame.mixer.music.play()
                
    reset = 1
    runda = 1
    nowa_runda = 1
    pauza = trol()
    pauza_2 = trol()
    pauza_3 = trol()
    flaga_pauzy = 1
    reset = 1
    runda =1
    czy_wyświetlić = 0
    Trol =  trol()
    nr_rundy = 1
    czy_poczatkowy_napis = 1
    czy_generować = 0
    czy_zapętlic = 0

    lista_wszystkich_obiektów = pygame.sprite.Group()
    lista_pocisków = pygame.sprite.Group()
    lista_wrogów = pygame.sprite.Group()
    lista_pocisków_wroga = pygame.sprite.Group()
    lista_graczy= pygame.sprite.Group()
    lista_żyć = pygame.sprite.Group()
    lista_broni = pygame.sprite.Group()


    # tworzenie obiektu gracza
    gracz = Gracz()
    lista_wszystkich_obiektów.add(gracz)
    lista_graczy.add(gracz)
    odl = 0
    
    ilość_wrogów = 0
    punkty = 0
    punkty_font = pygame.font.Font(None,22)
    punkty_obj = punkty_font.render("wynik: {0}".format(punkty),1,BIAŁY)
    ekran.blit(punkty_obj, [10,10])


    życia_font = pygame.font.Font(None,22)
    życia_obj = życia_font.render("życia: {0}".format(gracz.życia),1,BIAŁY)
    ekran.blit(życia_obj, [10,50])

    kociec_gry = pygame.font.Font(None,60)
    kociec_gry_obj = kociec_gry.render("NIE ŻYJESZ",1,CIEMNY_CZERWONY)
    ekran.blit(kociec_gry_obj, [400,350])

    początek_gry = pygame.font.Font(None,35)
    początek_gry_obj = początek_gry.render("Nacisnij spacje aby zacząć.",1,BIAŁY)
    ekran.blit(początek_gry_obj, [350,350])

    energia = pygame.font.Font(None,22)
    energia_obj = energia.render("energia: {}%".format(100-gracz.strzał),1,BIAŁY)
    ekran.blit(energia_obj, [10,90])


    runda_napis = pygame.font.Font(None,45)
    runda_napis_obj = runda_napis.render("RUNDA {}".format(nr_rundy),1,BIAŁY)
    




    # pętla gry


    
    okno_otwarte = True
    while okno_otwarte and reset :
        ekran.blit(tło, [0, 0])
        #początek gry
        while Trol.początek_gry and okno_otwarte:
            ekran.blit(początek_gry_obj, [350,350])
            for zdarzenie in pygame.event.get():
                if zdarzenie.type == pygame.QUIT:
                    okno_otwarte = False
                if zdarzenie.type == pygame.KEYDOWN:
                    if zdarzenie.key == pygame.K_SPACE:
                        Trol.początek_gry = 0
            pygame.display.flip()
            zegar.tick(60)
            
       
            
        if czy_poczatkowy_napis:
            ekran.blit(runda_napis_obj, [450,200])
            if pauza_3.odczekaj(2000):
                czy_poczatkowy_napis = 0
                czy_generować = 1
        
        #PĘTLA GENERUJACA WROGÓW W KOLEJNYCH RUNDACH
        if czy_generować:
            if nr_rundy >= 3 and czy_zapętlic:
                runda = 1
            if runda == 1:
                Trol.odl = 0
                Trol.ilosc = 0
                for i in range(19):
                    wróg = Wróg(30-odl,30)
                    lista_wrogów.add(wróg)
                    lista_wszystkich_obiektów.add(wróg)
                    odl += 80
                runda = 0
                nr_rundy += 1
                runda_napis_obj = runda_napis.render("RUNDA {}".format(nr_rundy),1,BIAŁY)
                nowa_runda = 1
                flaga_pauzy = 1
                czy_wyświetlić = 0
                czy_zapętlić = 0
            if runda == 2:
                Trol.odl = 0
                Trol.ilosc = 0
                odl = 0
                for i in range(19):
                    wróg = Wróg_2(1100+odl,200)
                    lista_wrogów.add(wróg)
                    lista_wszystkich_obiektów.add(wróg)
                    odl += 80
                runda = 0
                nr_rundy += 1
                runda_napis_obj = runda_napis.render("RUNDA {}".format(nr_rundy),1,BIAŁY)
                nowa_runda = 1
                flaga_pauzy = 1
                czy_wyświetlić = 0
                czy_zapętlić = 0
            if runda >= 3:
                runda = random.randint(1,2)
                pass

        for i in lista_wrogów.sprites()  :
            ilość_wrogów +=1
            
        if nowa_runda and ilość_wrogów == 0 :
            if pauza.odczekaj(2000):
                czy_wyświetlić = 1
                nowa_runda = 0
                flaga_pauzy = 1
                        
        if czy_wyświetlić == 1:
            if flaga_pauzy and ilość_wrogów == 0 :
                if pauza_2.odczekaj(2000):
                    czy_wyświetlić = 0
                    flaga_pauzy = 0
                    runda = nr_rundy        
            ekran.blit(runda_napis_obj, [450,200])


        if flaga_pauzy and ilość_wrogów == 0 :
            if pauza.odczekaj(2000):
                czy_wyświetlić = 1
                nowa_runda = 0
        
        ilość_wrogów = 0

        
        
            
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
                    energia_obj = energia.render("energia: {}%".format(100-gracz.strzał),1,BIAŁY)
                    if gracz.strzał <= 80:
                        dzwiek_strzal_gracza.play()
                        gracz.strzał += 20
                    if gracz.strzał > 80:
                        pass
                    elif gracz.rodzaj_broni == 1:
                        pocisk = Pocisk(BIAŁY)
                        pocisk.rect.center = gracz.rect.center
                        lista_wszystkich_obiektów.add(pocisk)
                        lista_pocisków.add(pocisk)
                    elif gracz.rodzaj_broni == 2:
                        pocisk = Pocisk(ŻÓŁTY)
                        pocisk.rect.centery = gracz.rect.centery
                        pocisk.rect.centerx = gracz.rect.centerx - 10
                        lista_wszystkich_obiektów.add(pocisk)
                        lista_pocisków.add(pocisk)
                        
                        pocisk2 = Pocisk(ŻÓŁTY)
                        pocisk2.rect.centery = gracz.rect.centery
                        pocisk2.rect.centerx = gracz.rect.centerx + 10
                        lista_wszystkich_obiektów.add(pocisk2)
                        lista_pocisków.add(pocisk2)
                    else:
                        pocisk = Pocisk(NIEBIESKI)
                        pocisk.rect.center = gracz.rect.center
                        lista_wszystkich_obiektów.add(pocisk)
                        lista_pocisków.add(pocisk)

                        pocisk2 = Pocisk_2(NIEBIESKI)
                        pocisk2.rect.center = gracz.rect.center
                        lista_wszystkich_obiektów.add(pocisk2)
                        lista_pocisków.add(pocisk2)

                        pocisk3 = Pocisk_3(NIEBIESKI)
                        pocisk3.rect.center = gracz.rect.center
                        lista_wszystkich_obiektów.add(pocisk3)
                        lista_pocisków.add(pocisk3)
                        
            if zdarzenie.type == pygame.KEYUP:
                if zdarzenie.key == pygame.K_a and gracz.ruch < 0:
                    gracz.stop()
                if zdarzenie.key == pygame.K_d and gracz.ruch > 0:
                    gracz.stop()
        if gracz.strzał > 0:
            gracz.strzał -= 1
        energia_obj = energia.render("energia: {}%".format(100-gracz.strzał),1,BIAŁY)
        # aktualizacja obiektów
        lista_wszystkich_obiektów.update()
    
        #śmierć gracza
        if gracz.życia < 0:
            ekran.blit(kociec_gry_obj, [400,350])
            lista_wszystkich_obiektów.remove(gracz)
            lista_graczy.remove(gracz)
            if pauza_3.odczekaj(4000):
                reset = 0
        
        # sprawdzaznie czy pocisk trafił w gracza
        for pocisk_wroga in lista_pocisków_wroga:
            if pygame.sprite.spritecollide(pocisk_wroga, lista_graczy, True):
                if gracz.wrażliwy == 1:
                    gracz.życia -= 1
                    if gracz.rodzaj_broni > 1:
                        gracz.rodzaj_broni -= 1
                    gracz.wrażliwy = 0
                    dzwiek_wybuch_gracza.play()
                    gracz.pozycja = 470
                życia_obj = życia_font.render("Życia: {0}".format(gracz.życia),1,BIAŁY)
                if gracz.życia >= 0 :
                    lista_wszystkich_obiektów.add(gracz)
                    lista_graczy.add(gracz)
                #niszecenie pocisków wychodzących poza planszę
            if pocisk_wroga.rect.centery > 810:
                lista_pocisków_wroga.remove(pocisk_wroga)
                lista_wszystkich_obiektów.remove(pocisk_wroga)

        #ochrona po stracie życia      
        if gracz.wrażliwy == 0:
            gracz.sprawdź_czy_wrażliwy(1500)
  

        # sprawdzaznie czy pocisk trafił w cel
        for pocisk in lista_pocisków:
            lista_trafionych_wrogów = pygame.sprite.spritecollide(pocisk, lista_wrogów, True)
            for wróg in lista_trafionych_wrogów:
                dzwiek_wybuch_wroga.play()
                if wróg.drop_życie == 2:
                    życie = Życie(wróg.rect.centerx, wróg.rect.centery)
                    lista_wszystkich_obiektów.add(życie)
                    lista_żyć.add(życie)
                if wróg.drop_broń == 2:
                    broń = Broń(wróg.rect.centerx, wróg.rect.centery)
                    lista_wszystkich_obiektów.add(broń)
                    lista_broni.add(broń)
                lista_wszystkich_obiektów.remove(wróg)
                
                    
            # dla trafionych bloczków liczymy punkty
            for wróg in lista_trafionych_wrogów:
                lista_pocisków.remove(pocisk)
                lista_wszystkich_obiektów.remove(pocisk)
                punkty += 10
                punkty_obj = punkty_font.render("Wynik: {0}".format(punkty),1,BIAŁY)
                
            
 
            # niszecenie pocisków wychodzących poza planszę
            if pocisk.rect.centery < -10:
                lista_pocisków.remove(pocisk)
                lista_wszystkich_obiektów.remove(pocisk)

        for gr in lista_graczy:
            if pygame.sprite.spritecollide(gr, lista_żyć, True):
                dzwiek_zycie.play()
                gracz.życia +=1
                życia_obj = życia_font.render("Życia: {0}".format(gracz.życia),1,BIAŁY)
            if pygame.sprite.spritecollide(gr, lista_broni, True):
                dzwiek_grab.play()
                if gracz.rodzaj_broni < 3:
                    gracz.rodzaj_broni += 1
                else:
                    punkty += 100
                    punkty_obj = punkty_font.render("wynik: {0}".format(punkty),1,BIAŁY)
                życia_obj = życia_font.render("życia: {0}".format(gracz.życia),1,BIAŁY)
        
            

        # rysowanie wszystkich obiektów
        lista_wszystkich_obiektów.draw(ekran)
        ekran.blit(punkty_obj, [10,10])
        ekran.blit(życia_obj, [10,50])
        ekran.blit(energia_obj, [10,90])
        # aktualizacja ekrany po narysowaniu
        pygame.display.flip()
    
        zegar.tick(60)

    if okno_otwarte == False:
        pygame.quit()

