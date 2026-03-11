
class Controller:

    def __init__(self, evaluator):
        self.evaluator = evaluator

    def calculate(self, expression):
        expression = eval(expression)
        #if len(expression) == 2:
        #    a = expression[0]
         #   operator = expression[1]
        #    return self.evaluator.evaluate(a, operator)
        
        #a = expression[0]
        #operator = expression[1]
        #b = expression[2]
        
        return expression
        #return self.evaluator.evaluate(a, operator, b)
        
        
