#!/usr/bin/env python
f = open('helloworld.html', 'w')

message = """<html>
<head></head>
<body><p>Hello Jenkins!</p></body>
</html>"""

f.write(message)
f.close()
