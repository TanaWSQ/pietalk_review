# Úloha #2 - deadline 2018-05-09


Domáca úloha sa skladá z troch povinných častí (1. - 3.) a zo 4. nepovinnej (náročnej) časti. Odhadovaný čas na vyriešenie povinnej časti je *2-4 hodiny*. Ak vám riešenie zaberá výrazne viac času a daný priestor nemáte, pripravte si nedokončené úlohy spolu s otázkami na call k domácej úlohe v pondelok _7. mája 2018 o 18:00_. Ak vám niečo v úlohe bráni/zasekli ste sa, nehanbite sa to komunikovať.

Tip: V prípade, že si nepamätáte postup, ako _odklonovať repozitár_, spraviť _commit_, _push_ či _pull request_, môžete si ho osviežiť z videa z prvej prednášky "Úvod do programátorských nástrojov" - po 4min18s a po 13min50s, resp. z druhej prednášky "Úvod do softvérového cyklu" po 1h25min.

## 1. časť - implementovať funkciu info() vypisujúcu farebný text
V súbore `Classes/AppMessage.py` a `Classes/AppMessageConsole.py` je _implementovaná_ (naprogramovaná) funkcionalita vypisovania hlášok/správ aplikácie (do konzoly).

Trieda *AppMessage* je v danú chvíľu "aliasom", tzn. v podstate všetku funkcionalitu *AppMessage* reálne implementujete v triede *AppMessageConsole*. 

Vašou úlohou je pridať implementáciu metód `info(self, text)` do súboru `AppMessage.py` a `info(text)` do súboru `AppMessageConsole.py`, ktoré budú do konzoly vypisovať text zelenou farbou.

_Overenie funkčnosti_: V súbore `Classes/Config.py` v konštruktore (metóda `__init__`) využívame funkcie triedy `AppMessage` na vypisovanie stavu nastavenia funkcie `autosave`. Pridajte na záver konštruktora volanie práve naimplementovanej funkcie `info` triedy `AppMessage` (analogicky k použitej `msg` resp. `warn`), ktorá vypíše text "config load - done\n".

## 2. časť - implementácia ukladania nastavení pomocou key/value storage
V súbore `Classes/Config.py` nájdete triedu `Config`, ktorá má slúžiť na ukladanie nastavení aplikácie. V triede `Config` sa aktuálne nachádzajú 2 metódy
* mock (neúplnú implementáciu, fungujúcu len na vybranom vstupe) metódy `getKey(self, keyName)` - funkcie slúžiacej na načítanie hodnoty uloženej pod názvom `keyName`
* neimplementovanú metódu `setKey(self, keyName, value)`, ktorá má slúžiť na zapísanie hodnoty identifikovanej kľúčom `keyValue`
(vidíte tam 2 rôzne prístupy k tomu, ako mať v programe nenaimplementovanú funkcionalitu). Cieľom dvojice `getKey` a `setKey` je poskytovať aplikácií tzv. *key/value storage*.

Vašou úlohou bude implementovať metódy `getKey` a `setKey` pomocou `hashmap`y (asociatívneho poľa, vysvetlované na záver workshopu). Vo výsledku si môžete napr. uložiť čas naposledy napísanej správy ako kľúč "*message.time_last*", tzn. zapisovať obsah premennej `aktualny_cas` pomocou volania `setKey('message.time_last', aktualny_cas)` resp. prečítať pomocou `getKey('message.time_last')`. Ak hodnota pre daný kľúč v hashmape neexistuje, `getKey` má vrátiť textový reťazec `undefined`.

_Overenie funkčnosti_: V `pie-talk.py` sa nachádza použitie metódy `getKey`, konkrétne `print(chat.config.getKey('testkey'))`. Na tomto mieste môžete overiť funkčnosť nastavením `setKey('user.nick', 'rusnovodic47')` a následným vypísaním obsahu po zavolaní `getKey('user.nick')`.

## 3. časť - prvé využitie key/value storage
V súbore `Classes/User.py` vyhľadajte časť kódu nájdete naimplementované metódy `get_nick`, `set_nick`, `get_status` a `set_status`, ktoré poskytujú manipulovať s triedou `User`, presnejšie možnosť prečítať/nastaviť jej `nick` a `status`. Aktuálne si trieda ukladá všetky vlastnosti "do seba" (`self.updated`, `self.nick`, `self.status`). Cieľom tejto časti úlohy je nahradiť vnútorné fungovanie objektu tak, aby si neukladal hodnoty do vnútorných premenných, ale využíval key/value storage z objektu config. Tzn. využíval metódy getKey a setKey, nick si uložil pod kľúčom _user.nick_, status pod _user.status_ a updated pod _user.updated_.

## 4. časť - parser príkazov
Nástroj resp. rutina na identifikáciu (vstupných) údajov (napr. textu), sa zvykne nazývať parser. V tejto časti úlohy bude Vašou úlohou upraviť existujúci parser `process_command_logic` v súbore `pie-talk.py`, ktorý slúži na identifikáciu príkazov z "limetkového príkazového riadku" tak, aby bol schopný identifikovať a vykonávať nové príkazy. Rozšírte ho teda nasledovne:
- schematicky: `/prikaz [parametre]`, tzn. príkaz
  - `/nick` - vypíše nick - (`User.get_nick`)
  - `/nick rusnovodic47` - nastaví nick na "rusnovodic47" (`User.set_nick`)
  - `/status` - vypíše aktuálny status (`User.get_status`)
  - `/status opat prichadza vlak... :/` - nastaví status na "opat prichadza vlak... :/" (`User.set_status`)
