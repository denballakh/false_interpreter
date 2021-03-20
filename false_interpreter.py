from false_machine import FalseMachine

code = R"""[][^$1_=~][[,!]]#%!"""
code = R"""
[\$@$@\/*-0={divides}]divides:
[$2/[\$@$@\divides;!~][1-]#1=\%{primeq}]primeq:
[[$1=~{cond}][$primeq;![$." "{print}]?1-{body}]#{printprimes}%]printprimes:

1000 printprimes;!

"""
code = R'''
[[$1=~][$$2/[\$@$@$@$@\/*-][1-]#1=\%[$." "]?1-]#%] f:
[[$1=~][$2[\$@$@$@$@\/*-][1+]#\$@=\%[$." "]?1-]#%] g:

1000 f;!
'''

# from parse import parse
# from constants import TOKEN_TYPES


# def pr(p, shift=''):
#     for t in p.data:
#         if t.token_type == TOKEN_TYPES.LAMBDA:
#             print(shift + '[')
#             pr(t.code, shift=shift + '    ')
#             print(shift + ']')
#         else:
#             print(shift + str(t))

# pr(p)

machine = FalseMachine(code)
machine.window.root.mainloop()
