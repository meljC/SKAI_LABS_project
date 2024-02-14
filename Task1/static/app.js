function displayPolygon() {
    fetch('/polygon')
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        // Extract the polygon coordinates from the data
        var coordinates = data.polygon;
        // Convert the coordinates to the format OpenLayers expects ([[[lon, lat], ...]])
        var transformedCoordinates = [coordinates.map(coord => ol.proj.fromLonLat(coord))];
        
        // Create a polygon feature
        var polygonFeature = new ol.Feature({
          geometry: new ol.geom.Polygon(transformedCoordinates)
        });
        
        var vectorSource = new ol.source.Vector({
          features: [polygonFeature]
        });
        var vectorLayer = new ol.layer.Vector({
          source: vectorSource,
          style: new ol.style.Style({
            fill: new ol.style.Fill({
                color: 'rgba(255, 0, 0, 0.5)' // Red fill with some transparency
            }),
            stroke: new ol.style.Stroke({
                color: '#ff0000', // Red stroke
                width: 2
            })
          })
        });
        
        var map = new ol.Map({
          target: 'map',
          layers: [
            new ol.layer.Tile({
              source: new ol.source.OSM()
            }),
            vectorLayer
          ],
          view: new ol.View({
            center: ol.proj.fromLonLat([0, 0]), // Adjusted below
            zoom: 2 // Adjusted below
          })
        });
        
        // Fit the map view to the polygon extent
        map.getView().fit(vectorSource.getExtent(), {padding: [100, 100, 100, 100]});
      });
  }
  
  displayPolygon();
  