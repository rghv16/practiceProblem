import re

Regex_Pattern = r'^[1-9][0-9]{4} (C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$'
for _ in range(int(input())):
    if bool(re.search(Regex_Pattern, input())):
        print('VALID')
    else:
        print('INVALID')

