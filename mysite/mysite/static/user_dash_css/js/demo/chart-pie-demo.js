// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var score = parseInt(document.getElementById("score").value);
console.log(score);
var negscore = 100 - score;
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Positive", "Negative"],
    datasets: [{
      data: [score, negscore],
      backgroundColor: ['#1565c0', '#f4b30d'],
      hoverBackgroundColor: ['#3f81cb', '#f6c039'],
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
    cutoutPercentage: 70,
  },
});

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

      var text = score + "%",
        textX = Math.round((width - ctx.measureText(text).width) / 2),
        textY = height / 2;

      ctx.fillText(text, textX, textY);
      ctx.save();
    }
  }
});
