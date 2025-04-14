document.addEventListener('DOMContentLoaded', () => {
  // Dados esperados da Lei de Benford
  const expected = {
    labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    data: [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
  };

  // Dados do JSON de exemplo
  const rawData = [
    "2944955", "182066", "1792000", "6176", "4887"
  ];

  const observed = Array(9).fill(0);

  rawData.forEach(value => {
    const firstDigit = value.trim()[0];
    const digit = parseInt(firstDigit);
    if (digit >= 1 && digit <= 9) {
      observed[digit - 1]++;
    }
  });

  const total = observed.reduce((acc, curr) => acc + curr, 0);
  const observedPercent = observed.map(count => (count / total * 100).toFixed(1));

  // Gráfico Esperado
  new Chart(document.getElementById('benfordExpectedChart'), {
    type: 'bar',
    data: {
      labels: expected.labels,
      datasets: [{
        label: 'Probabilidade (%)',
        data: expected.data,
        backgroundColor: '#6366F1'
      }]
    },
    options: {
      scales: { y: { beginAtZero: true } }
    }
  });

  // Gráfico Observado
  new Chart(document.getElementById('benfordObservedChart'), {
    type: 'bar',
    data: {
      labels: expected.labels,
      datasets: [{
        label: 'Distribuição Observada (%)',
        data: observedPercent,
        backgroundColor: '#10B981'
      }]
    },
    options: {
      scales: { y: { beginAtZero: true } }
    }
  });
});
