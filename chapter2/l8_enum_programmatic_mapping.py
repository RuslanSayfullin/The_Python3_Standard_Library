import enum
BugStatus = enum.Enum(
    value='BugStatus',
    names=[


    ],
)
print('All members:')
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))