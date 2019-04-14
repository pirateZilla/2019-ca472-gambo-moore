// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function(n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
}

// Area Chart Example
var ctx = document.getElementById("myAreaChart");
var jan = parseInt(document.getElementById("jan").value);
var feb = parseInt(document.getElementById("feb").value);
var mar = parseInt(document.getElementById("mar").value);
var apr = parseInt(document.getElementById("apr").value);
var may = parseInt(document.getElementById("may").value);
var jun = parseInt(document.getElementById("jun").value);
var jul = parseInt(document.getElementById("jul").value);
var aug = parseInt(document.getElementById("aug").value);
var sep = parseInt(document.getElementById("sep").value);
var oct = parseInt(document.getElementById("oct").value);
var nov = parseInt(document.getElementById("nov").value);
var dec = parseInt(document.getElementById("dec").value);

var wk1 = parseInt(document.getElementById("wk1").value);
var wk2 = parseInt(document.getElementById("wk2").value);
var wk3 = parseInt(document.getElementById("wk3").value);
var wk4 = parseInt(document.getElementById("wk4").value);
var wk5 = parseInt(document.getElementById("wk5").value);
var wk6 = parseInt(document.getElementById("wk6").value);
var wk7 = parseInt(document.getElementById("wk7").value);
var wk8 = parseInt(document.getElementById("wk8").value);
var wk9 = parseInt(document.getElementById("wk9").value);
var wk10 = parseInt(document.getElementById("wk10").value);

var mon = parseInt(document.getElementById("mon").value);
var tue = parseInt(document.getElementById("tue").value);
var wed = parseInt(document.getElementById("wed").value);
var thu = parseInt(document.getElementById("thu").value);
var fri = parseInt(document.getElementById("fri").value);
var sat = parseInt(document.getElementById("sat").value);
var sun = parseInt(document.getElementById("sun").value);

var monthDataset = [jun, jul, aug, sep, oct, nov, dec, jan, feb, mar, apr, may];
var monthLabels = ["Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May"];
var weekDataset = [wk1, wk2, wk3, wk4, wk5, wk6, wk7, wk8, wk9, wk10];
var weekLabels = ["17/03", "24/03", "31/03", "07/04", "14/04", "21/04", "28/04", "05/05", "12/05", "19/05"];
var dayDataset = [fri, sat, sun, mon, tue, wed, thu];
var dayLabels = ["Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu"];

var chartDataset = monthDataset;
var chartLabels = monthLabels;

var config = {
  type: 'line',
  data: {
    labels: monthLabels,
    datasets: [{
      label: "Score",
      lineTension: 0.3,
      backgroundColor: "rgba(21, 101, 192, 0.05)",
      borderColor: "rgba(21, 101, 192, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(21, 101, 192, 1)",
      pointBorderColor: "rgba(21, 101, 192, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(63, 129, 203, 1)",
      pointHoverBorderColor: "rgba(63, 129, 203, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: monthDataset,
    }],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function(value, index, values) {
            return number_format(value);
          }
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      intersect: false,
      mode: 'index',
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + ': ' + number_format(tooltipItem.yLabel);
        }
      }
    }
  }
}


var myLineChart = new Chart(ctx, config);

$("#3").click(function() {
  var chartDataset = monthDataset;
  var data = myLineChart.config.data;
  data.datasets[0].data = chartDataset;
  chartLabels = monthLabels;
  data.labels = chartLabels;
  myLineChart.update();
});
$("#4").click(function() {
  var chartDataset = weekDataset;
  var data = myLineChart.config.data;
  data.datasets[0].data = chartDataset;
  chartLabels = weekLabels;
  data.labels = chartLabels;
  myLineChart.update();
});
$("#5").click(function() {
  var chartDataset = dayDataset;
  var data = myLineChart.config.data;
  data.datasets[0].data = chartDataset;
  chartLabels = dayLabels;
  data.labels = chartLabels;
  myLineChart.update();
});

Chart.pluginService.register({
  beforeDraw: function(chart) {
    var width = chart.chart.width,
        height = chart.chart.height,
        ctx = chart.chart.ctx;

    ctx.restore();
    var fontSize = (height / 114).toFixed(2);
    ctx.font = fontSize + "em sans-serif";
    ctx.textBaseline = "middle";

    var text = "",
        textX = Math.round((width - ctx.measureText(text).width) / 2),
        textY = height / 2;

    ctx.fillText(text, textX, textY);
    ctx.save();
  }
});