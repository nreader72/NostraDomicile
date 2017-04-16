$(document).ready(function(){
	$('[data-toggle="popover"]').popover();
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
    $scope.message = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, ';
});

app.controller('helpController', function($scope) {
    $scope.message1 = 'NostraDomicile offers three primary functions: "Will Your House Sell?", "Most Important Attributes", and "Data Visualizations".'
	+ 'In order to fulfill the goal of these functions some input is needed.  For the "Will Your House Sell?" function both the Zip Code' +
	    'and your home''s attributes are required.  For the other two functions only the Zip Code of interest is required.';
    $scope.message2 = 'The submit buttons for the primary functions will not work until the proper input has been entered.';
    $scope.message3 = 'Thank you for using NostraDomicile, if you have any questions or concerns feel free to email us through the Contact Us Section.';
});


app.controller('selectboxCtrl', function ($scope) {
    $scope.bedrooms = [{
	value: '0',
	text: 'Bedrooms'
    }, {
        value: '1',
	text:'1'
    }, {
        value: '2',
	text: '2'
    }, {
       	value: '3',
	text: '3'
    }, {
       	value: '4',
	text: '4'
    }, {
        value: '5',
	text: '5'
    }, {
        value: '6',
	text: '6'
    }];
    $scope.checkselection = function () {
        if ($scope.userSelect1 != "" && $scope.userSelect1 != undefined)
            $scope.msg = 'Selected Value: ' + $scope.userSelect1;
        else
            $scope.msg = 'Please Select Dropdown Value';
    };
    $scope.bathrooms = [{
       	value: '0',
	text: 'Bathrooms'
    }, {
	value: '1',
	text: '1'
    }, {
        value: '2',
	text: '1.5'
    }, {
	value: '3',
        text: '2'
    }, {
	value: '4',
        text: '2.5'
    }, {
        value: '5',
	text: '3'
    }, {
        value: '6',
	text: '3.5'
    }, {
        value: '7',
	text: '4'
    }, {
        value: '8',
	text: '4.5'
    }, {
        value: '9',
	text: '5'
    }, {
        value: '10',
	text: '5.5'
    }, {
        value: '11',
	text: '6'
    }];

    $scope.checkselection = function () {
        if ($scope.userselect2 != "" && $scope.userSelect2 != undefined)
                $scope.msg = 'Selected Value: ' + $scope.userSelect2;
        else 
                $scope.msg = 'Please Select a Dropdown Value';
    };

    $scope.stories = [{
	value: '0',
	text: 'Story'
    }, {
	value: '1',
	text: '1'
    }, {
	value: '2',
	text: '2'
    }, {
	value: '3',
	text:  '3'
    }, {
	value: '4',
	text: '4'
    }];

    $scope.checkselection = function () {
        if ($scope.userSelect3 != "" && $scope.userSelect3 != undefined)
            $scope.msg = 'Selected Value: ' + $scope.userSelect3;
        else
            $scope.msg = 'Please Select Dropdown Value';
    };

    $scope.TypeList = [{
	value: '0',
	text: 'Type'
    }, {
        value: '1',
	text: 'Unknown'
    }, {
	value: '2',
        text: 'SingleFamily'
    }, {
	value: '3',
        text: 'Duplex'
    }, {
	value: '4',
        text: 'Triplex'
    }, {
	value: '5',
        text: 'Quadruplex'
    }, {
	value: '6',
        text: 'Condominium'
    }, {
	value: '7',
        text: 'Cooperative'
    }, {
	value: '8',
        text: 'Mobile'
    }, {
	value: '9',
        text: 'MultiFamily2To4'
    }, {
	value: '10',
        text: 'MultiFamily5Plus'
    }, {
	value: '11',
        text: 'Timeshare'
    }, {
	value: '12',
        text: 'Miscellaneous'
    },{
	value: '13',
        text: 'VacantResidentialLand'
    }];
    $scope.checkselection = function () {
        if ($scope.userSelect4 != "" && $scope.userSelect4 != undefined)
            $scope.msg = 'Selected Value: ' + $scope.userSelect4;
        else
            $scope.msg = 'Please Select Dropdown Value';
    };

    $scope.ParkingList = [{
	value: '0',
	text: 'Parking'
    }, {
	value: '1',
        text: 'Garage-Attached'
    }, {
	value: '2',
        text: 'Carport'
    }, {
	value: '3',
        text: 'Off-street'
    }, {
	value: '4',
        text: 'Garage-Detached'
    }, {
	value: '5',
       	text: 'None'

    }];

    $scope.checkselection = function () {
        if ($scope.userselect5 != "" && $scope.userSelect5 != undefined)
                $scope.msg = 'Selected Value: ' + $scope.userSelect5;
        else 
                $scope.msg = 'Please Select a Dropdown Value';
    };

	//

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




