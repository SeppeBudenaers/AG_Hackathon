ctx = document.getElementById('myChart');

var labels = []
var data = []
var Body_Temperature = []
var Blood_Oxygen = []



  chart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: 'Hartslag',
        data: data,
        borderWidth: 1
      },{
        label: 'Body_Temperature',
        data: Body_Temperature,
        borderWidth: 1
      },{
        label: 'Blood_Oxygen',
        data: Blood_Oxygen,
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
        min: 35,
        max: 120,
        }
      }
    }
  });


  function set_data(new_labels, new_data, new_body_temp, new_blood_oxygen){
    console.log("set_data")
    labels.push(...new_labels);
    data.push(...new_data);
    Body_Temperature.push(...new_body_temp)
    Blood_Oxygen.push(...new_blood_oxygen)
    
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
