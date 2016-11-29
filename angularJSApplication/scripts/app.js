(function(){
	var app = angular.module('store', [ 'store-products']);

	app.controller('StoreController', function(){
		this.products = gems;
	});
	var gems = [
		{
			name : "Dodecahedron",
			price : 2.25,
			description : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. \
						Perferendis omnis accusantium dicta provident, \
						nihil dolorem eligendi ipsum iure expedita reiciendis totam \
						harum placeat veritatis a voluptatibus esse atque velit, eaque.",
			canPurchase : true,
			soldOut : false,
			images : [
				{
					full: "assets/img/gem-01.gif",
					thumb: "assets/img/gem-02.gif"
				}
			],
            reviews: [{
              stars: 5,
              body: "I love this gem!",
              author: "joe@thomas.com",
              createdOn: 1397490980837
            }, {
              stars: 1,
              body: "This gem sucks.",
              author: "tim@hater.com",
              createdOn: 1397490980837
            }]
		},
		{
			name : "Pentagonal Gems",
			price : 5.95,
			description : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. \
						Perferendis omnis accusantium dicta provident, \
						nihil dolorem eligendi ipsum iure expedita reiciendis totam \
						harum placeat veritatis a voluptatibus esse atque velit, eaque.",
			canPurchase : true,
			soldOut : false,
			images : [
				{
					full: "assets/img/gem-03.gif",
					thumb: "assets/img/gem-04.gif"
				}
			],
            reviews: [{
                stars: 3,
                body: "I think this gem was just OK, could honestly use more shine, IMO.",
                author: "JimmyDean@sausage.com",
                createdOn: 1397490980837
                }, {
                stars: 4,
                body: "Any gem with 12 faces is for me!",
                author: "gemsRock@alyssaNicoll.com",
                createdOn: 1397490980837,
                date:'medium'
            }]
		}
	];

	app.controller('PanelController', function(){

	});

    app.controller('ReviewControler', function(){
        this.review = {};
        this.addReview = function(product){
            product.reviews.push(this.review);
            this.review = {};
        };
    });


})();
