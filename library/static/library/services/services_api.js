

app.factory("Books", function($resource) {
    return $resource('api/books/:id')
});