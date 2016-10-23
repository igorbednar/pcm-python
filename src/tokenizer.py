class Tokenizer:

    def __init__(self, exp):
        self.tokens = self._parse_exp(exp);
        self.index = 0;

    def _parse_exp(self,exp):
        list = [];
        for el in exp:
            if el.isspace():
                continue;
            list.append(el);
        return list;

    def get_next_token(self):
        if self.index < len(self.tokens):
            el = self.tokens[self.index];
            self.index = self.index + 1
            return el;
        return None;

    def peek_next_token(self):
        if self.index < len(self.tokens):
            return self.tokens[self.index];
        return None;