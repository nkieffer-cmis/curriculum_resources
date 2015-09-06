$(function(){
	document.Resource = Backbone.Model.extend({
	    idAttribute: "key"
	});
    
	document.ResourceCollection = Backbone.Collection.extend({
		model: document.Resource,
		url: "/resource"
	});

	document.Resources = new document.ResourceCollection;
	document.ResourceView = Backbone.View.extend({
		el: $("#resources"),
		template: _.template($('#resource-tmp').html(),{}),
		render: function(is_admin) {
		    console.dir(this.model);
		    console.log("ID: "+this.model.key);
		    this.model.is_admin = is_admin;
		    this.$el.append(this.template(this.model));
		   /* reviewInput = new document.ReviewInput({ resourceId: this.model.id });
		    reviewInput.resourceId = this.model.id;
		    document.ReviewInputs.push(reviewInput);
		    reviewInput.render();
		    */
		    return this;
		}
	});

	document.Resources.fetch({
		success: function(collection, response, options){
		    console.log(response);
		    is_admin = response[0]
			_.each(response[1], function(resource){
				var view = new document.ResourceView({model: resource});
				view.render(is_admin);
			});
		}
	});
	console.dir(document.Resources.length);
		
});
