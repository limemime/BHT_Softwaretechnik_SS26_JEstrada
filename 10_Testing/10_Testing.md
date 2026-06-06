# A1 Unit Tests

Für diese Aufgabe und die Aufgabe 3 habe ich mich entschieden, das Projekt von der Vibe-Coding-ESA/Präsenz zu benutzen.
In diesem Projekt habe ich einen Programm "gevibet", das randomisierte Suchen in Google macht, um jegliche Profiling zu erschweren.
Die Hauptfunktionen sind eine Engine, das ein Wörterbuch auflädt und die Suchen in eine einstellbare Zeitspanne ausführt.
Die vond er KI konzipierten testen haben sich auf Assertions konzentriert, aber die Schlusselfunktionen wurden mit Mock-Objekten getestet.

## Die KI hat trotz meines Tippfehlers, das Prompt verstanden. I habe mich nur auf einen Funktion konzentriert:

<img width="370" height="127" alt="grafik" src="https://github.com/user-attachments/assets/3e97b689-509c-4ef6-ade1-1a59a68eaea4" />

## Zuerst kann man sehen, dass die KI Assertions für alle variabeln hizugefügt hat:

<img width="1819" height="840" alt="grafik" src="https://github.com/user-attachments/assets/aa3653a1-9144-4f2d-8f84-3ab254f88883" />

## Es gibt Assertions für die Zeitspanne und den Deteipfad: 

<img width="975" height="169" alt="grafik" src="https://github.com/user-attachments/assets/bf3aad54-9bf9-4836-85f0-2185d0ad1822" />

## Die KI hat für das Testen von die geladenen Wörter eine Liste und ein Mock-load gemacht:

<img width="1365" height="147" alt="grafik" src="https://github.com/user-attachments/assets/45fb39b1-c232-42d6-996a-86f653c5cef5" />

## Für die Funktion, die das Wörterbuch lädt, gibt es auch ein mock file:

<img width="1107" height="214" alt="grafik" src="https://github.com/user-attachments/assets/fb9094f1-efc4-4499-8d64-e1d5cea1432f" />

## Nach dem Ausführung bekommt man eine Zusammenfassung: 

<img width="1227" height="607" alt="grafik" src="https://github.com/user-attachments/assets/cb136687-210e-43e6-b9a9-4ed035944255" />

## Wie in Punkt 4 hingedeutet wurded im Testing eine Ausnahme eingebaut:

<img width="1027" height="333" alt="grafik" src="https://github.com/user-attachments/assets/79cc6310-a9b3-4bc8-8a1e-fea39d81f20f" />


## Diese Testen mit KI unterstützung ist enfiach,
aber mir es kann gut sein, dass die KI nicht sofort an die Grenzfälle oder auf abwegige Fälle kommt.
Ich habe noch ein prompt eingegeben, um diese Vermutung zu testen.

<img width="553" height="91" alt="grafik" src="https://github.com/user-attachments/assets/863867dc-5ed9-4475-80dd-2a04f5e91030" />

## Die KI hat testen für negative und invertierten Werte sowie Out-of-bounds: 

<img width="1090" height="721" alt="grafik" src="https://github.com/user-attachments/assets/50fe52b3-0ebd-4a69-be8b-090a2422a67b" />

## Manche Tests sind gescheitert:

<img width="1410" height="352" alt="grafik" src="https://github.com/user-attachments/assets/54a8b92b-3475-4b8d-a72e-86019df941bd" />

## Aber die Ki hat sie sofort repariert und verbessert.
Die Date von der test und Programm sind im Unterordner hinzugefügt. 

# A2 TDD

## Ich habe in Gemini den ganezn Kontext und Aufgaben von Anfang an erklärt:

<img width="1123" height="766" alt="grafik" src="https://github.com/user-attachments/assets/ea0e6656-2a8c-4bc8-b167-cbff346bcf35" />

## Erste Rot:

<img width="1101" height="715" alt="grafik" src="https://github.com/user-attachments/assets/f8ef6318-286a-462a-81ed-5661c039ae1d" />

## Erste Grün:

<img width="1123" height="262" alt="grafik" src="https://github.com/user-attachments/assets/bd0446f8-6348-4e43-a2b3-b1f8d5976e7a" />

## 2. Rot

<img width="1084" height="823" alt="grafik" src="https://github.com/user-attachments/assets/82b6ecf1-b6e1-4b86-95a7-15525556e04c" />

## 2. Grün

<img width="1105" height="735" alt="grafik" src="https://github.com/user-attachments/assets/63154250-197f-479a-ab9c-b250e0e01cac" />

## 3. Rot
Diese war auch erfolgreich, da die FUnktion ist ganz trivial. Es geht nur um addieren.

<img width="1111" height="636" alt="grafik" src="https://github.com/user-attachments/assets/61136393-3df7-45f3-86b8-fbd5b43b69f6" />

## 3.' Rot

