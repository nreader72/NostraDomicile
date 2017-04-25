$(document).ready(function(){
	$('[data-toggle="popover"]').popover();

	$('#loading').hide();
	jQuery.ajaxSetup({
		beforeSend: function() {
			$('#loading').show();
		},
		complete: function() {
			$('#loading').hide();
		},
		success: function() {}
	});
	$('#rf').on('submit', function(event) {
		event.preventDefault();
		submit_post();
	});

	function submit_post() {
		$('#status').hide();
		var form_data = {};
		form_data['zipCode'] = $('#zip').val();
		form_data['price'] = $('#price').val();
		form_data['sqft'] = $('#sqft').val();
		form_data['acreage'] = $('#acreage').val();
		form_data['year'] = $('#year').val();
		form_data['neighborhood'] = $('#neighborhood').val();
		form_data['school'] = $('#school').val();
		form_data['bedrooms'] = $('#bedroomSelect').val();
		form_data['bathrooms'] = $('#bathroomSelect').val();
		form_data['stories'] = $('#storiesSelect').val();
		form_data['home'] = $('#homeSelect').val();
		form_data['parking'] = $('#parkingSelect').val();
		form_data['csrfmiddlewaretoken'] = document.getElementsByName('csrfmiddlewaretoken')[0].value;
		$.ajax({
			url: "index.html",
			type: "POST",
			data: form_data,
			success: function(json) {
				//console.log(json);
				if (json['status'] == 'True') {
					$('#status').html('<div class="alert alert-success"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a><strong>Success!</strong> ' + json["message"] + '</div>');
					if (json["zip"] == 'True') {
						
						var features = json['attributes'].split(",");

						var features_trace = {
							x:[features[0], features[2], features[4], features[6], features[8], features[10], features[12]],
							y:[features[1], features[3], features[5], features[7], features[9], features[11]],
							type:'bar'
						};
						var feature_data = [features_trace];							
						
						$('#zip_body').html('The most important attributes leading to home sales in your area are:<br /><div id="features_vis" style="width:600px; height:600px;"></div>'); //json['attributes']);
						Plotly.plot('features_vis', feature_data);
						
						
						trace={
						   x:[1,2,3,12,3,7],
						   y:[1,2,3,4,5,13],
						   marker:{
						   color:['red','blue'],
						   size:[20,50,80]},
						   mode:'markers'};
						$('#visualization_body').html('<div id="vis" style="width:600px; height:250px;"></div>');
						   Plotly.plot('vis',[trace]);
						


						$('#attributes_feature_button').removeClass('btn-disabled');
						$('#zip_error').remove();
						var trace = {
							x:[5,8,5,1], 
							y:[1,2,4,8], 
							z:[11,8,15,3], 
							mode:'lines'
						};
						var data = [trace];
						$('#visualization_body').html('<div id="vis" style="width:600px; height:250px;"></div>');
						Plotly.plot('vis', data);
						
						//added new charts here
						
						//don't know what this is but don't want to cut it [10:11] 
						
						trace={
						   x:[1,2,3],
						   y:[1,2,3],
						   marker:{
						   color:['red','blue'],
						   size:[20,50,80]},
						   mode:'markers'};
						   $('#visualization_body').html('<div id="vis" style="width:600px; height:250px;"></div>');
						   Plotly.plot('vis',[trace]);
						
						$('#visualization_feature_button').removeClass('btn-disabled');
						$('#visualization_error').remove();
					} else {
						
					}
					if (json['factors'] == 'True') {
						alert('sold:' + json['sold']);
						$('#factors_body').html('Your home is predicted to __ based on the submitted data and the zip code you provided.');
						$('#sell_feature_button').removeClass('btn-disabled');
						$('#factors_error').remove();
					} else {

					}
				} else {
					$('#status').html('<div class="alert alert-danger"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a><strong>Error!</strong> There was an error submiting your data!</div>');
				}
				$('#status').show();
			},
			error: function(xhr, errmsg, err) {
				$('#status').html('<div class="alert alert-danger"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a><strong>Error!</strong> There was an error submitting your data!</div>');
			}
		});
		$('#zip').val('');
		$('#price').val('');
		$('#sqft').val('');
		$('#acreage').val('');
		$('#year').val('');
		$('#neighborhood').val('');
		$('#school').val('');

	}
});

