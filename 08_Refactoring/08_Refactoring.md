# Refactoring Aufgaben
## 1) Zwei Refactorings
Aufgrund seiner Simplizität und gleichzeitig deutlichem Beitrag zum lesbaren, übersichtlichen Code finde ich das "Inline Methode" eine elegante Lösung, die man sich einprägen muss,
um Spaghetti-Code zu vermeiden. Ähnlicherweise hilft das "decompose conditional" Refactoring, einen knappen und knackigen Code zu haben.

## 2) IDE
Eclipse hat mehrere Refactoring-Musters, die sogar mit einem Hot-Key aktiviert werden können:
<img width="640" height="366" alt="grafik" src="https://github.com/user-attachments/assets/09f90359-2fa8-482f-b67d-84504d02864b" />


## 3) Refactoring Beispiel
Mein Beispiel stammt aus einem vorherigen Seminar. Es handelt sich um einen Brute-Force-Angriff auf AES. 
<img width="1016" height="411" alt="grafik" src="https://github.com/user-attachments/assets/e09b31ae-654d-4b86-ab83-5938a1ad29e7" />

Mit der Extract Method kriegt man:
<img width="792" height="185" alt="grafik" src="https://github.com/user-attachments/assets/2143858e-17de-412d-bd41-ce1a40215e11" />

Das Return-Werte funktionieren nicht, daher muss man manuell das Code anpassen:

<img width="724" height="182" alt="grafik" src="https://github.com/user-attachments/assets/ccd64d14-0726-4697-bf6d-eab9c0be3be3" />

und es funktioniert. Im Terminal sieht man zuerst den von der Refactored-Methode gefundenen Key in (int) und danach kommt das Ergebnis der originallen Methode

<img width="947" height="179" alt="grafik" src="https://github.com/user-attachments/assets/11defae1-411f-4762-a33c-9638e9c62aed" />

## 4) Refactoring with AI

Hier habe ich Lumo benutzt und habe ich ein paar Prompt eingegeben, um einen Kontext aufzubauen:
"Can you do code refactoring in python?"
"Here is my code. It is a Brute force attack to AES with a small key:"

Zuerst hat die AI versucht alle zu optimieren, obwohl das Code funktioniert. Ich musste noch ein prompt eingeben, damit nicht die unterliegende Logik untersucht wurde:
"Forget the last: Just undertand this attack to an AES and refactor the code. The code is working and now functional it must onyl be refactored: from Crypto.Cipher import AES"

Das Ergebnis ist ein übersichtlicherer Code, 

<img width="608" height="152" alt="grafik" src="https://github.com/user-attachments/assets/5fcf2ab8-44a6-431e-b0df-d9d9b83f589d" />

aber es wurde keine Methode extrahiert:

<img width="638" height="238" alt="grafik" src="https://github.com/user-attachments/assets/2b9fb859-aa7a-44d8-af4b-179a138970b5" />

Nach noch einem Prompt gibt es eine vernünftigere Ausgabe mit mehr Methoden:

<img width="848" height="325" alt="grafik" src="https://github.com/user-attachments/assets/07fee01f-1ce3-48f1-b08b-fc345278023d" />
<img width="810" height="341" alt="grafik" src="https://github.com/user-attachments/assets/c51c7bf5-a870-4a80-b04a-84295bcd9b43" />
<img width="860" height="387" alt="grafik" src="https://github.com/user-attachments/assets/0c1bec2f-66d4-4956-9085-0fc3908340df" />

Und es hat doch funktioniert:
<img width="915" height="267" alt="grafik" src="https://github.com/user-attachments/assets/5220d1c2-5199-489f-869c-3c7a5d3f69b6" />

Dieses Darstelung und Strukturierung ist besser, aber man muss auch erwähnen, dass in diesem Fall die Aufgabe einfach war. Daher scheinen alle diese Methode wie eine Vermehrung, die das Code verkomplizieren. Kurz gesagt, ein Over-kill.








