import random

class Arithmetic(object):
    def __init__(self, min_num= 0 , max_num = 10):
        self.max_num = max_num
        self.min_num = min_num
        self.operation = None
        self.num_one = None
        self.num_tow = None
        self.QUESTION = " What is {} {} {}?"

    def prep_rand_num(self):
        self.num_one = random.randint(self.min_num, self.max_num)
        self.num_tow = random.randint(self.min_num, self.max_num)

    def get_addition_question(self):
        self.prep_rand_num()
        self.operation = "+"
        return self.QUESTION.format(self.num_one, self.operation, self.num_tow)

    def get_subtraction_question(self):
        self.prep_rand_num()
        self.operation = "-"
        while self.num_one < self.num_tow:
            self.prep_rand_num()

        return self.QUESTION.format(self.num_one, self.operation, self.num_tow)

    def get_multipication_question(self):
        self.prep_rand_num()
        self.operation = "x"

        return self.QUESTION.format(self.num_one, self.operation, self.num_tow)

    def get_division_question(self):
        self.prep_rand_num()
        self.operation = "%"

        while self.num_tow == 0 or self.num_one % self.num_tow !=0:
            self.prep_rand_num()

        return self.QUESTION.format(self.num_one, self.operation, self.num_tow)

    def get_next_question(self, rand= False):

        if rand:
            _list = "+ - x %".split()
            self.operation = _list[random.randint(0, len(_list) - 1)]
        _dict={
            "+": self.get_addition_question,
            "-": self.get_subtraction_question,
            "x": self.get_multipication_question,
            "%": self.get_division_question
        }
        return _dict[self.operation]()

    def get_answer(self):
        if self.operation == "+":
            return self.num_one + self.num_tow
        elif self.operation == "-":
            return self.num_one - self.num_tow
        elif self.operation == "x":
            return self.num_one * self.num_tow
        else:
            return self.num_one / self.num_tow
