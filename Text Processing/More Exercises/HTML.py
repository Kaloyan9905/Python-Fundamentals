title, content = input(), input()
print("<h1>")
print("    " + title)
print("</h1>")

print("<article>")
print("    " + content)
print("</article>")
command = input()
while not command == "end of comments":
    print("<div>")
    print("    " + command)
    print("</div>")
    command = input()
