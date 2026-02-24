// ============================================
// ACTIVE MENU HIGHLIGHTING
// Save as: static/js/active-menu.js
// ============================================

(function() {
  'use strict';

  function activateMenu() {
    console.log('🔍 Checking active menu...');
    
    const currentPath = window.location.pathname;
    console.log('📍 Current path:', currentPath);

    // Get ALL navigation links that have data-url attribute
    const navLinks = document.querySelectorAll('.navigation a[data-url]');
    console.log('🔗 Found', navLinks.length, 'nav links with data-url');

    // First, remove 'active' class from all links
    navLinks.forEach(link => {
      if (link.classList.contains('active')) {
        console.log('❌ Removing active from:', link.textContent.trim());
        link.classList.remove('active');
      }
    });

    // Now check each link to see if it matches current path
    navLinks.forEach(link => {
      const linkPath = link.getAttribute('data-url');
      
      if (!linkPath) return;

      // Normalize both paths
      let normalizedCurrent = currentPath.replace(/\/$/, '') || '/';
      let normalizedLink = linkPath.replace(/\/$/, '') || '/';

      console.log(`Comparing: "${normalizedCurrent}" vs "${normalizedLink}"`);

      // Check if current path matches this link
      const isMatch = (normalizedCurrent === normalizedLink) || 
                      (normalizedLink !== '/' && currentPath.startsWith(normalizedLink + '/'));

      if (isMatch) {
        console.log('✅ MATCH FOUND:', link.textContent.trim());
        link.classList.add('active');
        
        // Force browser to re-paint the element
        link.style.display = 'inline-block';
        setTimeout(() => {
          link.style.display = '';
        }, 50);
      }
    });
  }

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', activateMenu);
  } else {
    activateMenu();
  }

  // Run again after a delay to catch any dynamically loaded content
  setTimeout(activateMenu, 100);
  setTimeout(activateMenu, 500);

  // Listen for navigation changes (for SPA)
  window.addEventListener('load', activateMenu);
})();