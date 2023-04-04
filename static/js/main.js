const alertElements = document.querySelectorAll('.alert');

alertElements.forEach(alert => {
  alert.addEventListener('click', () => {
    alert.classList.add('fade');
    setTimeout(() => {
      alert.remove();
    }, 500);
  });
});
