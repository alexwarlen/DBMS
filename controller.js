google.charts.load("visualization", "1", {packages:['corechart']});

var longStrings = new Array();
longStrings['Stress'] = "Percentage of Low Job Stress";
longStrings['Satisfaction'] = "Percentage of High Job Satisfaction";
longStrings['Meaning'] = "Percentage with High Job Meaning";
longStrings['Median'] = "Typical Median Pay";

var xQuery = 'Stress';
var yQuery = 'Satisfaction';
var bubbleQuery = 'CEO';
var visualization;
var title = String(longStrings['Stress']) + ' vs. ' + String(longStrings['Satisfaction']);
var xAxis = {title: 'Percentage of Company with Low Job Stress'};
var yAxis = {title: 'Percentage of Company High Job Satisfaction'};


var namespace = namespace || {};

namespace.module = {};

namespace.module = function() {
	
	namespace.module.onSubmit = function() {
		var x = document.getElementById('x-axis');
		xQuery = x.options[x.selectedIndex].value;
		xAxis = {title: String(longStrings[xQuery])};
		
		var y = document.getElementById('y-axis');
		yQuery = y.options[y.selectedIndex].value;
		yAxis = {title: String(longStrings[yQuery])};
		title = String(longStrings[xQuery]) + ' vs. ' + String(longStrings[yQuery]);
		
		var z = document.getElementById('bubbledata');
		bubbleQuery = z.options[z.selectedIndex].value;
		
	}
	
	namespace.module.drawVisualization = function() {
		var query = new google.visualization.Query(
												   'https://www.google.com/fusiontables/gvizdata?tq=');
		
		console.log('xQuery is ' + xQuery);
		console.log('yQuery is ' + yQuery);
		// Apply query language.
		query.setQuery('SELECT Name, ' + xQuery + ', ' + yQuery + ' , Sector,' +  bubbleQuery +
					   ' FROM 1_ZO3XZ_dB0S2-y-CgdUZ6yHSkgvmlWtPOTwjYtVr WHERE Stress > 0' );
		
		// Send the query with a callback function.
		query.send(namespace.module.handleQueryResponse);
	}
	
	namespace.module.handleQueryResponse = function (response) {
		if (response.isError()) {
			alert('Error in query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
			return;
		}
		var options = {
		title: title,
		hAxis: xAxis,
		vAxis: yAxis,
		bubble: {
		textStyle: {
		auraColor: 'none',
		fontSize: .25,
		}
		}
		};
		
		var data = response.getDataTable();
		visualization = new google.visualization.BubbleChart(document.getElementById('visualization'));
		visualization.draw(data, options);
	}
};

namespace.module();

google.charts.setOnLoadCallback(namespace.module.drawVisualization);
