// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';
Chart.defaults.global.defaultFontStyle = 'bold';

// Pie Chart Example
var score = parseInt(document.getElementById("score").value);
var negscore = 100 - score;
var lastMonthScore = parseInt(document.getElementById("last_month_avg").value);
var negLastMonthScore = 100 - lastMonthScore;
var avgMonthScore = parseInt(document.getElementById("total_avg").value);
var negAvgMonthScore = 100 - avgMonthScore;

var chart_label = ["Positive", "Negative"];
var pie_dataset = [score, negscore];



var ctx = document.getElementById("myPieChart");

var config ={
  type: 'doughnut',
  data: {
    labels: ["Positive", "Negative"],
    datasets: [{
      data: [score, negscore],
      backgroundColor: ['#1565c0', '#dc3545'],
      hoverBackgroundColor: ['#3f81cb', '#E54C59'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 60,
  },
};

var myPieChart = new Chart(ctx, config);


Chart.pluginService.register({
  beforeDraw: function (chart) {
    var width = chart.chart.width,
      height = chart.chart.height,
      ctx = chart.chart.ctx;
    type = chart.config.type;

    ctx.restore();

    if (type == 'doughnut') {
      var fontSize = (height / 80).toFixed(2);
      ctx.font = fontSize + "em Roboto";
      ctx.textBaseline = "middle";

      var text = pie_dataset[0] + "%",
        textX = Math.round((width - ctx.measureText(text).width) / 2),
        textY = height / 2;

      ctx.fillText(text, textX, textY);
      ctx.save();
    }
  }
});



$("#0").click(function() {
  var data = myPieChart.config.data;
  data.datasets[0].data = pie_dataset;
  data.labels = chart_label;
  myPieChart.update();
});
$("#1").click(function() {
  var pie_dataset = [lastMonthScore, negLastMonthScore];
  var data = myPieChart.config.data;
  data.datasets[0].data = pie_dataset;
  data.labels = chart_label;
  myPieChart.update();
});
$("#2").click(function() {
  var pie_dataset = [avgMonthScore, negAvgMonthScore];
  var data = myPieChart.config.data;
  data.datasets[0].data = pie_dataset;
  data.labels = chart_label;
  myPieChart.update();
});