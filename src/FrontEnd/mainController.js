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
            templateUrl : 'pages/about.html',
            controller  : 'aboutController'
        })

        .when('/blog', {
            templateUrl : 'pages/blog.html',
            controller  : 'blogController'
        })

        // route for the contact page
        .when('/contact', {
            templateUrl : 'pages/contact.html',
            controller  : 'contactController'
        });
});

// create the controller and inject Angular's $scope
/*app.controller('homeController', function($scope) {
    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});*/

app.controller('aboutController', function($scope) {
    $scope.message = 'BLAH BLAH BLAH BLAH BLAH BLAH BLAH';
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



app.controller('SubjectDropDownController', function ($scope) {

    $scope.subjects = ['Math', 'Physics', 'Chemistry', 'Hindi', 'English'];
    $scope.selectedItem;
    $scope.dropboxitemselected = function () {

        $scope.selectedItem = item;
        alert("drop box item selected");
    }
});

