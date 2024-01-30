import codewars_test as test


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_operator(c):
    return c in ['+', '-', '*', '/']


def is_unary_minus(tokens, index):
    if tokens[index] != '-':
        return False
    if index == 0:
        return True
    if tokens[index - 1] in ['+', '-', '*', '/', '(']:
        return True
    return False


def precedence(op, is_unary):
    if op == '-' and is_unary:
        return 3  # Unary minus has higher precedence
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    return 0


def tokenize(expression):
    tokens = []
    number = ''
    for char in expression:
        if char.isdigit() or (char == '-' and (not number and (not tokens or tokens[-1] in ['+', '-', '*', '/', '(']))):
            number += char
        else:
            if number:
                tokens.append(number)
                number = ''
            if char in ['+', '-', '*', '/', '(']:
                tokens.append(char)
    if number:
        tokens.append(number)
    return tokens


def infix_to_postfix(tokens):
    stack = []
    postfix = []
    for i, token in enumerate(tokens):
        if token.lstrip('-').isnumeric():
            postfix.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        elif is_operator(token):
            while stack and precedence(stack[-1], is_unary_minus(stack, len(stack) - 1)) >= precedence(token, is_unary_minus(tokens, i)):
                postfix.append(stack.pop())
            stack.append(token)

    while stack:
        postfix.append(stack.pop())
    return postfix


def build_expression_tree(postfix):
    stack = []
    for token in postfix:
        if token.lstrip('-').isnumeric() or (token == '-' and len(token) > 1):  # Negative number
            stack.append(TreeNode(token))
        elif is_operator(token):
            node = TreeNode(token)
            node.right = stack.pop()
            # Check if it's unary minus
            if not is_unary_minus(postfix, len(postfix) - len(stack) - 1):
                node.left = stack.pop()
            stack.append(node)
    return stack.pop()


def evaluate_tree(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return int(node.value)

    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)

    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        if node.left is None:  # Unary minus
            return -right_val
        else:
            return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.left, level + 1)


def calc(expression):
    expression = expression.replace(" ", "")
    print(expression)
    tokens = tokenize(expression)
    postfix = infix_to_postfix(tokens)
    tree = build_expression_tree(postfix)
    # print_tree(tree)
    result = evaluate_tree(tree)
    print(result)

    return result
# result = evaluate_tree(tree)



'''
https://www.codewars.com/kata/52a78825cdfc2cfc87000005/train/python

'''

@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        cases = (
            ("1 + 1", 2),
            ("8/16", 0.5),
            ("3 -(-1)", 4),
            ("2 + -2", 0),
            ("10-2--5", 13),
            ("(((10)))", 10),
            ("3 * 5", 15),
            ("-7 * -(6 / 3)", 14)
        )

        for x, y in cases:
            test.assert_equals(calc(x), y)