Daher habe ich einen neue promtp gegeben, um zu sagen, dass es geht um eine test, in dem mehere item gleichzeitig eingegeben werden.

<img width="1113" height="723" alt="grafik" src="https://github.com/user-attachments/assets/3f6e025f-c86d-4b05-a3a1-da75bb1c6469" />

## 3. Grün
<img width="1114" height="697" alt="grafik" src="https://github.com/user-attachments/assets/6151af93-eadf-43d4-a622-3b53c93ff9a2" />

## 4. Rot

<img width="1114" height="820" alt="grafik" src="https://github.com/user-attachments/assets/c01af97b-3ef1-49cf-906b-a20c119070bc" />

## 4. Grün

<img width="1087" height="706" alt="grafik" src="https://github.com/user-attachments/assets/4f569c0a-9325-4181-a6ef-343f2858f4e7" />













# A3 Mutation Testing (Zwei Teilen)
Ich habe Antigravity weiter benutzt, um MutPy in the .venv zu installieren 

## Mit MutPy gab es 11 überlebende Mutanten ohne kills:

Hier muss man erwähnen, dass die Überlebende zu dem Code gehören, die nicht mut testen versehen war. 

<img width="619" height="663" alt="grafik" src="https://github.com/user-attachments/assets/140a28a5-457c-4a2f-a76b-5233475b2450" />

## Die erste Vier überlebende:

<img width="1795" height="361" alt="grafik" src="https://github.com/user-attachments/assets/2c69fc4a-c004-4b9f-aa4a-d78ab564778f" />

## 1 und 2 Assignment Operator replacement

Hier wurde den Werten mit "-" oder null mutiert:

<img width="1512" height="126" alt="grafik" src="https://github.com/user-attachments/assets/fd44696c-712f-43df-9b26-073fc27d5999" />

<img width="1624" height="183" alt="grafik" src="https://github.com/user-attachments/assets/06136716-ba22-44b1-8590-a56a78709551" />

## 9 und 10 gehären aber zum Code mit Testen
Hier handelt es sich um "incompetent" Mutante, also Mutaten, die die funktionalität des Programms nicht änderten. Aber hier hendelt sich eher um eine schwieriger Fall, denn Antigravity zufolge wurden diese als incompentet bezeichnet, weil bei dem exception handling, die hier doch getestet wurde, MutPy gecrasht hat. 

<img width="1674" height="250" alt="grafik" src="https://github.com/user-attachments/assets/b2e68b9c-2f1b-4303-b2df-2bc9091991ba" />

Aber nach weitere Fragen und Versuchen, kann es sein, dass es sich um eine Kompatibilität Problem mit der Ausnahmen handelt:

<img width="829" height="327" alt="grafik" src="https://github.com/user-attachments/assets/63de3811-4bfa-45d3-9224-a2c523cd5d50" />

## Für diese spezifische Mutant wäre weitere Debbuging und testen notwendig....






# A3 MUtation Testing nur mit AI

Ich habe diese Aufgabe so zuerst gemacht, wiel ich die Frameworks vergessen habe. Dabei habe ich aber was über die KI gelernt.

## Da der Kontext schon da ist, konnte der Prompt kurz sein:

<img width="576" height="90" alt="grafik" src="https://github.com/user-attachments/assets/a3fd1eab-8aa4-48fa-b45c-abd22fa929ff" />

## Das Code ist nach Kurzem da

<img width="1348" height="835" alt="grafik" src="https://github.com/user-attachments/assets/23213e6f-518b-4bc8-ba5b-a587eff3945e" />

## Zuerst wird die Baseline überprüft und dann kommen die Mutanten:

<img width="1236" height="681" alt="grafik" src="https://github.com/user-attachments/assets/a9086281-c196-4ce0-92be-a739fd463cd9" />

## Die Mutaten wurden besiegt (Darwin und die Evolution trauern...)

<img width="1162" height="445" alt="grafik" src="https://github.com/user-attachments/assets/0db972ae-6a2e-4f92-92a0-5f8ba5d2b36e" />
<img width="1297" height="453" alt="grafik" src="https://github.com/user-attachments/assets/a48f68ca-a122-4e6c-b8e9-e1e4478a01b9" />

## Da alle überlebt haben, musste ich noch einen Prompt eingeben:

<img width="676" height="76" alt="grafik" src="https://github.com/user-attachments/assets/c7c53b0f-43db-4500-9108-c3a3c24df883" />

## Die neue Mutanten habenn alle Überlebt:

Diese Ergebnisse zeigen deutlich auf, dass die KI beim Testen nicht um die Ecken denken kann. Sie hat die ersten Mutaten in Bezug auf die vorherigen Assertions gebaut.
Die zweite Mutantengruppe orientierte sich "gezielt" auf den ungetesteten Teil der Klasse, daher könnten Sie alle überleben.

<img width="1437" height="538" alt="grafik" src="https://github.com/user-attachments/assets/8a65262f-d28b-4091-b7bf-7a63817bf433" />










