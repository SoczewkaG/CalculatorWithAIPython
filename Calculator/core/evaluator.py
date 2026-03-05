from operations import *



class Evaluator:
    def __init__(self):
        self.operations = {
            "add": add,
            "substract": substract,
            "multiply": multiply,
            "divide": divide,
            "power": power,
            "sqrt": sqrt,
            "absolute": absolute,
            "negate": negate,
            "modulo": modulo,
            "percentage": percentage,
            "factorial": factorial,
            "reciprocal": reciprocal,
            "square": square,
            "cube": cube,
        }
    
    def evaluate(self, a, operator, b=None):
        """Function takes A and B and then defines which 
        operation to perform and returns it as the result """

        operation = self.operations.get(operator)

        if operation is None:
            raise ValueError("Invalid operator")
        if b is None:
            "if B is not given"
            return operation(a)
        else: 
            return operation(a, b)
        

