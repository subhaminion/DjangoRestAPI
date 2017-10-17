var app = angular.module('toDo', []);

app.controller('toDoController', function ($scope, $http) {
	// $scope.todoList = [{todoText: 'Finish this App...', done: false}];
	$http.get('/todo/api').then(function(response){
		$scope.todoList = [];
		for (var i = 0; i < response.data.length; i++) {
			var todo = {};
			todo.todoText = response.data[i].todo_text;
			todo.done = response.data[i].done;
			console.log(todo);
			$scope.todoList.push(todo);
		}
	});

	$scope.todoAdd = function(){
		$scope.todoList.push({todoText: $scope.todoInput, done: false});
		$scope.todoInput = '';
	};

	$scope.remove = function(){
		var oldList = $scope.todoList;
		$scope.todoList = [];
		angular.forEach(oldList, function(x){
			if(!x.done){
				$scope.todoList.push(x);
			}
		});
	};
})