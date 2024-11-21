class QuizBrain:
    """
    A kvíz logikáját kezelő és a felhasználó előrehaladását követő osztály.

    Attribútumok:
        question_number (int): Aktuális kérdés sorszáma
        score (int): Felhasználó pontszáma
        question_list (list): Question objektumok listája
    """
    def __init__(self, q_list):
        """
        QuizBrain példány inicializálása.

        Args:
            q_list (list): Question objektumok listája
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        """
        Ellenőrzi, hogy van-e még megválaszolatlan kérdés.

        Returns:
            bool: True ha van még kérdés, False ha nincs
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Megjeleníti a következő kérdést és feldolgozza a választ.

        Bekéri a felhasználó válaszát és ellenőrzi azt a check_answer metódussal.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}. {current_question.text}. (True / False ): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, currect_answer):
        """
        Ellenőrzi, hogy a felhasználó válasza helyes-e.

        Args:
            user_answer (str): A felhasználó válasza
            currect_answer (str): A helyes válasz

        Visszajelzést ad és frissíti a pontszámot helyes válasz esetén.
        """
        if user_answer.lower() == currect_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Te correct answer was: {currect_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
