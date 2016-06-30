app = angular.module('library', ["ngRoute"]);
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
    $scope.author_id = ''
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
