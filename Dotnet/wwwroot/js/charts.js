ctx = document.getElementById('myChart');

var labels = []
var data = []

function set_data(new_labels, new_data){
  labels = new_labels;
  data = new_data;
}

  chart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: 'Hartslag',
        data: data,
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
        min: 55,
        max: 75,
        }
      }
    }
  });

  interval = setInterval(function() {
    time = new Date();
    if(chart.data.labels.length > 20) {
        chart.data.labels.shift();
        chart.data.datasets[0].data.shift();
    }
    chart.data.labels.push(time.getHours() + ":" + time.getMinutes() + ":" + time.getSeconds());
    chart.data.datasets[0].data.push(Math.random()*10 + 60);
    chart.update();
}, 5000);
