import sys

try:
    F = float(sys.argv[1])
except IndexError:
    raise IndexError\
    ('Fahrenheit must be supplied on the command line!')
    sys.exit(1)
except ValueError:
    raise ValueError\
    ('Fahrenheit must be a pure number, not "%s"' % sys.argv[1])
    sys.exit(1)

C = (F - 32)*(5.0/9)
print '%.1f C' % C
