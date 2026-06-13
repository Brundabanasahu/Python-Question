var=input()
key={"break", "case", "continue", "default", "defer", "else", "for","func", "goto", "if", "map", "range", "return", "struct", "type", "var"}
if var in key:
    print("Keyword")
else:
    print("Not a Keyword")    