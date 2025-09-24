  const slider = document.getElementById('uniqueProductSlider');
  let isDown = false;
  let startX;
  let scrollLeft;

  // Drag functionality
  slider.addEventListener('mousedown', (e) => {
    isDown = true;
    slider.classList.add('active');
    startX = e.pageX - slider.offsetLeft;
    scrollLeft = slider.scrollLeft;
  });

  slider.addEventListener('mouseleave', () => {
    isDown = false;
    slider.classList.remove('active');
  });

  slider.addEventListener('mouseup', () => {
    isDown = false;
    slider.classList.remove('active');
  });

  slider.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - slider.offsetLeft;
    const walk = (x - startX) * 1.5; // scroll-fast
    slider.scrollLeft = scrollLeft - walk;
  });

  // Auto scroll functionality
  let autoScroll = () => {
    const scrollAmount = slider.offsetWidth / 4; // one product width
    if (slider.scrollLeft + scrollAmount >= slider.scrollWidth) {
      slider.scrollLeft = 0;
    } else {
      slider.scrollLeft += scrollAmount;
    }
  };

  let autoPlay = setInterval(autoScroll, 3000); // every 3 seconds

  // Pause on hover
  slider.addEventListener('mouseover', () => clearInterval(autoPlay));
  slider.addEventListener('mouseout', () => {
    autoPlay = setInterval(autoScroll, 3000);
  });
