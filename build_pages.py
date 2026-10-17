"""Generate the bilingual study pages using Page 22's shared layout."""
from pathlib import Path
from html import escape
import re

root = Path(__file__).resolve().parent
source = (root / 'index.html').read_text(encoding='utf-8')
nav_css = '''    .page-nav { width: min(1100px, 100%); margin: auto; padding: 24px; display: flex; flex-wrap: wrap; gap: 16px; }
    .page-nav a { flex: 1 1 200px; text-align: center; padding: 24px 16px; border: 3px solid #173a32; border-radius: 14px; font-size: clamp(32px, 5vw, 44px); font-weight: 700; text-decoration: none; color: #173a32; background: #fffef8; }
    .page-nav a[aria-current="page"], .page-nav a:hover { color: white; background: #173a32; }
    .page-nav a:focus-visible { outline: 4px solid #b06b13; outline-offset: 4px; }
'''
if '.page-nav {' not in source:
    source = source.replace('  </style>', nav_css + '  </style>')

def nav(page):
    links = []
    for n, href in [(22, 'index.html'), (23, 'page23.html'), (24, 'page24.html')]:
        current = ' aria-current="page"' if n == page else ''
        links.append(f'<a href="{href}"{current}>Page {n}</a>')
    return '<nav class="page-nav" aria-label="Textbook pages">' + ''.join(links) + '</nav>'

source = re.sub(r'\s*<nav class="page-nav".*?</nav>', '', source, flags=re.S)
source = source.replace('<body>', '<body>\n  ' + nav(22))
(root / 'index.html').write_text(source, encoding='utf-8')

