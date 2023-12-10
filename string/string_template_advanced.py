import string

class MyTemplate(string.Template):
    delimer = '%'
    idpattern = '[a-z]+_[a-z]+'

template_text = '''
    Delimer : %%
    Replaced: %with_underscore
    Ignored : %notunderscored
'''

d = {
    'with_underscore': 'replaced',
    'notunderscored' : 'not replaced',
}

t = MyTemplate(template_text)
print('Modified ID pattern:')
print(t.safe_substitute(d))
