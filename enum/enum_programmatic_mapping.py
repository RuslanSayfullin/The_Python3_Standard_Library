#!/usr/bin/env python3
# encoding: utf-8
"""С целью получения большего контроля над значениями, связанными с элемен­
тами, вместо строки с именами можно передавать двухкомпонентные кортежи
или словарь, отображающий имена на значения
"""

#end_pymotw_header
import enum


BugStatus = enum.Enum(
    value='BugStatus',
    names=[
        ('new', 7),
        ('incomplete', 6),
        ('invalid', 5),
        ('wont_fix', 4),
        ('in_progress', 3),
        ('fix_committed', 2),
        ('fix_released', 1),
    ],
)

print('All members:')
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))
