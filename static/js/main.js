// Crime Empire Guide - Accordion + Panel Switching

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
  var row = document.getElementById('heroAccordion');
  if (row) {
    var cards = row.children;
    for (var i = 0; i < cards.length; i++) {
      cards[i].classList.remove('expanded');
    }
    var target = row.querySelector('[data-game="' + gameId + '"]');
    if (target) target.classList.add('expanded');
  }

  var panels = document.querySelectorAll('.game-panel');
  for (var i = 0; i < panels.length; i++) {
    panels[i].classList.remove('active');
  }
  var panel = document.getElementById('panel-' + gameId);
  if (panel) panel.classList.add('active');


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

// Mobile Navigation Toggle
function toggleMobileNav() {
  var overlay = document.getElementById('mobileOverlay');
  var drawer = document.getElementById('mobileDrawer');
  var toggle = document.querySelector('.mobile-nav-toggle');
  if (!overlay || !drawer) return;
  var isOpen = overlay.classList.contains('open');
  overlay.classList.toggle('open');
  drawer.classList.toggle('open');
  if (toggle) toggle.classList.toggle('open');
  document.body.style.overflow = isOpen ? '' : 'hidden';
}
