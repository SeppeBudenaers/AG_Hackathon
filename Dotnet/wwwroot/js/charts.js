ctx = document.getElementById('myChart');

var labels = []
var data = []

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
        max: 120,
        }
      }
    }
  });


  function set_data(new_labels, new_data){
    console.log("set_data")
    labels.push(...new_labels);
    data.push(...new_data);
    
    console.log(labels, labels.length > 20)

    while (labels.length > 20) {
      labels.shift()
      data.shift()
    }

    console.log(labels)


    chart.update()
  }

//   interval = setInterval(function() {
//     time = new Date();
//     if(chart.data.labels.length > 20) {
//         chart.data.labels.shift();
//         chart.data.datasets[0].data.shift();
//     }
//     chart.data.labels.push(time.getHours() + ":" + time.getMinutes() + ":" + time.getSeconds());
//     chart.data.datasets[0].data.push(Math.random()*10 + 60);
//     chart.update();
// }, 5000);
