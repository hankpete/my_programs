<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>D3 Test</title>
	<script src="d3/d3.min.js"></script>
	<script src="d3/topojson.min.js"></script>
	<style>
		* {
			margin: 0;
			padding: 0;
		}

		body {
			background-color: #eee;
		}

		svg {
			position: absolute;
			width: 100%;
			height: 100%;
		}

		.background {
			fill: #eee;
			pointer-events: all;
		}

		#zones {
			fill: #555;
		}

		#zones .active {
			fill: #55a;
		}

		#zone-borders {
		  fill: none;
		  stroke: #fff;
		  stroke-width: 1px;
		  stroke-linejoin: round;
		  stroke-linecap: round;
		  pointer-events: none;
	    }

		#ids {
			fill: #fff;
			font-family: helvetica;
			font-size: 10px;
			text-anchor: middle;
			opacity: .75;
		}

		#moused-zone {
			fill: #5a5;
		}

		.category-text {
			font-family: Roboto;
			fill: #55f;
			font-size: 36px;
		}

		.min-text, .max-text {
			font-family: Roboto;
			fill: black;
			font-size: 15px;
		}
	</style>
</head>
<body>

	<div id="category-div" style="display: none;">
    <?php
      $cats = ["elev", "Temp", "TempC", "Dewp", "Relh",
					"Winds", "SLP", "Altimeter", "Visibility", "TempHi24",
					"TempLo24", "RelhHi24", "RelhLo24", "GustHi24",
					"RawsTemp12", "RawsTemp13", "RawsTemp14", "RawsRelh12",
					"RawsRelh13", "RawsRelh14"];
      $catsLength = count($cats);

      for ($i = 0; $i < $catsLength; $i++)
      {
        if( $_GET[ $cats[$i] ] == $cats[$i] )
        {
          echo htmlspecialchars($cats[$i]);
        }
      }
    ?>
	</div>

	<div id="radius-div" style="display: none;">
		<?php
			$radius = $_GET[ "radius" ];
			echo "<p>";
			echo htmlspecialchars($radius);
			echo "</p>";
		?>
	</div>

	<div id="dt-div" style="display: none;">
		<?php
			$dt = $_GET[ "dt" ];
			echo "<p>";
			echo htmlspecialchars($dt);
			echo "</p>";
		?>
	</div>

	<div id="delay-div" style="display: none;">
		<?php
			$delay = $_GET[ "delay" ];
			echo "<p>";
			echo htmlspecialchars($delay);
			echo "</p>";
		?>
	</div>

	<script>
		//begin by getting the variables put into DOM by form/php

		//set categories variable from the form
		var div = document.getElementById("category-div");
		var myData = div.textContent;

		var allCategories = ["elev", "Temp", "TempC", "Dewp", "Relh",
				"Winds", "SLP", "Altimeter", "Visibility", "TempHi24",
				"TempLo24", "RelhHi24", "RelhLo24", "GustHi24",
				"RawsTemp12", "RawsTemp13", "RawsTemp14", "RawsRelh12",
				"RawsRelh13", "RawsRelh14"];

		var categories = [];
		for (var i = 0; i < allCategories.length; i++) {
			if (myData.indexOf(allCategories[i]) >= 0) {
				categories.push(allCategories[i]);
			}
		}
		//set radius variable from the form
		div = document.getElementById("radius-div");
		var radius = +div.children[0].textContent;

		//set dt variable from the form
		div = document.getElementById("dt-div");
		var dt = +div.children[0].textContent;

		//set delay variable from the form
		div = document.getElementById("delay-div");
		var delay = +div.children[0].textContent;


		//set up variables and functions we will need
		var width = window.innerWidth,
			height = window.innerHeight;

		var projectionFunc = d3.geo.mercator()	//world
			.scale(7000)
			.center([-119.6, 36.3])	//hnx coords
			.translate([width/2, height/2]);

		var pathFunc = d3.geo.path()
			.projection(projectionFunc);

		var svg = d3.select("body").append("svg")
			.attr("width", width)
			.attr("height", height);

		//get hnx map data and plot it
		d3.json("hnxSaZones.json", function(error, hnx) {
			if (error) throw error;

			var zones = topojson.feature(hnx, hnx.objects.hnxsaZones).features;
			svg.selectAll("path")
					.data(zones)
				.enter()
					.append("path")
					.attr("id", "zones")
					.attr("d", pathFunc);

			//make borders separately so they dont slow it down
			svg.append("path")
		        .datum(topojson.mesh(hnx, hnx.objects.hnxsaZones, function(a, b) {
				    return a !== b;
			    }))
		        .attr("id", "zone-borders")
		        .attr("d", pathFunc);

			//label zones
			svg.selectAll("text")
				.data(zones)
			  .enter().append("text")
			  	.attr("id", "ids")
				.attr("x", function(d) {
					return projectionFunc([d.properties.LON, d.properties.LAT])[0];
				})
				.attr("y", function(d) {
					return projectionFunc([d.properties.LON, d.properties.LAT])[1];
				})
				.text(function(d) {
					return d.properties.ZONE;
				});
		});

