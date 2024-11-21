# 🧠 Számítástechnikai Kvíz Alkalmazás

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Egyszerű konzolos kvíz alkalmazás Python nyelven, számítástechnikai témájú igaz/hamis kérdésekkel.

## ✨ Jellemzők

- 🎯 Igaz/Hamis kérdések
- 📊 Azonnali pontozás és visszajelzés
- 💾 Bővíthető kérdés adatbázis
- 🖥️ Számítástechnikai témájú kérdések
- 📝 Angol nyelvű felhasználói felület

## 🚀 Telepítés

```bash
git clone https://github.com/namezor90/Quiz_Game.git
cd tech-quiz-app
python main.py
```

## 💻 Használat

1. Futtasd a `main.py` fájlt
2. Válaszolj a kérdésekre `True` vagy `False` beírásával
3. Minden válasz után azonnali visszajelzést kapsz
4. A kvíz végén láthatod a végső pontszámodat

## 📁 Projekt Struktúra

```
tech-quiz-app/
├── main.py           # Fő program fájl
├── question_model.py # Kérdés osztály definíció
├── quiz_brain.py     # Kvíz logika
└── data.py          # Kérdések adatbázisa
```

## 🛠️ Fejlesztés

Új kérdések hozzáadása a `data.py` fájlban:

```python
{
    "type": "boolean",
    "difficulty": "easy",
    "category": "Számítástechnika",
    "question": "Kérdés szövege",
    "correct_answer": "True/False",
    "incorrect_answers": ["False/True"]
}
```

## 📝 Licensz

[MIT](LICENSE)

## 🤝 Közreműködés

1. Fork-old a projektet
2. Hozz létre egy új branch-et (`git checkout -b feature/awesome`)
3. Commit-old a változtatásokat (`git commit -m 'Add awesome feature'`)
4. Push-old a branch-et (`git push origin feature/awesome`)
5. Nyiss egy Pull Request-et

## 👥 Szerzők

- [@namezor90](https://github.com/namezor90)
