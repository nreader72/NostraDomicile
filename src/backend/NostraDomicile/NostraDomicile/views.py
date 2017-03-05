from django.http import HttpResponse

def index(request):
	text = """
<!DOCTYPE html>
<html lang="en">

<head>
  <title>NostraDomicile</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
  body {
      font: 20px Montserrat, sans-serif;
      line-height: 1.8;
      color: #f5f6f7;
  }

  p {font-size: 16px;}

  .margin {margin-bottom: 45px;}

  .bg-1 { 
      background-color: #1abc9c; /* Green */
      color: #ffffff;
  }

  .bg-2 { 
      background-color: #474e5d; /* Dark Blue */
      color: #ffffff;
  }

  .bg-3 { 
      background-color: #ffffff; /* White */
      color: #555555;
  }

  .bg-4 { 
      background-color: #2f2f2f; /* Black Gray */
      color: #fff;
  }

  .container-fluid {
      padding-top: 70px;
      padding-bottom: 70px;
  }

  .navbar {
      padding-top: 15px;
      padding-bottom: 15px;
      border: 0;
      border-radius: 0;
      margin-bottom: 0;
      font-size: 12px;
      letter-spacing: 5px;
  }

  .navbar-nav  li a:hover {
      color: #1abc9c !important;
  }
  </style>
</head>

<body>
<!-- Navbar -->

<nav class="navbar navbar-default">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">

        <span class="icon-bar"></span>

        <span class="icon-bar"></span>

        <span class="icon-bar"></span>                        

      </button>

      <a class="navbar-brand" href="#">NostraDomicile</a>

    </div>

    <div class="collapse navbar-collapse" id="myNavbar">

      <ul class="nav navbar-nav navbar-right">

        <li><a href="#">ABOUT</a></li>

        <li><a href="#">BLOG</a></li>

        <li><a href="#">CONTACT US</a></li>

      </ul>

    </div>

  </div>

</nav>

<!--Angular framework load -->

<script src = "https://ajax.googleapis.com/ajax/libs/angularjs/1.3.14/angular.min.js">

</script>





<!-- First Container -->

<div class="container-fluid bg-1 text-center">

  <h2 class="margin">Smart Solutions For Data Driven Real Estate Queries</h2>

  <img src="nostraPicture.jpg" class="img-responsive img-circle margin" style="display:inline" alt="Bird" width="300" height="300">

  </div>

  



<!-- Second Container -->

<div class="container-fluid bg-2 text-center">

  <h3 class="margin">Most Important Factors Leading to Sale by Zip Code</h3>

  <div class="form-group">

  <!--define app-->

<div ng-app = "NostraDomicile">



<p>Enter your Zip Code: <input type = "text" ng-model = "NostraDomicile"></p>

         <p><span ng-bind = "NostraDomicile"></span></p>

 </div>

 <div class="btn-toolbar">

    <!--Default buttons with dropdown menu-->

    <div class="btn-group">

        <button type="button" class="btn btn-default">Bedrooms</button>

        <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle"><span class="caret"></span></button>

        <ul class="dropdown-menu">

            <li><a href="#">6</a></li>

            <li><a href="#">5</a></li>

			<li><a href="#">4</a></li>

            <li><a href="#">3</a></li>

			<li><a href="#">2</a></li>

            <li><a href="#">1</a></li>

            

        </ul>

    </div>

	<div class="btn-group">

        <button type="button" class="btn btn-default">Bathrooms</button>

        <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle"><span class="caret"></span></button>

        <ul class="dropdown-menu">

            <li><a href="#">5.5</a></li>

            <li><a href="#">5</a></li>

			<li><a href="#">4.5</a></li>

            <li><a href="#">4</a></li>

			<li><a href="#">3.5</a></li>

            <li><a href="#">3</a></li>

			<li><a href="#">2.5</a></li>

			<li><a href="#">2</a></li>

            <li><a href="#">1.5</a></li>

			<li><a href="#">1</a></li>

                      

        </ul>

    </div>

	<div class="btn-group">

        <button type="button" class="btn btn-default">Blank</button>

        <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle"><span class="caret"></span></button>

        <ul class="dropdown-menu">

            <li><a href="#">6</a></li>

            <li><a href="#">5</a></li>

			<li><a href="#">4</a></li>

            <li><a href="#">3</a></li>

			<li><a href="#">2</a></li>

            <li><a href="#">1</a></li>

            

        </ul>

    </div>

	<div class="btn-group">

        <button type="button" class="btn btn-default">Blank</button>

        <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle"><span class="caret"></span></button>

        <ul class="dropdown-menu">

            <li><a href="#">6</a></li>

            <li><a href="#">5</a></li>

			<li><a href="#">4</a></li>

            <li><a href="#">3</a></li>

			<li><a href="#">2</a></li>

            <li><a href="#">1</a></li>

            

        </ul>

    </div>

	<div class="btn-group">

        <button type="button" class="btn btn-default">Blank</button>

        <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle"><span class="caret"></span></button>

        <ul class="dropdown-menu">

            <li><a href="#">6</a></li>

            <li><a href="#">5</a></li>

			<li><a href="#">4</a></li>

            <li><a href="#">3</a></li>

			<li><a href="#">2</a></li>

            <li><a href="#">1</a></li>

            

        </ul>

    </div>

	<div class="btn-group">

        <button type="button" class="btn btn-default">Blank</button>

        <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle"><span class="caret"></span></button>

        <ul class="dropdown-menu">

            <li><a href="#">6</a></li>

            <li><a href="#">5</a></li>

			<li><a href="#">4</a></li>

            <li><a href="#">3</a></li>

			<li><a href="#">2</a></li>

            <li><a href="#">1</a></li>

            

        </ul>

    </div>

	<div class="btn-group">

        <button type="button" class="btn btn-default">Blank</button>

        <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle"><span class="caret"></span></button>

        <ul class="dropdown-menu">

            <li><a href="#">6</a></li>

            <li><a href="#">5</a></li>

			<li><a href="#">4</a></li>

            <li><a href="#">3</a></li>

			<li><a href="#">2</a></li>

            <li><a href="#">1</a></li>

            

        </ul>

    </div>

	<div class="btn-group">

        <button type="button" class="btn btn-default">Blank</button>

        <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle"><span class="caret"></span></button>

        <ul class="dropdown-menu">

            <li><a href="#">6</a></li>

            <li><a href="#">5</a></li>

			<li><a href="#">4</a></li>

            <li><a href="#">3</a></li>

			<li><a href="#">2</a></li>

            <li><a href="#">1</a></li>

            

        </ul>

    </div>

	<div class="btn-group">

        <button type="button" class="btn btn-default">Blank</button>

        <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle"><span class="caret"></span></button>

        <ul class="dropdown-menu">

            <li><a href="#">6</a></li>

            <li><a href="#">5</a></li>

			<li><a href="#">4</a></li>

            <li><a href="#">3</a></li>

			<li><a href="#">2</a></li>

            <li><a href="#">1</a></li>

            

        </ul>

    </div>

	<div class="btn-group">

        <button type="button" class="btn btn-default">Blank</button>

        <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle"><span class="caret"></span></button>

        <ul class="dropdown-menu">

            <li><a href="#">6</a></li>

            <li><a href="#">5</a></li>

			<li><a href="#">4</a></li>

            <li><a href="#">3</a></li>

			<li><a href="#">2</a></li>

            <li><a href="#">1</a></li>

            

        </ul>

    </div>

	<div class="btn-group">

        <button type="button" class="btn btn-default">Blank</button>

        <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle"><span class="caret"></span></button>

        <ul class="dropdown-menu">

            <li><a href="#">6</a></li>

            <li><a href="#">5</a></li>

			<li><a href="#">4</a></li>

            <li><a href="#">3</a></li>

			<li><a href="#">2</a></li>

            <li><a href="#">1</a></li>

            

        </ul>

    </div>

	<div class="btn-group">

        <button type="button" class="btn btn-default">Blank</button>

        <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle"><span class="caret"></span></button>

        <ul class="dropdown-menu">

            <li><a href="#">6</a></li>

            <li><a href="#">5</a></li>

			<li><a href="#">4</a></li>

            <li><a href="#">3</a></li>

			<li><a href="#">2</a></li>

            <li><a href="#">1</a></li>

            

        </ul>

    </div>

	<div class="btn-group">

        <button type="button" class="btn btn-default">Blank</button>

        <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle"><span class="caret"></span></button>

        <ul class="dropdown-menu">

            <li><a href="#">6</a></li>

            <li><a href="#">5</a></li>

			<li><a href="#">4</a></li>

            <li><a href="#">3</a></li>

			<li><a href="#">2</a></li>

            <li><a href="#">1</a></li>

            

        </ul>

    </div>

	<div class="btn-group">

        <button type="button" class="btn btn-default">Blank</button>

        <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle"><span class="caret"></span></button>

        <ul class="dropdown-menu">

            <li><a href="#">6</a></li>

            <li><a href="#">5</a></li>

			<li><a href="#">4</a></li>

            <li><a href="#">3</a></li>

			<li><a href="#">2</a></li>

            <li><a href="#">1</a></li>

            

        </ul>

    </div>

    

    

</div>



  <!--<label for="usr">Please Enter Your Zip Code:</label>-->

  <!--<input type="text" class="form-control" id="usr">-->

  </div>

  </div>



<!-- Third Container (Grid) -->

<div class="container-fluid bg-1 text-center">

<div class="row">

<div class="col-sm-4">

<div class="card" style="width: 20rem;">

  <img class="card-img-top" src="houseSold.jpeg" alt="Card image cap">

  <div class="card-block">

    <h4 class="card-title">Prediction on Sale</h4>

    <p>Click the button below to see if your house will sell based on the attributes you have provided.</p>

    <a href="#" class="btn btn-primary">Will My House Sell?</a>

  </div>

  </div>

  </div>

  <div class="col-sm-4">

<div class="card" style="width: 20rem;">

  <img class="card-img-top" src="homeAtt.jpeg" alt="Card image cap">

  <div class="card-block">

    <h4 class="card-title">Prediction on Most Important Attributes</h4>

    <p>Click the button below to see the most attractive factors leading to home sales in the chosen area.</p>

    <a href="#" class="btn btn-primary">Most Important Attributes</a>

</div>

</div>

</div>

<div class="col-sm-4">

<div class="card" style="width: 20rem;">

  <img class="card-img-top" src="statsImage.jpeg" alt="Card image cap">

  <div class="card-block">

    <h4 class="card-title">Data Visualizations</h4>

    <p>Click the button below to see a collection of valuable statistics pertaining to the chosen area.</p>

    <a href="#" class="btn btn-primary">Data Visualizations</a>

  </div>

</div>

</div>

</div>

</div>

<!--<div class="container-fluid bg-3 text-center">    

  <h3 class="margin">Will Your House Sell?</h3><br>

  <div class="row">

    <div class="form-group">

  <!--<label for="usr">Please Enter Your Zip Code:</label>

  <input type="text" class="form-control" id="usr">-->

  <!--define app-->

<!--<div ng-app = "NostraDomicile">

<!--<div ng-app = "mainApp" ng-controller = "studentController">

         Enter first name: <input type = "text" ng-model = "student.firstName"><br><br>

         Enter last name: <input type = "text" ng-model = "student.lastName"><br>

         <br>

         

         You are entering: {{student.fullName()}}

      </div>

	   <script>

         var mainApp = angular.module("mainApp", []);

         

         mainApp.controller('studentController', function($scope) {

            $scope.student = {

               firstName: "Mahesh",

               lastName: "Parashar",

               

               fullName: function() {

                  var studentObject;

                  studentObject = $scope.student;

                  return studentObject.firstName + " " + studentObject.lastName;

               }

            };

         });

      </script>-->

<!--<p>Enter your Zip Code: <input type = "text" ng-model = "NostraDomicile"></p>

         <p><span ng-bind = "NostraDomicile"></span></p>

 </div>



  



<!-- Footer -->

<footer class="container-fluid bg-4 text-center">

  <p>Created as Senior Project</p> 

</footer>



</body>

</html>


	 """
	return HttpResponse(text)
