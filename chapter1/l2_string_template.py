import string

values = {'var': 'foo'}

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")

print('Template:', t.substitute(values))

s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %{var}iable
"""

print('NTERPOLATION:', s % values)

s = """
Variable        : (var)
Escape          : {{}}
Variable in text: {var}iable
"""

print('FORMAT:', s.format(**values))

