# Úloha #1 - deadline 2018-05-02

Domáca úloha sa skladá z troch povinných častí (1. - 3.) a zo 4. nepovinnej (náročnej) časti. Odhadovaný čas na vyriešenie povinnej časti je *2-4 hodiny*. Ak vám riešenie zaberá výrazne viac času a daný priestor nemáte, pripravte si nedokončené úlohy spolu s otázkami na call k domácej úlohe v pondelok _30. apríla 2018 o 18:00_.

V prípade, že si nepamätáte postup, ako _odklonovať repozitár_, spraviť _commit_, _push_ či _pull request_, môžete si ho osviežiť z videa z prvej prednášky "Úvod do programátorských nástrojov" - po 4min18s a po 13min50s, resp. z druhej prednášky "Úvod do softvérového cyklu" po 1h25min.

Tip: po odklonovaní projektu si overte, či skutočne využívate conda environment _pytalk_, tj. menu _File / Settings / search "project interpreter"_ overte si, že tam v roletke svieti zvolený _Python 3.6 (pytalk)_ a nie napr. venv). Ak máte Mac, tak namiesto vo _File_ hľadajte v _PyCharm / Settings_.

## 1. časť - titulok okna
* Spustite v PyCharm projekt cez "Check out from version control" a vloženie linku z GitHub, menu *Run* / *Run...*, zvoľte súbor `pie-talk.py`. (Pri spustení sa môže stať, že si od vás bude pýtať výber Interpretera. Vyberte _Python 3.6 (pytalk)_.) Po spustení by sa Vám malo zobraziť okno aplikácie s titulkom *PieTalk!*, podobné tomu, ktoré ste videli na prezentácii na workshope. Ak sa zobrazilo, úspešne ste kód spustili.

* V editore otvorte súbor `pie-talk.py`, vyhľadajte riadok kódu, v ktorom je nastavený titulok okna, a zmeňte titulok okna z _PieTalk!_ na _PieTalk 3000!_ . Spustite aplikáciu a overte si, že sa titulok okna skutočne zmenil. Ak vidíte okno s titulkom _PieTalk 3000!_ úspešne ste absolvovali tento bod. *Hurá!*

## 2. časť - forcyklus
* V súbore `pie-talk.py` vyhľadajte časť kódu, kde sa pravý panel (side panel, `LBUsers`) vo "forcykle" napĺňa položkami zo zoznamu (`#kanal`, `@user`). Upravte kód tak, aby sa bočný panel napĺňal výstupom z funkcie `chat.get_rooms()`. 

Po spustení opraveného kódu by ste mali v bočnom paneli vidieť namiesto `#kanal` a `@user` nový kanál (začína `#`) a nových používateľov (začínajúce `@`). 

Tip: Ak si chcete pripomenúť čo znamená "forcyklus", môžete si pozrieť lekciu https://www.py4e.com/lessons/loops.

## 3. časť - vypíš dátum
* V súbore `pie-talk.py` nájdite procedúru s názvom `window_print_line` slúžiacu na vypisovanie parametra `txt` ako riadku textu do okna chatovacej aplikácie. Upravte ju tak, aby pri každom volaní tejto funkcie nevypísala len obsah parametra `txt`, ale napísala pred ním aktuálny dátum a čas - tzn. vo výsledku po zavolaní procedúry `window_print_line('ahoj')` _24. aprila 2018_ v case _15:20_ vypíše stará verzia riadok `ahoj`, nová verzia vypíše `[2018-04-24][15:20] ahoj`. V tejto úlohe budete musieť vyhľadať korešpondujúce funkcie v online dokumentácii: https://www.python.org/doc/.

## 4. časť - Escape
* Aktuálne sa dá aplikácia zavrieť 2 spôsobmi. Zavretím okna alebo napísania príkazu `bye` a stlačenia klávesy `Enter`. Cieľom tejto úlohy je upraviť `pie-talk.py` tak, aby aplikácia skončila aj po stlačení klávesy `Esc`. Tip: Pri hľadaní riešenia môžete využiť kľúčové slová `TkInter`, `bind` a `Escape`.
