import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
head = '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
s = s.replace('</style>\n', '</style>\n</head>\n<body>\n', 1)
s = s.rstrip() + '\n</body>\n</html>\n'
open(dst, 'w').write(head + s)
