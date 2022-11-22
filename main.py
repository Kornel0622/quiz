class QA:
  def __init__(self, question, correctAnswer, otherAnswers):
    self.question = question
    self.corrAnsw = correctAnswer
    self.otherAnsw = otherAnswers

kerdesek = [QA("Hány éves Orbán Viktor?", "59", ["70", "49", "60"]),
QA("Kicsoda Orbán Viktor meleg szeretője?", "Gyurcsány Ferenc", ["Soros György", "Mészáros Lőrinc", "Németh Szilárd"]),
QA("Mennyi ideje van hatalmon Orbán Viktor?", "Több ideje, mint kellett volna", ["12 év", "8 év", "20 év"]),
QA("Milyen betegségben szenved Orbán Viktor?", "Elhízás", ["Rák", "Éc", "Down-szindróma"]),
QA("Ki/Kik Orbán Viktor legnagyobb ellensége(i)?", "Gyurcsány", ["Transznemű óvodások", "Brüsszel", "Soros", ]),
QA("Melyik állat hasonlít a legjobban Orbán Viktorra?", "Disznó", ["Bika", "Oroszlán", "Medve",])]