var app = angular.module("NostraDomicile", ["ngRoute"]);

app.controller('mainController', ['$scope', 'mainController']);

var mainController = function ($scope) {
    $scope.zipCode =  {zip_code: 'Zip Code'};
};

app.config(function($routeProvider) {
    $routeProvider.when('/about', {
            templateUrl : 'static/about.html',
            controller  : 'aboutController'
        })

        .when('/blog', {
            templateUrl : 'static/blog.html',
            controller  : 'blogController'
        })

        // route for the contact page
        .when('/contact', {
            templateUrl : 'static/contact.html',
            controller  : 'contactController'
        })
	.when('/help', {
            templateUrl : 'static/help.html',
            controller  : 'helpController'
        });
});

app.controller('aboutController', function($scope) {
    $scope.message1 = 'The goal of the NostraDomicile Project is to create a web application whose two main functions ' +
        'are to predict whether a house will sell in a specific area based on the home’s attributes, and given a zip ' +

        'code, what are the most important factors leading to a sale in that area.';

     $scope.message2 =   'NostraDomicile will accomplish this' +

        ' goal by retrieving and storing housing market information using a Zillow API and MySQL database, using ' +

        'machine learning to evaluate housing data and determine factors influencing home sales in a particular area,' +

        ' and creating a user-friendly interface for users to view data about factors influencing home sales and ' +

        'create data visualizations about houses on the market based on user preferences';
});

app.controller('contactController', function($scope) {
    //$scope.message = 'BLAH BLAH BLAH BLAH BLAH EMAIL FORM BLAH BLAH BLAH';
});

app.controller('blogController', function($scope) {
    //$scope.message = '';
});

app.controller('helpController', function($scope) {

    $scope.message1 = 'NostraDomicile offers three primary functions: "Will Your House Sell?", "Most Important Attributes", and "Data Visualizations".'

	+ 'In order to fulfill the goal of these functions some input is needed.  For the "Will Your House Sell?" function both the Zip Code' +

	    'and your home\'s attributes are required.  For the other two functions only the Zip Code of interest is required.';

    $scope.message2 = 'The submit buttons for the primary functions will not work until the proper input has been entered.';

    $scope.message3 = 'Thank you for using NostraDomicile, if you have any questions or concerns feel free to email us through the Contact Us Section.';

});


