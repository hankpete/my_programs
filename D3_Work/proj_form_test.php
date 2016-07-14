<!DOCTYPE html>
<html>
<head>
  <title>D3 Test</title>
</head>
<body>
  <div id="dom-target" style="display: none;">
    <?php
      $cats = ["elev", "Temp", "TempC", "Dewp"];
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
  <script>
    var div = document.getElementById("dom-target");
    var myData = div.textContent;
    console.log(myData);
    var categories = ["elev", "Temp", "TempC", "Dewp", "Relh",
				"Winds", "SLP", "Altimeter", "Visibility", "TempHi24",
				"TempLo24", "RelhHi24", "RelhLo24", "GustHi24",
				"RawsTemp12", "RawsTemp13", "RawsTemp14", "RawsRelh12",
				"RawsRelh13", "RawsRelh14"];

    var newCat = [];
    for (var i = 0; i < categories.length; i++) {
      if (myData.indexOf(categories[i]) >= 0) {
        newCat.push(categories[i]);
      }
    }
  </script>
</body>
</html>
