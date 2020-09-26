import cfile as C
hello = C.cfile('hello.c')
hello.code.append(C.sysinclude('stdio.h'))
hello.code.append(C.blank())
hello.code.append(C.function('main', 'int',).add_param(C.variable('argc', 'int')).add_param(C.variable('argv', 'char', pointer=2)))
body = C.block(innerIndent=3)
body.append(C.statement(C.fcall('printf').add_arg(r'"Hello World!\n"')))
body.append(C.statement('return 0'))
hello.code.append(body)
print(str(hello))
