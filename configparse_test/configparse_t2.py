import ConfigParser

config = ConfigParser.ConfigParser()
config.read('example.cfg')

# Set the third, optional argument of get to 1 if you wish to use raw mode.
print config.get('Section1', 'foo', 0)  # -> "Python is fun!"
print config.get('Section1', 'foo', 1)  # -> "%(bar)s is %(baz)s!"
print config.get('Section1', 'my_list')
my_list = config.get('Section1', 'my_list')[1:-1].split(',')

print (my_list[0].split(':')[1])

# The optional fourth argument is a dict with members that will take
# precedence in interpolation.
print config.get('Section1', 'foo', 0, {'bar': 'Documentation',
                                        'baz': 'evil'})


# ZLC TEST  Set the third optional argument of get to 1
print config.get('Section1', 'foo', 1, {'bar': 'Documentation',
                                        'baz': 'evil'})


