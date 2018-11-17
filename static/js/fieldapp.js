var mdiscusdistance = []

var wdiscusdistance = []

var wshotdistance = []

var mshotdistance = []

d3.csv("../../db/MensDiscus.csv", function(mdiscus) {
  mdiscusdistance.push(mdiscus.avg_medalists);
});
d3.csv("../../db/WomensDiscus.csv", function(wdiscus) {
  wdiscusdistance.push(wdiscus.avg_medalists);
});

d3.csv("../../db/Womens shotput.csv", function(wshot) {
  wshotdistance.push(wshot.avg_medalists);
});

d3.csv("../../db/mshot.csv", function(mshot) {
  mshotdistance.push(mshot.avg_medalists);
});

setTimeout(function(){
  makeCharts();
}, 1000);

function makeCharts() {

console.log(mdiscusdistance);
var mensDiscus = {
  r: mdiscusdistance.reverse(),
  t: ['Rome 1960','Tokyo 1964','Mexico City 1968', 'Munich 1972','Montreal 1976','Moscow 1980','Los Angeles 1984','Seoul 1988','Barcelona 1992','Atlanta 1996','Sydney 2000','Athens 2004','Beijing 2008','London 2012','Rio 2016'],
  mode: 'markers',
  name: 'Trial 1',
  marker: {
    color: 'blue',
    size: 300,
    line: {color: 'blue'},
    opacity: 0.75
  },
  type: 'scatter'
};

var womensDiscus = {
  r: wdiscusdistance,
  t: ['Rome 1960','Tokyo 1964','Mexico City 1968', 'Munich 1972','Montreal 1976','Moscow 1980','Los Angeles 1984','Seoul 1988','Barcelona 1992','Atlanta 1996','Sydney 2000','Athens 2004','Beijing 2008','London 2012','Rio 2016'],
  mode: 'markers',
  name: 'Trial 2',
  marker: {
    color: 'pink',
    size: 300,
    line: {color: 'pink'},
    opacity: 0.75
  },
  type: 'scatter'
};

var discusData = [mensDiscus, womensDiscus];

var layout = {
  width: 900,
  height: 900,
  title: 'Discus Results',
  font: {size: 20},
  plot_bgcolor: '#3d7d00',
  angularaxis: {tickcolor: 'white'},
  hovermode: false,
  radialaxis: {
    visible: true,
    color: 'white',
    range: [50, 75],
  }
};
Plotly.plot('plot1', discusData, layout);

var mensShot = {
  r: mshotdistance,
  t: ['Rome 1960','Tokyo 1964','Mexico City 1968', 'Munich 1972','Montreal 1976','Moscow 1980','Los Angeles 1984','Seoul 1988','Barcelona 1992','Atlanta 1996','Sydney 2000','Athens 2004','Beijing 2008','London 2012','Rio 2016'],
  mode: 'markers',
  name: 'Trial 1',
  marker: {
    color: 'blue',
    size: 300,
    line: {color: 'blue'},
    opacity: 0.75
  },
  type: 'scatter'
};

var womensShot = {
  r: wshotdistance,
  t: ['Rome 1960','Tokyo 1964','Mexico City 1968', 'Munich 1972','Montreal 1976','Moscow 1980','Los Angeles 1984','Seoul 1988','Barcelona 1992','Atlanta 1996','Sydney 2000','Athens 2004','Beijing 2008','London 2012','Rio 2016'],
  mode: 'markers',
  name: 'Trial 2',
  marker: {
    color: 'pink',
    size: 300,
    line: {color: 'pink'},
    opacity: 0.75
  },
  type: 'scatter'
};

var shotputData = [mensShot, womensShot];

var layout = {
  width: 900,
  height: 900,
  title: 'Shot Put Results',
  font: {size: 20},
  plot_bgcolor: '#3d7d00',
  angularaxis: {tickcolor: 'white'},
  hovermode: false,
  radialaxis: {
    visible: true,
    color: 'white',
    range: [16, 23],
  }
};
Plotly.plot('plot2', shotputData, layout);
}