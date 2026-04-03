import sys
import os
from lark import Lark, Transformer, v_args

# Define the Helium Interpreter
class HeliumInterpreter:
    def __init__(self, grammar_path):
        with open(grammar_path, 'r') as f:
            self.parser = Lark(f.read(), start='program', parser='lalr')
        
        self.globals = {
            'print': print,
            'len': len,
        }
        self.scopes = [self.globals]

    def get_var(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise NameError(f"Variable '{name}' not found")

    def set_var(self, name, value):
        self.scopes[-1][name] = value

    def run(self, code):
        tree = self.parser.parse(code)
        return self.execute(tree)

    def execute(self, node):
        if hasattr(node, 'data'):
            method_name = f'exec_{node.data}'
            if hasattr(self, method_name):
                return getattr(self, method_name)(node)
            else:
                # Default behavior for non-explicit methods (like program)
                result = None
                for child in node.children:
                    result = self.execute(child)
                return result
        return node

    def exec_assignment_stmt(self, node):
        name = str(node.children[0])
        if name.startswith('"') or name.startswith("'"):
            name = name[1:-1]
        value = self.evaluate(node.children[1])
        self.set_var(name, value)

    def exec_expr_stmt(self, node):
        return self.evaluate(node.children[0])

    def exec_func_def(self, node):
        name = str(node.children[0])
        params = [str(p) for p in node.children[1].children] if node.children[1] else []
        body = node.children[2]
        
        def helium_func(*args):
            new_scope = dict(zip(params, args))
            self.scopes.append(new_scope)
            try:
                result = self.execute(body)
            except ReturnException as e:
                result = e.value
            finally:
                self.scopes.pop()
            return result
            
        self.set_var(name, helium_func)

    def exec_if_stmt(self, node):
        condition = self.evaluate(node.children[0])
        if condition:
            return self.execute(node.children[1])
        elif len(node.children) > 2:
            return self.execute(node.children[2])

    def exec_return_stmt(self, node):
        value = self.evaluate(node.children[0])
        raise ReturnException(value)

    def evaluate(self, node):
        if not hasattr(node, 'data'):
            return node
            
        if node.data == 'number':
            return float(node.children[0])
        elif node.data == 'string':
            return str(node.children[0])[1:-1] # Remove quotes
        elif node.data == 'true': return True
        elif node.data == 'false': return False
        elif node.data == 'null': return None
        
        elif node.data == 'var':
            return self.get_var(str(node.children[0]))
            
        elif node.data == 'object':
            obj = {}
            for child in node.children:
                key = str(child.children[0])
                if key.startswith('"') or key.startswith("'"):
                    key = key[1:-1]
                val = self.evaluate(child.children[1])
                obj[key] = val
            return HeliumObject(obj)
            
        elif node.data == 'list':
            return [self.evaluate(c) for c in node.children]
            
        elif node.data == 'func_call':
            func = self.evaluate(node.children[0])
            args = [self.evaluate(a) for a in node.children[1].children] if node.children[1] else []
            return func(*args)
            
        elif node.data == 'sum':
            left = self.evaluate(node.children[0])
            op = str(node.children[1])
            right = self.evaluate(node.children[2])
            if op == '+':
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                return left + right
            return left - right
            
        elif node.data == 'product':
            left = self.evaluate(node.children[0])
            op = str(node.children[1])
            right = self.evaluate(node.children[2])
            return left * right if op == '*' else left / right

        elif node.data == 'comparison':
            left = self.evaluate(node.children[0])
            op = str(node.children[1])
            right = self.evaluate(node.children[2])
            if op == '==': return left == right
            if op == '!=': return left != right
            if op == '<': return left < right
            if op == '>': return left > right
            if op == '<=': return left <= right
            if op == '>=': return left >= right

        elif node.data == 'attr_access':
            obj = self.evaluate(node.children[0])
            attr = str(node.children[1])
            if isinstance(obj, HeliumObject):
                return obj.data.get(attr)
            return getattr(obj, attr)

        return node

class HeliumObject:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return str(self.data)
    def __str__(self):
        return str(self.data)

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 helium_interpreter.py <file.ium>")
    else:
        grammar_file = os.path.join(os.path.dirname(__file__), 'grammar.lark')
        interpreter = HeliumInterpreter(grammar_file)
        with open(sys.argv[1], 'r') as f:
            interpreter.run(f.read())
