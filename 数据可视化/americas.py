# from pygal_maps_world.i18n import COUNTRIES
import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()

# wm.add()
wm.add('North America', {'ca': 123456, 'mx': 456789, 'us': 45678})
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('1.svg')
