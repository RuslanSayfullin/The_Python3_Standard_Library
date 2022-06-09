import gettext

gettext.install(
    'example',
    'locale',
    names=['ngettext'],
)

print(('This message is in the script.'))

