/**
 * Created by punto on 3/12/2017.
 */
var app = angular.module("NostraDomicile", ["ngRoute"]);

app.controller('mainController', ['$scope', 'mainController']);

var mainController = function ($scope) {
    $scope.zipCode =  {zip_code: 'Zip Code'};
};

app.config(function($routeProvider) {
    $routeProvider

    // route for the home page
       /* .when('/', {
            templateUrl : 'pages/home.html',
            controller  : 'homeController'
        })
*/
        // route for the about page
        .when('/about', {
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
        });
});

// create the controller and inject Angular's $scope
/*app.controller('homeController', function($scope) {
    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});*/

app.controller('aboutController', function($scope) {
    $scope.message = 'The goal of the NostraDomicile Project is to create a web application whose two main functions ' +
        'are to predict whether a house will sell in a specific area based on the home’s attributes, and given a zip ' +
        'code, what are the most important factors leading to a sale in that area.'  +
        ' \n\n ' +
        '\nNostraDomicile will accomplish this' +
        ' goal by retrieving and storing housing market information using a Zillow API and MySQL database, using ' +
        'machine learning to evaluate housing data and determine factors influencing home sales in a particular area,' +
        ' and creating a user-friendly interface for users to view data about factors influencing home sales and ' +
        'create data visualizations about houses on the market based on user preferences';
});

app.controller('contactController', function($scope) {
    $scope.message = 'BLAH BLAH BLAH BLAH BLAH EMAIL FORM BLAH BLAH BLAH';
});

app.controller('blogController', function($scope) {
    $scope.message = 'BLOG BLOG BLOG BLOG BLOG BLOG BLOG BLOG BLOG';
});



app.controller('selectboxCtrl', function ($scope) {
    $scope.BedroomList = [{
        "bedroom": 6
    }, {
        "bedroom": 5
    }, {
        "bedroom": 4
    }, {
        "bedroom": 3
    }, {
        "bedroom": 2
    }, {
        "bedroom": 1
    }];
    $scope.checkselection = function () {
        if ($scope.userSelect1 != "" && $scope.userSelect1 != undefined)
            $scope.msg = 'Selected Value: ' + $scope.userSelect1;
        else
            $scope.msg = 'Please Select Dropdown Value';
    };
    $scope.BathroomList = [{
        "bathroom": 6
    }, {
        "bathroom": 5.5
    }, {
        "bathroom": 5
    }, {
        "bathroom": 4.5
    }, {
        "bathroom": 4
    }, {
        "bathroom": 3.5
    }, {
        "bathroom": 3
    }, {
        "bathroom": 2.5
    }, {
        "bathroom": 2
    }, {
        "bathroom": 1.5
    }, {
        "bathroom": 1
    }];
    $scope.checkselection = function () {
        if ($scope.userSelect2 != "" && $scope.userSelect2 != undefined)
            $scope.msg = 'Selected Value: ' + $scope.userSelect2;
        else
            $scope.msg = 'Please Select Dropdown Value';
    };

    $scope.TypeList = [{
        "type": "Unknown"
    }, {
        "type": "SingleFamily"
    }, {
        "type": "Duplex"
    }, {
        "type": "Triplex"
    }, {
        "type": "Quadruplex"
    }, {
        "type": "Condominium"
    }, {
        "type":  "Cooperative"
    }, {
        "type": "Mobile"
    }, {
        "type": "MultiFamily2To4"
    }, {
        "type": "MultiFamily5Plus"
    }, {
        "type": "Timeshare"
    }, {
        "type": "Miscellaneous"
    },{
        "type": "VacantResidentialLand"
    }];
    $scope.checkselection = function () {
        if ($scope.userSelect2 != "" && $scope.userSelect2 != undefined)
            $scope.msg = 'Selected Value: ' + $scope.userSelect2;
        else
            $scope.msg = 'Please Select Dropdown Value';
    };

    $scope.ParkingList = [{
        "parking": "Garage-Attached"
    }, {
        "parking": "Carport"
    }, {
        "parking": "Off-street"
    }, {
        "parking": "Garage-Detached"
    }, {
        "parking": "None"

    }];
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




