(function(){

    app = angular.module('apper', []);


    app.controller('PhoneListCtrl', function () {
      this.phones = gems;



    });

     var gems = [
    {'name': 'Nexus S',
     'snippet': 'Fast just got faster with Nexus S.'},
    {'name': 'Motorola XOOM™ with Wi-Fi',
     'snippet': 'The Next, Next Generation tablet.'},
    {'name': 'MOTOROLA XOOM™',
     'snippet': 'The Next, Next Generation tablet.'}
  ];




})();


(function(){


	var app = angular.module('store', []);

	app.controller('ReviewController', function  () {

		this.review = {};

		this.addReview = function  (product) {
			// body...
			product.reviews.push(this.review);
			this.review = {};


		};
		// body...
	});

	app.controller('PanelController', function  () {

		this.tab = 2;

		this.selectTab = function  (setTab) {
			this.tab = setTab;
		};

		this.isSelected = function  (checkTab) {

			return this.tab === checkTab;
		};
				// body...
	});

	app.controller('StoreController', function  () {
		// body...
		this.products = gems;

	});

	var gems = [{
		name: 'Decor',
		price: 23,
		desc: 'vvvv',
		canPurchase: true,
		soldOut: false,
		images: [
		{ full: 'contacto_bxf.jpg',
		  thumb: 'people_thumbs_up_008.jpg'}],
		 reviews: [
	{ stars: 5,
	  body: "Love something",
	  author: "anton@anton.ru"},
  { stars: 4,
  body: "Love something1111",
  author: "anton@anton.ru"}
	  ]},
		{
		name: 'Decor 4444',
		price: 234234,
		desc: 'vvvv',
		canPurchase: false,
		soldOut: false,},
		{
		name: 'Arkeline',
		price: 555,
		desc: 'vvvv',
		canPurchase: true,
		soldOut: false,

	}];




})();