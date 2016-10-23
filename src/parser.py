import sys;
from tokenizer import Tokenizer;

class ArithmeticParser:
    def __init__(self):
        pass;
    
    def parse(self,exp):
        self.tokenizer = Tokenizer(exp);
        return self._parse_expression();

    def _parse_expression(self):
        return self._parse_additive_expression();

    def _parse_additive_expression(self):
        operand1 = self._parse_multiplicative_expresssion();
        while self.tokenizer.peek_next_token() in ('+','-'):
            operator = self.tokenizer.get_next_token();
            operand2 = self._parse_multiplicative_expresssion();
            operand1 = self._apply_operator(operand1,operand2,operator);
        return operand1;

    def _parse_multiplicative_expresssion(self):
        operand1 = self._parse_primary();
        while self.tokenizer.peek_next_token() in ('*','/'):
            operator = self.tokenizer.get_next_token();
            operand2 = self._parse_primary();
            operand1 = self._apply_operator(operand1,operand2,operator);
        return operand1;

    def _parse_primary(self):
        operand = self.tokenizer.get_next_token();
        if (operand == '('):
            operand = self._parse_expression();
            self.tokenizer.get_next_token();
        return operand;

    def _apply_operator(self,operand1,operand2,operator):
        if operator == '+':
            return int(operand1) + int(operand2);
        elif operator == '-':
            return int(operand1) - int(operand2);
        elif operator == '*':
            return int(operand1) * int(operand2);
        else:
            return int(operand1) / int (operand2);

if __name__ == "__main__":
    parser = ArithmeticParser();
    if (len(sys.argv) < 2):
        print("Please provide arithmetic expression enclosed in parentheses");
    else:
        result = parser.parse(sys.argv[1]);
        print(result);

