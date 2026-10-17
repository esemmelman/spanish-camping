'use strict';

function shuffle(items) {
  const result = [...items];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
}

const ui = Object.fromEntries(['progress', 'score', 'question', 'answers', 'feedback', 'next', 'restart'].map(id => [id, document.getElementById(id)]));
let questions, index, correct, answered, locked;
let lastCorrectPosition = -1, positionStreak = 0;

function arrangeAnswers(answer, alternatives) {
  const positions = [0, 1, 2, 3].filter(position => positionStreak < 2 || position !== lastCorrectPosition);
  const position = positions[Math.floor(Math.random() * positions.length)];
  positionStreak = position === lastCorrectPosition ? positionStreak + 1 : 1;
  lastCorrectPosition = position;
  const options = shuffle(alternatives).slice(0, 3);
  options.splice(position, 0, answer);
  return options;
}

function updateScore() {
  ui.score.textContent = `Score: ${correct} / ${answered} answered${answered ? ` · ${Math.round(correct / answered * 100)}%` : ''}`;
}

function showQuestion(focus = true) {
  locked = false;
  const question = questions[index];
  ui.progress.textContent = `Phrase ${index + 1} of ${questions.length}`;
  ui.question.textContent = question.es;
  ui.feedback.textContent = '';
  ui.next.hidden = true;
  ui.restart.hidden = true;
  ui.answers.replaceChildren();
  const alternatives = [...new Set(phraseQuestions.map(q => q.en))].filter(en => en !== question.en);
  const options = arrangeAnswers(question.en, alternatives);
  options.forEach(option => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'answer';
    button.textContent = ` - ${option}`;
    button.addEventListener('click', () => {
      if (locked) return;
      locked = true;
      answered++;
      const right = option === question.en;
      if (right) correct++;
      for (const choice of ui.answers.children) {
        choice.disabled = true;
        if (choice.textContent === ` - ${question.en}`) choice.classList.add('correct');
      }
      if (!right) button.classList.add('incorrect');
      ui.feedback.textContent = right ? 'Correct! +1 point.' : `Incorrect. The correct answer is: ${question.en}`;
      updateScore();
      const finished = index === questions.length - 1;
      ui.next.hidden = finished;
      ui.restart.hidden = !finished;
      if (finished) ui.feedback.textContent += ` Quiz complete! Final score: ${correct} out of ${questions.length}.`;
    });
    ui.answers.append(button);
  });
  if (focus) ui.question.focus();
}

function start(focus = true) {
  questions = shuffle(phraseQuestions);
  index = correct = answered = 0;
  lastCorrectPosition = -1;
  positionStreak = 0;
  updateScore();
  showQuestion(focus);
}
ui.next.addEventListener('click', () => { if (locked && index < questions.length - 1) { index++; showQuestion(); } });
ui.restart.addEventListener('click', () => start());
start(false);
