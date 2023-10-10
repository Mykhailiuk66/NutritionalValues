const alertElements = document.querySelectorAll('.alert');

alertElements.forEach(alert => {
  alert.addEventListener('click', () => {
    alert.classList.add('fade');
    setTimeout(() => {
      alert.remove();
    }, 500);
  });
});


// const nutritionAddBtns = document.querySelectorAll('.nutrition-add');

// nutritionAddBtns.forEach(el => {
//   el.addEventListener('click', function (e) {
//     e.preventDefault();
//     url = el.getAttribute('href')
//     fetch(url, {
//       headers: {
//         "X-Requested-With": "XMLHttpRequest",
//       },
//       method: 'GET'
//     })

//   });
// });



// const nutritionRemoveBtns = document.querySelectorAll('.nutrition-remove');

// nutritionRemoveBtns.forEach(el => {
//   el.addEventListener('click', function (e) {
//     e.preventDefault();
//     url = el.getAttribute('href')
//     fetch(url, {
//       headers: {
//         "X-Requested-With": "XMLHttpRequest",
//       },
//       method: 'GET'
//     })
//     location.href = location.href;
//   });
// });
