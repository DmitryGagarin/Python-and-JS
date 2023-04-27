const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['BDK', 'OUG', 'XFZ', 'EFDS'],
      datasets: [{
        label: 'Cost of crypto',
        data: [900, 300, 657, 732,],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
