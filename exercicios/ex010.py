a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) # ocupa o mesmo espaço na mémoria ? false
print(a is not b) # não ocupa o mesmo espaço na mémoria ? true

curso = 'curso em python'
curso_python = curso

print(curso is curso_python) # ocupa o mesmo espaço na mémoria ? true
print(curso is not curso_python) # não ocupa o mesmo espaço na mémoria ? false