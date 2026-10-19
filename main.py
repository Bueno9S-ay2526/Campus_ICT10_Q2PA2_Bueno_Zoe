# Using Python sets :P
from pyscript import display, document


def add_member(e):

    taxes_here = {'Rani / rani_sleeping', 'Wanderer / dad_sir', 'Dim / denias_dad', 'Xavier / dad_boss'}
    online_2011 = {'Gudz / bloxygod', 'Khelicho / daviddata2011', 'Adam / petduckadam', 'Nyan / dauboi'}
    og_2011 = {'Toast / moonsmthnalpha', 'Denia / deniadenial', 'Lux / luxembourg', 'Fish / fishyfih', 'Nana / nyenenaboo'}
    young_ones = {'Blue / 29indigo9', 'Jaydens / jaydensidk'}
    displayname = document.getElementById('dis_name').value.title()
    user = document.getElementById('username').value.lower()
    gaming_name = str(displayname) + ' / ' + str(user)
    gaming_club = taxes_here | online_2011 | og_2011 | young_ones
    gaming_club.add(gaming_name)

    display(f'List of members: {gaming_club}', target='results', append=False)
    display(f'The total no. of members: {len(gaming_club)}', target='results') #member count
