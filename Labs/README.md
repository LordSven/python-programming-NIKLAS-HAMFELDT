## 🧠 Beskrivning
Mitt program utför linjär klassificering av en uppsättning data från en given fil (`unlabelled_data.csv`) samt eventuella egna punkter som användaren kan mata in. Punkterna klassificeras baserat på den data som lästs in.

Jag har valt att visa två exempel:

1. **Uppskattad linje:** Jag uppskattade var medelpunkten för varje kluster låg och drog en linje mellan dessa punkter som en första uppdelning.  
2. **Uträknad linje:** Därefter räknade jag ut en ny, mer träffsäker linje baserat på de faktiska medelvärdena (genomsnittspunkterna) för kluster 0 och kluster 1.

---

## ⚙️ Hur man använder programmet
1. Kör Python-filen (`.py`-filen).  
2. Välj om du vill mata in egna koordinater eller om du vill låta programmet slumpa fram en punkt ur den givna datan.  
3. Programmet visar två grafer:  
   - En med den **uppskattade delande linjen**.  
   - En med den **uträknade (korrekta) delande linjen**.  
4. Du får även textutskrift som visar om den valda punkten ligger **över** eller **under** linjen, vilket också kan ses i graferna.

---

## 📊 Övrigt
Anledningen till att båda graferna visas är att i min uppskattade linje hamnade alla punkter vars summa blev 0 precis på linjen, vilket gjorde att de inte kunde klassificeras.  
Innan jag räknade ut den mer exakta linjen hade jag därför också lagt till kod som kunde:
- Ge svaret att punkten ligger *på* linjen, och  
- Räkna antalet eventuella felklassificeringar.

---

## 📁 Utdata
Programmet genererar även en fil `labelled_data.csv` där varje punkt har fått en etikett (`0` eller `1`) beroende på vilken sida av linjen den ligger.

---