app.controller('selectboxCtrl', function ($scope) {
    $scope.bedrooms = [{value: '0', text: 'Bedrooms'}, {value: '1', text:'1'}, {value: '2', text: '2'}, {value: '3', text: '3'}, {value: '4',text: '4'}, {value: '5',text: '5'}, {value: '6', text: '6'}];
    $scope.checkselection = function () {
        if ($scope.userSelect1 != "" && $scope.userSelect1 != undefined)
            $scope.msg = 'Selected Value: ' + $scope.userSelect1;
        else
            $scope.msg = 'Please Select Dropdown Value';
    };
    $scope.bathrooms = [{value: '0', text: 'Bathrooms'}, {value: '1', text: '1'}, {value: '1.5', text: '1.5'}, {value: '2', text: '2'}, {	value: '2.5', text: '2.5'}, {value: '3', text: '3'}, {value: '3.5', text: '3.5'}, {value: '4', text: '4'}, {value: '4.5', text: '4.5'}, {value: '5', text: '5'}, {value: '5.5', text: '5.5'}, {value: '6', text: '6'}];

    $scope.checkselection = function () {
        if ($scope.userselect2 != "" && $scope.userSelect2 != undefined)
                $scope.msg = 'Selected Value: ' + $scope.userSelect2;
        else 
                $scope.msg = 'Please Select a Dropdown Value';
    };

    $scope.stories = [{value: '0', text: 'Story'}, {value: '1',	text: '1'}, {value: '2', text: '2'}, {value: '3', text:  '3'}, {value: '4',	text: '4'}];

    $scope.checkselection = function () {
        if ($scope.userSelect3 != "" && $scope.userSelect3 != undefined)
            $scope.msg = 'Selected Value: ' + $scope.userSelect3;
        else
            $scope.msg = 'Please Select Dropdown Value';
    };

    $scope.TypeList = [{value: '0',	text: 'Type'}, {value: 'Unknown',	text: 'Unknown'}, {value: 'SingleFamily', text: 'SingleFamily'}, {value: 'Duplex', text: 'Duplex'}, {value: 'Triplex', text: 'Triplex'}, {value: 'Quadruplex', text: 'Quadruplex'}, {value: 'Condominium', text: 'Condominium'}, {value: 'Cooperative', text: 'Cooperative'}, {value: 'Mobile', text: 'Mobile'}, {value: 'MultiFamily2To4', text: 'MultiFamily2To4'}, {value: 'MultiFamily5Plus', text: 'MultiFamily5Plus'}, {value: 'Timeshare', text: 'Timeshare'}, {value: 'Miscellaneous', text: 'Miscellaneous'},{value: 'VacantResidentialLand', text: 'VacantResidentialLand'}];
    $scope.checkselection = function () {
        if ($scope.userSelect4 != "" && $scope.userSelect4 != undefined)
            $scope.msg = 'Selected Value: ' + $scope.userSelect4;
        else
            $scope.msg = 'Please Select Dropdown Value';

    };



    $scope.ParkingList = [{value: '0', text: 'Parking'}, {value: 'Garage-Attached', text: 'Garage-Attached'}, {value: 'Carport', text: 'Carport'}, {value: 'Off-street', text: 'Off-street'}, {value: 'Garage-Detached', text: 'Garage-Detached'}, {value: 'None',text: 'None'}];



    $scope.checkselection = function () {

        if ($scope.userselect5 != "" && $scope.userSelect5 != undefined)

                $scope.msg = 'Selected Value: ' + $scope.userSelect5;

        else 

                $scope.msg = 'Please Select a Dropdown Value';

    };



	//

/*
    $scope.result = 'hidden'
    $scope.resultMessage;
    $scope.rfData; //formData is an object holding the name, email, subject, and message
    $scope.submitButtonDisabled = false;
    $scope.submitted = false; //used so that form errors are shown only after the form has been submitted
    $scope.submit = function(rfForm) {
    $scope.submitted = true;
    $scope.submitButtonDisabled = true;
	if (contactform.$valid) {
            $http({
                method  : 'POST',
           	 url     : 'index.php',
           	 data    : $.param($scope.rfData),  //param method from jQuery
           	 headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  //set the headers so angular passing info as form data (not request payload)
        }).success(function(data){
                console.log(data);
                if (data.success) { //success comes from the return json object
                    $scope.submitButtonDisabled = true;
                    $scope.resultMessage = data.message;
                    $scope.result='bg-success';
                } else {
                    $scope.submitButtonDisabled = false;
                    $scope.resultMessage = data.message;
                    $scope.result='bg-danger';
                }
            });
        } else {
            $scope.submitButtonDisabled = false;
            $scope.resultMessage = 'Failed <img src="http://www.chaosm.net/blog/wp-includes/images/smilies/icon_sad.gif" alt=":(" class="wp-smiley">  Please fill out all the fields.';
            $scope.result='bg-danger';
        }
    }
*/
	//
});

app.controller('ContactController', function ($scope, $http) {
    $scope.result = 'hidden'
    $scope.resultMessage;
    $scope.formData; //formData is an object holding the name, email, subject, and message
    $scope.submitButtonDisabled = false;
    $scope.submitted = false; //used so that form errors are shown only after the form has been submitted
    $scope.submit = function(contactform) {
        $scope.submitted = true;
        $scope.submitButtonDisabled = true;
        if (contactform.$valid) {
            $http({
            method  : 'POST',
            url     : 'contact-form.php',
            data    : $.param($scope.formData),  //param method from jQuery
            headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  //set the headers so angular passing info as form data (not request payload)
        }).success(function(data){
                console.log(data);
                if (data.success) { //success comes from the return json object
                    $scope.submitButtonDisabled = true;
                    $scope.resultMessage = data.message;
                    $scope.result='bg-success';
                } else {
                    $scope.submitButtonDisabled = false;
                    $scope.resultMessage = data.message;
                    $scope.result='bg-danger';
                }
            });
        } else {
            $scope.submitButtonDisabled = false;
            $scope.resultMessage = 'Failed <img src="http://www.chaosm.net/blog/wp-includes/images/smilies/icon_sad.gif" alt=":(" class="wp-smiley">  Please fill out all the fields.';
            $scope.result='bg-danger';

        }

    }

});





