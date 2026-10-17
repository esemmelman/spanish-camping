"""Generate the bilingual study pages using Page 22's shared layout."""
from pathlib import Path
from html import escape
from html import unescape
import json
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
    current = ' aria-current="page"' if page == 'phrases' else ''
    links.append(f'<a href="phrases.html"{current}>Phrases</a>')
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

# Use the displayed translations as the quiz's single source of content.
excluded = {'Vocabulario en contexto 1', 'veintidós', 'veinticuatro',
            'Capítulo 1 · Días inolvidables', 'ESCUCHAR', 'Equipo de cámping',
            'Ir de cámping', 'La aventura de Jairo y sus amigos'}
questions = []
seen = set()
for number, filename in [(22, 'index.html'), (23, 'page23.html'), (24, 'page24.html')]:
    text = (root / filename).read_text(encoding='utf-8')
    for es, en in re.findall(r'<p class="es" lang="es">(.*?)</p><p class="en" lang="en"> - (.*?)</p>', text):
        es, en = unescape(es), unescape(en)
        if es in excluded or es in seen:
            continue
        seen.add(es)
        questions.append({'es': es, 'en': en, 'page': number})
(root / 'phrases-data.js').write_text('const phraseQuestions = ' + json.dumps(questions, ensure_ascii=False, indent=2) + ';\n', encoding='utf-8')
quiz = source.replace(nav(22), nav('phrases'))
quiz = quiz.replace('<title>¡Cámping! — Spanish &amp; English</title>', '<title>Phrases Quiz — Spanish &amp; English</title>')
quiz = re.sub(r'<header>.*?</header>', '''<header>
    <p class="eyebrow">Practice · Pages 22–24</p>
    <h1>Phrases</h1>
    <p class="intro">Choose the English translation. Each answer is scored immediately. Questions and answers are shuffled each time.</p>
  </header>''', quiz, flags=re.S)
quiz = re.sub(r'<main>.*?</main>', '''<main>
    <p id="progress" class="intro"></p>
    <p id="score" class="intro" aria-live="polite"></p>
    <section class="pair" aria-labelledby="question">
      <p id="source-page" class="intro"></p>
      <h2 id="question" lang="es" tabindex="-1"></h2>
      <div id="answers" class="answers" aria-label="English translations"></div>
    </section>
    <p id="feedback" class="intro" role="status"></p>
    <button id="next" class="quiz-button" type="button" hidden>Next phrase</button>
    <button id="restart" class="quiz-button" type="button" hidden>Play again</button>
    <noscript><p class="intro">Enable JavaScript to use the phrases quiz.</p></noscript>
  </main>''', quiz, flags=re.S)
quiz = re.sub(r'<footer>.*?</footer>', '<footer>Practice phrases from all three textbook pages.</footer>', quiz, flags=re.S)
quiz = quiz.replace('</style>', '''    .answers { display: grid; gap: 18px; }
    .quiz-button, .answer { font: inherit; font-size: clamp(28px, 4vw, 44px); line-height: 1.35; font-weight: 700; border: 3px solid #173a32; border-radius: 12px; padding: 24px; cursor: pointer; background: #fffef8; color: #173a32; }
    .answer { text-align: left; width: 100%; }
    .answer:hover:enabled, .quiz-button:hover { background: #e0eadb; }
    .answer.correct { background: #d9edcf; border-color: #315d20; }
    .answer.incorrect { background: #fce1dc; border-color: #a32a19; }
    .answer:disabled { cursor: default; opacity: 1; }
    button:focus-visible { outline: 4px solid #b06b13; outline-offset: 4px; }
    #question { font-size: clamp(36px, 5vw, 58px); margin-top: 20px; }
    #feedback { font-weight: 700; }
    [hidden] { display: none !important; }
  </style>''')
quiz = quiz.replace('</body>', '<script src="phrases-data.js"></script>\n<script src="phrases.js"></script>\n</body>')
(root / 'phrases.html').write_text(quiz, encoding='utf-8')
print(f'Quiz: {len(questions)} unique phrases')
