

tree = {"rule": "go left", 
        "left": {
            "rule": "go right",
            "left": 4,
            "right": 2},
        "right": {
            "rule": "go left",
            "left": 1,
            "right": 0}}

def traverse(t):
    if t["rule"] == "go left":
        if isinstance(t["left"], dict):
            return traverse(t["left"])
        else:
            return t["left"]
    else:
        if isinstance(t["right"], dict):
            return traverse(t["right"])
        else:
            return t["right"]

 
print(traverse(tree))
