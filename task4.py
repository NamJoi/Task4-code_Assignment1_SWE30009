import operator
class Solution(object):
    def __init__(self):
        self.signs = ["+", "-","*", "/"]
        self.operator = {
            "+" : operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        self.value = {}
    def correct_program(self , a, b, sign1, sign2 ):
        operator1 = self.operator.get(sign1)
        operator2 = self.operator.get(sign2)
        c = operator1(a,b)
        return operator2(c , 2 )
    

    def incorrect_program(self , a, b):
        correct_answer = self.correct_program(a, b, "-", "*" )
        for sign in self.signs : 
            for sign1 in self.signs:
                if sign == "-"  and sign1 == "*" : 
                    continue 
                incorrect_answer = self.correct_program(a, b, sign, sign1)

                if incorrect_answer == correct_answer : 
                    self.value[f"Value of A: {a} - Sign: ('{sign}' , '{sign1}')"] = f"Incorrect case result: {incorrect_answer} - Correct case result: {correct_answer}"
        return self.value
    
solution = Solution() 
b = 1 
for a in range(-100 , 100):
    value = solution.incorrect_program(a , b)


for key, val in value.items():
    print(f"{key}: {val}\n")