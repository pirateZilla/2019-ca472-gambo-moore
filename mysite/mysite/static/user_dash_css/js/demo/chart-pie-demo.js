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
    elements: {
				center: {
					text: pie_dataset[0] + "%",
          color: '#5a5c69', // Default is #000000
          fontStyle: 'Roboto', // Default is Arial
          sidePadding: 20 // Defualt is 20 (as a percentage)
				}
			}
  },
};

var myPieChart = new Chart(ctx, config);


Chart.pluginService.register({
  beforeDraw: function (chart) {
    if (chart.config.options.elements.center) {
      //Get ctx from string
      var ctx = chart.chart.ctx;
      
      //Get options from the center object in options
      var centerConfig = chart.config.options.elements.center;
      var fontStyle = centerConfig.fontStyle || 'Arial';
      var txt = centerConfig.text;
      var color = centerConfig.color || '#000';
      var sidePadding = centerConfig.sidePadding || 20;
      var sidePaddingCalculated = (sidePadding/100) * (chart.innerRadius * 2)
      //Start with a base font of 30px
      ctx.font = "30px " + fontStyle;
      
      //Get the width of the string and also the width of the element minus 10 to give it 5px side padding
      var stringWidth = ctx.measureText(txt).width;
      var elementWidth = (chart.innerRadius * 2) - sidePaddingCalculated;

      // Find out how much the font can grow in width.
      var widthRatio = elementWidth / stringWidth;
      var newFontSize = Math.floor(30 * widthRatio);
      var elementHeight = (chart.innerRadius * 2);

      // Pick a new font size so it will not be larger than the height of label.
      var fontSizeToUse = Math.min(newFontSize, elementHeight);

      //Set font settings to draw it correctly.
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      var centerX = ((chart.chartArea.left + chart.chartArea.right) / 2);
      var centerY = ((chart.chartArea.top + chart.chartArea.bottom) / 2);
      ctx.font = fontSizeToUse+"px " + fontStyle;
      ctx.fillStyle = color;
      
      //Draw text in center
      ctx.fillText(txt, centerX, centerY);
    }
  }
});




$("#0").click(function() {
  var data = myPieChart.config.data;
  var options = myPieChart.config.options;
  data.datasets[0].data = pie_dataset;
  data.labels = chart_label;
  options.elements.center.text = pie_dataset[0] + "%";
  myPieChart.update();
});
$("#1").click(function() {
  var pie_dataset = [lastMonthScore, negLastMonthScore];
  var data = myPieChart.config.data;
  var options = myPieChart.config.options;
  data.datasets[0].data = pie_dataset;
  data.labels = chart_label;
  options.elements.center.text = pie_dataset[0] + "%";
  myPieChart.update();
});
$("#2").click(function() {
  var pie_dataset = [avgMonthScore, negAvgMonthScore];
  var data = myPieChart.config.data;
  var options = myPieChart.config.options;
  data.datasets[0].data = pie_dataset;
  data.labels = chart_label;
  options.elements.center.text = pie_dataset[0] + "%";
  myPieChart.update();
});