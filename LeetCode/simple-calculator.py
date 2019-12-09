class Solution:
    def eval(self, expression, index):
        # op variable as empty string to hold operation state
        op = '+'
        result = 0 
        while index < len(expression):
            char = expression[index]
            if char in ('+', '-'):
                op = char
            else:
                value = 0
                if char.isdigit():
                    value = int(char)
                elif char == '(':     
                    (value, index) = self.eval(expression, index+1)
                if op == '+':
                    result += value 
                if op == '-':
                    result -= value 
            index += 1 

        return(result, index) 


print(Solution().eval('(1 + (2 + (3 + (4 + 5))))',0))