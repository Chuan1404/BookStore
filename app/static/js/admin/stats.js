window.addEventListener("load", () => {
  const ctx = document.getElementById("myChart");
  new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["ACtion", "Adult", "Adventure", "Anime", "Chuyển sinh", "Cổ đại", "Commedy", "Comic"],
      datasets: [
        {
          label: "Doanh thu theo tháng",
          data: [100000, 200000, 400000, 534534, 223456, 32344,62523,72343],
          borderWidth: 1,
        },
        
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });

  const ctx2 = document.getElementById("myChart2");
  new Chart(ctx2, {
    type: "bar",
    data: {
      labels: ["One peace", "Naruto", "One punch man"],
      datasets: [
        {
          label: "% Tần suất sách bán",
          data: [50, 20, 30],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
});
