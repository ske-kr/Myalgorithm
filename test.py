# output=[]
#         for i in words:
#             string_to_pattern={}
#             pattern_to_string={}
#             for s in range(len(pattern)):
#                 string_to_pattern[i[s]]=pattern[s]
#                 pattern_to_string[pattern[s]]=i[s]
#             A=""
#             B=""
#             for s in range(len(pattern)):
#                 A+=pattern_to_string[pattern[s]]
#                 B+=string_to_pattern[i[s]]
#             if A==i and B==pattern:
#                 output.append(i)
#         return output

a={"a" : 1, "b":2}
print(len(a))