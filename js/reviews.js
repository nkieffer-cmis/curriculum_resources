$(function(){
	document.Review = Backbone.Model.extend({
		defaults: {
			"text" : ""
		}
	});
	
	document.ReviewCollection = Backbone.Collection.extend({
		model: document.Review,
		url: "/review"
	});

	document.Reviews = new document.ReviewCollection;
	
	document.ReviewInput = Backbone.View.extend({
		resourceId: null,
		tagName: "textarea",
		className: "new-review",
		render: function(){
			console.log(this.$el);
			console.log($("#resource:"+this.resourceId));
			$("#resource:"+this.resourceId).append($(this.el));
			return this;
		},
		events: {
			"change" : "createReview"
		},
		createReview: function(e){
			alert(e.target.innerHTML);
		}
	});
	
	document.ReviewInputs = new Array();
			
});
