def concat(arr):
    result = ""
    for string in arr:
        result += string
    return result
arr = ["Johnny", "DeeDee", "Joey", "Marky"]
result = concat(arr)
print(result)
with open("output.html", "w") as f:
    f.write("<html><body>")
    f.write(result)
    f.write("</body></html>")
