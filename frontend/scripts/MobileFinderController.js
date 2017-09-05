app.controller('MobileFinderController',['$scope',function($scope){
  //Price Slider
  $scope.PriceSlider = {
    minValue: 500,
    maxValue: 30000,
    options: {
      floor: 0,
      ceil: 100000,
      step: 5000,
      showTicks: false,
      showSelectionBar: true,
      getPointerColor: function(value){return '#0275d8';},
      selectionBarGradient: {
        from: 'white',
        to: 'red'
      },
      translate: function(value, sliderId, label) {
        switch (label) {
          case 'model':
          	if(value == 0)
          		return 'Min';
            	return '₹' + value;
          case 'high':
          	if(value == 100000)
          		return 'Max';
            return '₹' + value;
          default:
            return ''
        }
      }
    }
  };

  //Rating Slider
  $scope.RatingSlider = {
  	value: 1,
    	options: {
  	    
  	    showTicks:true,
  	    showTicksValues: false,
  	    stepsArray: [
  	      
  	      {value: 1, legend: 'Fair'},
  	      {value: 2, legend: 'Average'},
  	      {value: 3, legend: 'Good'},
  	      {value: 4, legend: 'Best'}
  	    ],
  	    //The color coding is not working as expected. Might be a BUG!
  	    getTickColor: function (value) {
              if (value == 1)
                return '#ffad18';
              if (value == 2)
                return '#0ee027';
              if (value == 3)
                return 'Green';
              return 'Red';
          },
          showSelectionBar: true,
          getSelectionBarColor: function(value) {
              if (value == 1)
                return 'red';
              if (value == 2)
                return '#ffad18';
              if (value == 3)
                return '#0ee027';
              return 'green';
          }
    }
  };
}])