/* globals Chart:false, feather:false */

$(function () {
  'use strict'
  const valueAc = JSON.parse(document.getElementById('nodeAc').textContent);
  const valueGy = JSON.parse(document.getElementById('nodeGy').textContent);
  const valueSo = JSON.parse(document.getElementById('nodeSo').textContent);
  const valueTe = JSON.parse(document.getElementById('nodeTe').textContent);


  var valAcce = JSON.parse(valueAc);
  var valGyro = JSON.parse(valueGy);
  var valSoil = JSON.parse(valueSo);
  var valTemp = JSON.parse(valueTe);

//**
// Accelerometer Chart
  var timeAc = [];
  var meanAc = [];
  //outer loop
  valAcce.forEach((item, i) => {
    //inner loop
    item.forEach((myvar, i) => {
      timeAc.push(new Date(myvar.time).getHours().toString().padStart(2, '0')+ ":"+new Date(myvar.time).getMinutes().toString().padStart(2, '0'));
      meanAc.push(myvar.mean);
    });

  });

  feather.replace()

  // Graphs
  var ctx = document.getElementById('AccelerometerChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels:timeAc,
      datasets: [{
        data: meanAc,
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })

//***
//Gyro Chart
  var timeGy = [];
  var meanGy = [];
  //outer loop
  valGyro.forEach((item, i) => {
    //inner loop
    item.forEach((myvar, i) => {
      timeGy.push(new Date(myvar.time).getHours().toString().padStart(2, '0')+ ":"+new Date(myvar.time).getMinutes().toString().padStart(2, '0'));
      meanGy.push(myvar.mean);
    });

  });

  feather.replace()

  // Graphs
  var gychart = document.getElementById('GyroChart')
  // eslint-disable-next-line no-unused-vars
  var GyroChart = new Chart(gychart, {
    type: 'line',
    data: {
      labels:timeGy,
      datasets: [{
        data: meanGy,
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })

//***
//Soil Moisture Chart
  var timeSo = [];
  var meanSo = [];

  valSoil.forEach((item, i) => {
    //inner loop
    item.forEach((myvar, i) => {
      timeSo.push(new Date(myvar.time).getHours().toString().padStart(2, '0')+ ":"+new Date(myvar.time).getMinutes().toString().padStart(2, '0'));
      meanSo.push(myvar.mean);
    });

  });
  feather.replace()
  var sochart = document.getElementById('SoilChart')
  // eslint-disable-next-line no-unused-vars
  var SoilChart = new Chart(sochart, {
    type: 'line',
    data: {
      labels:timeSo,
      datasets: [{
        data: meanSo,
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })

//***
//Temperature Chart
  var timeTe = [];
  var meanTe = [];

  valTemp.forEach((item, i) => {
    //inner loop
    item.forEach((myvar, i) => {
      timeTe.push(new Date(myvar.time).getHours().toString().padStart(2, '0')+ ":"+new Date(myvar.time).getMinutes().toString().padStart(2, '0'));
      meanTe.push(myvar.mean);
    });

  });
  feather.replace()
  var sochart = document.getElementById('TemperatureChart')
  // eslint-disable-next-line no-unused-vars
  var SoilChart = new Chart(sochart, {
    type: 'line',
    data: {
      labels:timeTe,
      datasets: [{
        data: meanTe,
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })

});
