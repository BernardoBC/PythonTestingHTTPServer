#!/usr/bin/env python
f = open('helloworld.html', 'w')

message = """<html>
<head></head>
<body><p>Hello Everyone!</p></body>
</html>"""

f.write(message)
f.close()
