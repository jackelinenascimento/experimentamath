document.addEventListener('DOMContentLoaded', function () {
  const ctx = document.getElementById('benfordChart');

  if (ctx) {
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
        datasets: [{
          label: 'Distribuição Esperada (%)',
          data: [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6],
          backgroundColor: 'rgba(75, 192, 192, 0.6)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Distribuição Esperada pela Lei de Benford'
          },
          legend: {
            display: false
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 35
          }
        }
      }
    });
  } else {
    console.warn('Canvas #benfordChart não encontrado.');
  }
});