//////////////////////////////////////////////////////////////
///				main vis 																			//////
///////////////////////////////////////////////////////////////
		//main loop
		var index = 0;
		main();


		function main() {
			//put all the vis on the svg, make the heatmap, cycle through
			//changing opacity on the categories selected (default all)
			//get the data and run initialize() for each category
			var dataUrl = "ba-simple-proxy/ba-simple-proxy.php?url=http://www.wrh.noaa.gov/hnx/JimBGmwXJList.php?extents=34.74,-121.4,38.36,-117.62&mode=native";
			d3.json(dataUrl, function(error, data) {
				if (error) { console.log("There was an error loading the data." + error); }

				for (var i = 0; i < categories.length; i++) {
					initialize(data.stations, categories[i])
				}
			});
			makeLegend();
			cycle();
			index++;
			setInterval(function() {
						cycle();
						index++;
					}, 2*dt + delay);
		}


		function makeLegend() {
			//make a heatmap bar to show what the data represents
			var numRects = 100;
			var rectsData = [];
			for (var i = 0; i < numRects; i++) {
				rectsData.push(i);
			}
			var textHeight = height/15;
			var categoryTextWidth = width/4;
			var colorScale = d3.scale.linear()
					.domain([0, numRects - 1])
					.range([0, 255]);

			svg.selectAll("rect.heatmap")
					.data(rectsData)
				.enter()
					.append("rect")
					.attr("x", function(d, i) {
						return 2.2*categoryTextWidth + i*(.75*categoryTextWidth/numRects);
					})
					.attr("y", textHeight/2)
					.attr("width", categoryTextWidth/numRects)
					.attr("height", textHeight/2)
					.attr("fill", function(d) {
						var num = Math.round(colorScale(d));
						return "rgb(" + num + ", 0, " + (255 - num) + ")";
					});
		}


		function cycle() {
			//pick next data category, make it opacity 1 and the
			//one before it opacity 0 in a smooth transition
			var nextCategory = categories[index % categories.length];
			var previousCategory = categories[(index-1) % categories.length];

			svg.selectAll("#" + previousCategory)		//above
				.transition()
					.duration(dt)
					.style("opacity", 0);

			svg.selectAll("#" + nextCategory)		//below
				.transition()
					.duration(dt)
					.style("opacity", 1);
		}


		function average(data) {
			//returns mean of data
			var sum = 0;
			for (var i = 0; i < data.length; i++) {
				sum += data[i];
			}
			var average = sum/data.length;
			return average;
		}


		function initialize(dataFull, name) {
			//from the data, plot the heatmapped dots in their
			//coordinates and start them off opacity 0.
			//also display some text for what the colors mean
			//and what the data is about
			var dataList = [];
			var newNum;
			for (var i = 0; i < dataFull.length; i++) {
				newNum = eval("dataFull[i]." + name);
				if (typeof newNum == "string" && newNum != "") {
					dataList.push( parseFloat(newNum) );
				}
			}

			var avg = average(dataList);

			var diffs = [];
			for (var i = 0; i < dataList.length; i++) {
				diff = Math.abs(dataList[i] - avg)
				diffs.push( Math.pow(diff, 2) );
			}
			var sum = 0;
			for (var i = 0; i < diffs.length; i++) {
				sum += diffs[i];
			}
			var stdv = Math.sqrt(sum/diffs.length);

			dataList.sort( function(a, b) { return a-b; });

			for (var i = 0; i < dataList.length; i++) {
				if (dataList[i] > (avg - 3*stdv)) {
					var min = dataList[i];
					break;
				}
			}
			for (var i = 0; i < dataList.length; i++) {
				if (dataList[dataList.length - i - 1] < (avg + 3*stdv)) {
					var max = dataList[dataList.length - i - 1];
					break;
				}
			}

			var colorScale = d3.scale.linear()
					.domain([min, max])
					.range([0, 255]);

			// var radiusScale =	d3.scale.linear()
			// 				.domain([min, max])
			// 				.range([2, 10]);

			//display name of category
			var textHeight = height/15;
			var categoryTextWidth = width/4;
			var text = svg.selectAll("text#" + name + ".category-text")
					.data([0]);

			text
				.enter()
					.append("text")
					.attr("class", "category-text")
					.attr("id", name)
					.attr("x", categoryTextWidth)
					.attr("y", textHeight)
					.text(name)
					.style("opacity", 0);

			text
					.text(name);

			//show a legend for the color map
			var minText = svg.selectAll("text#" + name + ".min-text")
					.data([0]);

			minText
				.enter()
					.append("text")
					.attr("class", "min-text")
					.attr("id", name)
					.attr("x", 2*categoryTextWidth)
					.attr("y", textHeight)
					.text(min)
					.style("opacity", 0);

			minText
				.text(min);

			var maxText = svg.selectAll("text#" + name + ".max-text")
					.data([0]);

			maxText
				.enter()
					.append("text")
					.attr("class", "max-text")
					.attr("id", name)
					.attr("x", 3*categoryTextWidth)
					.attr("y", textHeight)
					.text(max)
					.style("opacity", 0);

			maxText
				.text(max);

			//add data vis with class 'name' and opacity 0
			var circs = svg.selectAll("circle." + name)
					.data(dataFull);

			circs
				.enter()
					.append("circle")
					.attr("class", function(d) {
						if (eval("d." + name)) {
							return name;
						} else {
							return "undefined";
						}
					})
					.attr("id", name)
					.attr("cx", function(d) {
						return projectionFunc([d.longitude, d.latitude])[0]
					})
					.attr("cy", function(d) {
						return projectionFunc([d.longitude, d.latitude])[1]
					})
					// .attr("r", function(d) {
					// 	return radiusScale(eval("d." + name));
					// })
					.attr("r", radius)
					.attr("fill", function(d) {
						var num = Math.round(colorScale(eval("d." + name)));
						if (num < 0 || num > 255) {
							return "rgb(0, 0, 0)";
						}
						return "rgb(" + num + ", 0, " + (255 - num)+ ")";
					})
					.style("opacity", 0);

			circs
					.attr("class", function(d) {
						if (eval("d." + name)) {
							return name;
						} else {
							return "undefined";
						}
					})
					.attr("cx", function(d) {
						return projectionFunc([d.longitude, d.latitude])[0]
					})
					.attr("cy", function(d) {
						return projectionFunc([d.longitude, d.latitude])[1]
					})
					// .attr("r", function(d) {
					// 	return radiusScale(eval("d." + name));
					// })
					.attr("fill", function(d) {
						var num = Math.round(colorScale(eval("d." + name)));
						if (num < 0 || num > 255) {
							return "rgb(0, 0, 0)";
						}
						return "rgb(" + num + ", 0, " + (255 - num)+ ")";
					})
					.style("opacity", 0);

			circs
				.exit()
					.remove()

			//the ones that had no data
			svg.selectAll("circle.undefined")
					.remove();
		}


	</script>

</body>
</html>
