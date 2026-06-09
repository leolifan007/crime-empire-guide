// Crime Empire Guide - Accordion + Panel Switching
// Cards use onclick="activateCard(this); switchGame('id');" directly in HTML
// CTA links use onclick="event.stopPropagation();" to prevent card click

function activateCard(card) {
  var row = document.getElementById('heroAccordion');
  if (!row) return;
  var cards = row.children;
  for (var i = 0; i < cards.length; i++) {
    cards[i].classList.remove('expanded');
  }
  card.classList.add('expanded');
}

function switchGame(gameId) {
  var contentArea = document.getElementById('home-content');
  var oldPanel = contentArea ? contentArea.querySelector('.game-panel.active') : null;
  var newPanel = document.getElementById('panel-' + gameId);

  // Measure new panel height before switching
  if (contentArea && oldPanel && newPanel && oldPanel !== newPanel) {
    var oldH = oldPanel.offsetHeight;
    // Temporarily make new panel visible (but hidden) to measure height
    newPanel.style.position = 'relative';
    newPanel.style.opacity = '0';
    newPanel.style.pointerEvents = 'none';
    var newH = newPanel.offsetHeight;
    newPanel.style.position = '';
    newPanel.style.opacity = '';
    newPanel.style.pointerEvents = '';
    // Lock content area to max of old and new heights
    contentArea.style.height = Math.max(oldH, newH) + 'px';
  }

  // Switch hero cards
  var row = document.getElementById('heroAccordion');
  if (row) {
    var cards = row.children;
    for (var i = 0; i < cards.length; i++) {
      cards[i].classList.remove('expanded');
    }
    var target = row.querySelector('[data-game="' + gameId + '"]');
    if (target) target.classList.add('expanded');
  }

  // Switch content panels
  var panels = document.querySelectorAll('.game-panel');
  for (var i = 0; i < panels.length; i++) {
    panels[i].classList.remove('active');
  }
  if (newPanel) newPanel.classList.add('active');

  // After new panel renders, transition to actual height then release
  requestAnimationFrame(function() {
    requestAnimationFrame(function() {
      if (contentArea && newPanel) {
        contentArea.style.height = newPanel.offsetHeight + 'px';
        // Release after CSS height transition completes
        setTimeout(function() {
          contentArea.style.height = '';
        }, 350);
      } else if (contentArea) {
        contentArea.style.height = '';
      }
    });
  });
}

document.addEventListener('keydown', function(e) {
  var cards = document.querySelectorAll('.game-card');
  if (!cards.length) return;
  var idx = -1;
  for (var i = 0; i < cards.length; i++) {
    if (cards[i].classList.contains('expanded')) { idx = i; break; }
  }
  if (idx < 0) return;
  if (e.key === 'ArrowRight' && idx < cards.length - 1) {
    cards[idx + 1].click();
    e.preventDefault();
  } else if (e.key === 'ArrowLeft' && idx > 0) {
    cards[idx - 1].click();
    e.preventDefault();
  }
});