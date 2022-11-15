from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view

def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32    #первод в форенгейты
    xml = '<xml>\n'
    xml += '    <temperature units = "f">{}</temperature\n'\
        .format(t)
    xml += '    <wind_speed_view units = "m/c">{}</(wind_speed_view\n'\
        .format(w)
    xml += '    <pressure units = "c">{}</pressure\n'\
        .format(p)
    xml += '<xml>'

    with open('Lec/LEC4/JOIN_JOB/new_data.xml', 'w') as page:
        page.write(xml)

    return data