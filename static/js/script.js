const toggleBtn = document.getElementById('toggleSidebar');
const sidebar = document.getElementById('sidebar');
const closeBtn = document.getElementById('closeSidebar');
const overlay = document.getElementById('overlay');
const mainContent = document.getElementById('main-content');

// Abrir sidebar
toggleBtn.addEventListener('click', () => {
  sidebar.classList.add('active');
});

// Fechar com botão X
closeBtn.addEventListener('click', () => {
  sidebar.classList.remove('active');
});

// Fechar clicando no overlay
overlay.addEventListener('click', () => {
  sidebar.classList.remove('active');
});

// Fechar clicando no conteúdo principal
mainContent.addEventListener('click', () => {
  if (window.innerWidth < 768 && sidebar.classList.contains('active')) {
    sidebar.classList.remove('active');
  }
});

// Fechar ao clicar nos links
document.querySelectorAll('#sidebar .nav-link').forEach(link => {
  link.addEventListener('click', () => {
    if (window.innerWidth < 768) {
      sidebar.classList.remove('active');
    }
  });
});
