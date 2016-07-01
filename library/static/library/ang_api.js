app = angular.module('library', ["ngRoute", "ui.bootstrap"]);
app.config(function ($routeProvider) {
    $routeProvider.when('/authors',
        {
            templateUrl:'/static/library/templates/authors.html',
            controller:'AuthorsController'
        });
    $routeProvider.when('/books',
        {
            templateUrl:'/static/library/templates/books.html',
            controller: 'BooksController'
        });
    $routeProvider.when('/add-author',
        {
            templateUrl:'/static/library/templates/test.html',
            controller: 'AddAuthorController'
        });
    $routeProvider.when('/add-book',
        {
            templateUrl:'/static/library/templates/test.html',
            controller: 'AddBookController'
        });
    $routeProvider.when('/books/:id',
        {
            templateUrl: '/static/library/templates/book_detail.html',
            controller: 'BookDetailController'
        });
});
app.controller('AuthorsController', function ($scope, $http) {
    $http({
        method:'GET',
        url: '/api/authors'
    }).then(function (responce) {
        $scope.data = responce.data;
    });
    $scope.page = 'Authors'
});

app.controller('BooksController', function ($scope, $http) {
    $http({
        method: "GET",
        url: '/api/books'
    }).then(function (responce) {
        $scope.books = responce.data;
    });
    // $scope.filter_by_title = '';
    $scope.page = 'Books'
    $scope.MyFilter = {
        selectedAuthorID:""
    }
});

app.controller('AddAuthorController', function ($scope, $http) {
    $http({
        method: 'GET',
        url: '/api/books'
    });
    $scope.page = 'addAuthor'
});

app.controller('AddBookController', function ($scope) {
    $scope.page = 'addBook'
});

app.controller('BookDetailController', function ($scope, $http, $routeParams) {
    var id = $routeParams["id"];
    $http({
        method:'GET',
        url:'/api/books/'+id,
        params: {id: id}
    }).then(function (responce) {
        $scope.data = responce.data;
    });
    $scope.page = 'DetailBook'

});
app.filter('unique', function(){
    return function (object) {
        var unique_array_id = [];
        var unique_authors = [];
        var author_id =0;
        if (object) {
            for(var i=0; i<object.length; i++) {
                author_id = object[i].author.id;
                if (unique_array_id.indexOf(author_id) ===-1){
                    unique_array_id.push(author_id);
                    unique_authors.push(object[i].author)
                }
            }
        }
        return unique_authors
    }
});
app.controller('DatepickerPopup', function ($scope) {
  $scope.today = function() {
    $scope.dt = new Date();
  };
  $scope.today();


  $scope.inlineOptions = {
    customClass: getDayClass,
    minDate: new Date(),
    showWeeks: false
  };

  $scope.dateOptions = {
    dateDisabled: disabled,
    formatYear: 'yy',
    maxDate: new Date(2020, 5, 22),
    minDate: new Date(),
    startingDay: 1
  };

  // Disable weekend selection
  function disabled(data) {
    var date = data.date,
      mode = data.mode;
    return mode === 'day' && (date.getDay() === 0 || date.getDay() === 6);
  }

  $scope.toggleMin = function() {
    $scope.inlineOptions.minDate = $scope.inlineOptions.minDate ? null : new Date();
    $scope.dateOptions.minDate = $scope.inlineOptions.minDate;
  };

  $scope.toggleMin();

  $scope.open1 = function() {
    $scope.popup1.opened = true;
  };

  $scope.open2 = function() {
    $scope.popup2.opened = true;
  };

  $scope.setStartDate = function(year, month, day) {
    $scope.dt = new Date(year, month, day);
  };
  $scope.setStopDate1 = function(year, month, day) {
    $scope.dt1 = new Date(year, month, day);
  };

  $scope.formats = ['yyyy-MM-dd', 'dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
  $scope.format = $scope.formats[0];
  $scope.altInputFormats = ['M!/d!/yyyy'];

  $scope.popup1 = {
    opened: false
  };

  $scope.popup2 = {
    opened: false
  };

  // var tomorrow = new Date();
  // tomorrow.setDate(tomorrow.getDate() + 1);
  // var afterTomorrow = new Date();
  // afterTomorrow.setDate(tomorrow.getDate() + 1);
  // $scope.events = [
  //   {
  //     date: tomorrow,
  //     status: 'full'
  //   },
  //   {
  //     date: afterTomorrow,
  //     status: 'partially'
  //   }
  // ];

  function getDayClass(data) {
    var date = data.date,
      mode = data.mode;
    if (mode === 'day') {
      var dayToCheck = new Date(date).setHours(0,0,0,0);

      for (var i = 0; i < $scope.events.length; i++) {
        var currentDay = new Date($scope.events[i].date).setHours(0,0,0,0);

        if (dayToCheck === currentDay) {
          return $scope.events[i].status;
        }
      }
    }

    return '';
  }
});