pages = {
23: [
('A family camping trip', [
('Todos los años miles de personas van de cámping a las sierras chilenas y lo pasan muy bien.', 'Every year, thousands of people go camping in the Chilean mountain ranges and have a great time.'),
('¡Los paisajes son hermosos!', 'The landscapes are beautiful!'),
('Éstas son unas fotos de una familia y sus maravillosas vacaciones.', 'These are some photos of a family and their wonderful vacation.'),
('la naturaleza', 'nature'),
('Al amanecer, mi familia y yo dimos un paseo a caballo.', 'At dawn, my family and I went for a horseback ride.'),
('Durante nuestro viaje nos gustaba escalar rocas.', 'During our trip, we enjoyed rock climbing.'),
('Al anochecer las estrellas se veían muy claras y cercanas.', 'At nightfall, the stars looked very clear and close.')]),
('Activity 1', [
('Equipo de cámping', 'Camping equipment'),
('ESCUCHAR', 'LISTEN'),
('En una hoja de papel escribe los números del 1 al 6.', 'On a sheet of paper, write the numbers from 1 to 6.'),
('Vas a escuchar a unos jóvenes hablar sobre el equipo de cámping.', 'You are going to listen to some young people talk about camping equipment.'),
('Escucha cada frase y escribe si es lógica o ilógica.', 'Listen to each statement and write whether it is logical or illogical.')]),
('Activity 2', [
('Ir de cámping', 'Going camping'),
('ESCUCHAR', 'LISTEN'),
('En una hoja de papel escribe los números del 1 al 5.', 'On a sheet of paper, write the numbers from 1 to 5.'),
('Escucha cada frase y escribe C (cierta) o F (falsa), según las fotos.', 'Listen to each statement and write C (true) or F (false), based on the photos.'),
('Vas a oír cada frase dos veces.', 'You will hear each statement twice.')])],
24: [
('Jairo and his mom', [
('Jairo le cuenta a su mamá cómo le fue en su paseo por la sierra.', 'Jairo tells his mom how his trip through the mountains went.'),
('Mamá: Hola hijo, ¿qué tal te fue en tu paseo?', 'Mom: Hi, son. How was your trip?'),
('Jairo: Nos divertimos mucho, mami.', 'Jairo: We had a lot of fun, Mom.'),
('¡Pero no te imaginas lo que nos pasó!', 'But you can’t imagine what happened to us!'),
('Mamá: ¿Qué sucedió?', 'Mom: What happened?'),
('Jairo: Cuando estábamos escalando una montaña, vimos relámpagos y oímos un trueno.', 'Jairo: While we were climbing a mountain, we saw lightning and heard a clap of thunder.'),
('¡Luego comenzó a caer granizo!', 'Then it started to hail!'),
('Mamá: ¡No me digas!', 'Mom: You don’t say!'),
('¿Y qué hicieron?', 'And what did you do?'),
('Jairo: Nos refugiamos en una caverna.', 'Jairo: We took shelter in a cave.'),
('Una vez allí, nos sentamos a hablar mientras pasaba el mal tiempo.', 'Once there, we sat down to talk while the bad weather passed.'),
('Nos impresionó el tamaño del granizo.', 'We were amazed by the size of the hailstones.'),
('¡Parecían bolas de golf!', 'They looked like golf balls!'),
('Mamá: ¡Qué bueno que encontraron refugio!', 'Mom: How good that you found shelter!'),
('Jairo: Sí, pero ahí no terminó todo.', 'Jairo: Yes, but that wasn’t the end of it.'),
('Cuando dejó de llover salimos de la caverna y comenzamos a bajar la montaña.', 'When it stopped raining, we left the cave and began to go down the mountain.'),
('El suelo estaba mojado y Miguel perdió el equilibrio, pero no se cayó.', 'The ground was wet, and Miguel lost his balance, but he didn’t fall.'),
('Mamá: ¡Ay, qué bien!', 'Mom: Oh, that’s good!'),
('¿Y entonces qué pasó?', 'And then what happened?'),
('Jairo: Bajamos la montaña y anduvimos por un rato hasta que nos acercamos a un bosque grande.', 'Jairo: We went down the mountain and walked for a while until we came near a large forest.'),
('Habíamos olvidado la linterna y la brújula en la caverna.', 'We had left the flashlight and the compass in the cave.'),
('¡Yo sabía que íbamos a perdernos!', 'I knew we were going to get lost!'),
('Mamá: ¿Y cómo volvieron entonces?', 'Mom: So how did you get back?'),
('Jairo: Al rato apareció un guardabosques (park ranger) que nos mostró hacia dónde ir.', 'Jairo: After a while, a park ranger appeared and showed us which way to go.'),
('Llegamos a la tienda al anochecer.', 'We arrived at the tent at nightfall.'),
('Mamá: ¡Ay, hijo, tus aventuras me asustan mucho!', 'Mom: Oh, son, your adventures really scare me!')]),
('Activity 3', [
('La aventura de Jairo y sus amigos', 'The adventure of Jairo and his friends'),
('ESCUCHAR', 'LISTEN'),
('En una hoja de papel escribe los números del 1 al 4.', 'On a sheet of paper, write the numbers from 1 to 4.'),
('Escucha cada frase y escribe C si es cierta o F si es falsa.', 'Listen to each statement and write C if it is true or F if it is false.')]),
('Page labels', [
('veinticuatro', 'twenty-four'),
('Capítulo 1 · Días inolvidables', 'Chapter 1 · Unforgettable days')])]
}

for number, sections in pages.items():
    content = []
    for heading, pairs in sections:
        content.append(f'<h2>{escape(heading)}</h2>')
        for es, en in pairs:
            content.append(f'<article class="pair"><p class="es" lang="es">{escape(es)}</p><p class="en" lang="en"> - {escape(en)}</p></article>')
    page = source.replace(nav(22), nav(number)).replace('· Page 22', f'· Page {number}')
    page = re.sub(r'<main>.*?</main>', '<main>\n' + '\n'.join(content) + '\n  </main>', page, flags=re.S)
    page = page.replace('photograph of page 22', f'photograph of page {number}')
    page = page.replace('<title>¡Cámping! — Spanish &amp; English</title>', f'<title>Page {number} — Spanish &amp; English Camping</title>')
    (root / f'page{number}.html').write_text(page, encoding='utf-8')
    print(f'Page {number}: {sum(len(pairs) for _, pairs in sections)} translation pairs')
