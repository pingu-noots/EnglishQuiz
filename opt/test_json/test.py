from polyglot.text import Text 

t = "Machine learning is employed in a range of computing tasks where designing and programming explicit algorithms with good performance as difficult or infeasible. Example applications include email filtering, detection of network intruders and computer vision. Machine learning is closely related to computational statistics, which also focuses on predictions making through the use of computer. It has strong ties to mathematical optimization, which delivers methods, theory and application domains to the field."

tokens = Text(t)
for token in tokens.pos_tags:
    print(token)
